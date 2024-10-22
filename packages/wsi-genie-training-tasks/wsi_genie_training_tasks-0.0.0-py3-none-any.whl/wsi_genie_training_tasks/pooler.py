import sys
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Union, Generator, Dict, Any, Tuple
from torch import nn
import torch
import numpy as np
import h5py
from DatasetManager import FeatureDataset, stratified_split
from torch.utils.data import DataLoader
from torch.nn import CrossEntropyLoss
from torch_optimizer import RAdam
from torch_optimizer import Lookahead
import xml.etree.cElementTree as ET
from config import Config as cfg
import os
import cv2
from TransMIL.model import TransMIL
from config import Config

# Import TransMIL Model
from TransMIL.model import TransMIL

# TransMIL = importlib.import_module("TransMIL-visualisation.model.TransMIL")

if torch.backends.mps.is_available():
    device = torch.device('mps')
elif torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')

class Pooler(ABC):
    def __init__(self, options: Dict[str, Any]):
        self.options = options
    
    # @classmethod
    # @abstractmethod
    # def get_options(cls) -> List[Dict[str, Union[str, List[str]]]]:
    #     """
    #     Returns a list of dictionaries containing the name, type, and choices (if applicable) 
    #     of the options for the model.
    #     """
    #     pass



# Pulled from TransMIL-visualisation
def calcTileAttns(attns: List[torch.Tensor], y_hat):
    result = torch.ones(attns[0].shape).to(attns[0].device)
    for i, attn in enumerate(attns):
        torch.cuda.empty_cache()
        torch.cuda.empty_cache()
        torch.cuda.empty_cache()
        torch.cuda.empty_cache()
        torch.cuda.empty_cache()
        torch.cuda.empty_cache()
        attn = attn / (attn.max())
        result = ((attn * result) + result) / 2
    attns = result[0, 1:].to('cpu')
    if True:
        epsilon = 1e-10
        attns = attns + epsilon
        attns = attns.exp()
        min_val = attns.min()
        max_val = attns.max()
        attns = (attns - min_val) / (max_val - min_val)
    else:
        attns = attns.max()
        attns = attns * 0.1

    return attns

class TransMILPooler(Pooler):
    def __init__(self, num_epochs = 100, input_size=1024, early_stopping = True, patience = 5, val_split = .2, random_state = None, model = None, patch_size=256, callback_fn = None):
        self.num_epochs = num_epochs
        self.early_stopping = early_stopping
        self.patience = patience
        self.val_split = val_split
        self.random_state = random_state
        self.patch_size = patch_size
        self.input_size = input_size
        if model is not None:
            self.model = torch.load(model).to(device=device)
        self.callback_fn = callback_fn

    # def get_options(cls):
    #     pass

    def train(self, features: Union[List[str], List[np.ndarray]], feature_extractor,):
        # Dataset and loaders
        ds = FeatureDataset(features)
        ds_train, _, ds_val, _ = stratified_split(ds, ds.labels, 1-self.val_split, self.random_state)
        train_loader = DataLoader(ds_train, 1, num_workers=8, shuffle=True)
        val_loader = DataLoader(ds_val, 1, num_workers=8)
        # print(f"{len(ds_train)=}, {len(ds_val)=}")
        # Model
        self.model: nn.Module = TransMIL.TransMIL( n_classes=len(ds.class_idx_map), input_size=self.input_size).to(device=device)

        # Lookahead RAdam
        optimizer = RAdam(self.model.parameters(), lr=0.0002, weight_decay=0.00001)
        optimizer = Lookahead(optimizer)

        # Loss function
        loss_fn = CrossEntropyLoss()

        # Init for early stopping / preserving best model
        best_val_loss = float('inf')
        best_model_weights = None
        epochs_since_improvement = 0

        preogress_report_epochs = []
        preogress_report_train_losses = []
        preogress_report_train_accuracies = []
        preogress_report_val_losses = []
        preogress_report_val_accuracies = []

        for epoch in range(self.num_epochs):
            # Do training
            running_tloss = 0.0
            tcorrect_count = 0
            train_predictions = []
            train_labels = []
            self.model.train()
            for batch_idx, (coords, features, label) in enumerate(train_loader):
                forward_pass_outputs, attentions = self.model(features.to(device=device))
                loss = loss_fn(forward_pass_outputs['logits'], label.to(device=device))
                running_tloss += loss
                tcorrect_count += 1 if forward_pass_outputs['Y_hat'].item() == label.item() else 0
                train_predictions.append(forward_pass_outputs['Y_hat'].item())
                train_labels.append(label.item())
                # for name, param in self.model.named_parameters():
                #     print(name, param.grad)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                if batch_idx % 50 == 0 and batch_idx > 0:
                    print(f'Epoch: {epoch}, Batch: {batch_idx}')

            # Do validation
            self.model.eval()  # Set model to evaluation mode
            running_vloss = 0.0
            vcorrect_count = 0
            val_predictions = []
            val_labels = []
            with torch.no_grad():  # Disable gradient calculation for validation
                for i, (coords, features, label) in enumerate(val_loader):
                    forward_pass_outputs, attentions = self.model(features.to(device=device))
                    vloss = loss_fn(forward_pass_outputs['Y_prob'], label.to(device=device))
                    running_vloss += vloss
                    vcorrect_count += 1 if forward_pass_outputs['Y_hat'].item() == label.item() else 0
                    val_predictions.append(forward_pass_outputs['Y_hat'].item())
                    val_labels.append(label.item())
            avg_vloss = running_vloss.item() / len(ds_val) if len(ds_val) > 0 else float('inf')
            avg_tloss = running_tloss.item() / len(ds_train) if len(ds_train) > 0 else float('inf')
            val_accuracy = vcorrect_count / len(ds_val) if len(ds_val) > 0 else 0
            train_accuracy = tcorrect_count / len(ds_train) if len(ds_train) > 0 else 0
            print(f'Train: {list(zip(train_labels, train_predictions))}')
            print(f'Val: {list(zip(val_labels, val_predictions))}')
            # print(f'Epoch {epoch} Complete; Avg Loss: Val:{avg_vloss}; Accuracy: Val: {accuracy}')

            # Perform early stopping checks
            if round(best_val_loss, 4) > round(avg_vloss, 4) or (best_val_loss == float('inf') and avg_vloss == float('inf')): # Better or too little data for validation
                # Save best results
                best_val_loss = avg_vloss
                best_model_weights = self.model.state_dict()
                # reset patience
                epochs_since_improvement = 0
            else:
                epochs_since_improvement += 1


            # Updating values to send report
            preogress_report_epochs.append(epoch)
            preogress_report_train_losses.append(avg_tloss)
            preogress_report_val_losses.append(avg_vloss)
            preogress_report_train_accuracies.append(train_accuracy)
            preogress_report_val_accuracies.append(val_accuracy)
            
            progress_report = {'progress_total':self.num_epochs,
                    'progress_done':epoch+1,
                    'epochs_since_improvement': epochs_since_improvement, 
                    'patience': self.patience,
                    'epochs': preogress_report_epochs,
                    'train_losses': preogress_report_train_losses, 
                    'val_losses': preogress_report_val_losses,
                    'train_accuracies': preogress_report_train_accuracies, 
                    'val_accuracies': preogress_report_val_accuracies}
            
            if self.early_stopping and epochs_since_improvement >= self.patience:
                #early stopping triggered, exit epoch loop, call the update function for last time to update progressbar
                progress_report['progress_total'] = epoch+1
                self.callback_fn('training-update',progress_report)    
                
                break
            print(f"Epoch complete: {progress_report}")
            self.callback_fn('training-update',progress_report)

        # Load best model
        self.model.load_state_dict(best_model_weights)

        # Perform a final test with the best model on the training data and the validation data
        train_features = [ds.files[i] for i in ds_train.indices]
        val_features = [ds.files[i] for i in ds_val.indices]

        # Add stitches path before calling test function
        # TODO: Update and make it better instead of just a workaround


        print('Training done, running testing on training data for final performance')
        print(f"{train_features=}")
        print(f"{val_features=}")


        train_stitches = Path(str(train_features[0]).replace(f"{Config.FEATURE_DATA_FOLDER}/{feature_extractor}",f"{Config.STITCHES_FOLDER}"))
        val_stitches = Path(str(val_features[0]).replace(f"{Config.FEATURE_DATA_FOLDER}/{feature_extractor}",f"{Config.STITCHES_FOLDER}"))

        # Find the index of the STITCHES_FOLDER in the path parts
        parts = train_stitches.parts
        print(f"{parts}\t{Config.STITCHES_FOLDER}")
        train_stitches_index = train_stitches.parts.index(str(Config.STITCHES_FOLDER))
        val_stitches_index = val_stitches.parts.index(str(Config.STITCHES_FOLDER))
        
        # Create a new path with parts up to and including STITCHES_FOLDER
        train_stitches_dir = Path(*train_stitches.parts[:train_stitches_index+1])
        val_stitches_dir = Path(*val_stitches.parts[:val_stitches_index+1])

        print(f"{train_stitches_dir=}")
        print(f"{val_stitches_dir=}")
        # print(f"{train_stitches.with_name(Config.STITCHES_FOLDER)=}")
        final_train_predictions, _ = self.test(train_features, train_stitches_dir)
        final_val_predictions, _ = self.test(val_features, val_stitches_dir)

        final_progress_report = { 'total_epochs': epoch+1,
                'val_losses': preogress_report_val_losses,
                'val_accuracies': preogress_report_val_accuracies,
                'train_losses': preogress_report_train_losses,
                'train_accuracies': preogress_report_train_accuracies,
                'final_train_predictions': final_train_predictions,
                'final_val_predictions': final_val_predictions,
        }
        return self.model, ds.class_idx_map, final_progress_report

    def test(self, features: List[Path], stitch_directory):
        
        # Get the image IDs
        image_ids = [f.stem for f in features]
        
        # Determine file destinations
        

        # Get location of stitched thumbnails
        stitch_paths = list(stitch_directory.rglob('*.jpg'))
        # jpg_dests = Path(str(stitch_paths).replace("stitches", 'attention_results'))
        jpg_dests = [Path(str(stitch_path).replace("stitches", 'attention_results')) for stitch_path in stitch_paths]
        # jpg_dests = [cfg.ATTENTION_HEATMAP_FOLDER/ Path(f).relative_to(cfg.FEATURE_DATA_FOLDER).with_suffix('.jpg') for f in features] # Attention jpg heatmap
        # stitch_paths = [cfg.STITCHES_FOLDER/ Path(f).relative_to(cfg.FEATURE_DATA_FOLDER).with_suffix('.jpg') for f in features]
        
        # Dataset and loaders
        dataset = FeatureDataset(features)
        test_loader = DataLoader(dataset, 1, num_workers=8)
        predictions_list = []
        correct_preds = 0 # Correct preds counter to calculate live accuracy
        
        self.model.eval()  # Set model to evaluation mode
        with torch.inference_mode():  # Disable gradient calculation for validation
            for i, (coords, features, label) in enumerate(test_loader):
                # Make predictions
                forward_pass_outputs, attentions = self.model(features.to(device=device))

                # Calculate attentions per tile
                attns = calcTileAttns(attentions, forward_pass_outputs['Y_hat'].item())
                
                # Create thumbnail image of heatmap
                patch_size = 256
                thumbnail_path = stitch_paths[i]

                downsample = 64
                downsample_patchsize = int(patch_size//downsample)
                img = cv2.imread(str(thumbnail_path))

                mask = np.zeros((int(img.shape[0]),int(img.shape[1])))
                mask1 = np.ones((int(downsample_patchsize),int(downsample_patchsize)))
                coords = coords[0]
                for coords_i in range(coords.shape[0]):
                    # print(coords[coords_i][1])
                    x = int(coords[coords_i][1]//downsample)
                    y = int(coords[coords_i][0]//downsample)
                    if x+downsample_patchsize < mask.shape[0] and y+downsample_patchsize < mask.shape[1]:
                        mask[x:x+downsample_patchsize,y:y+downsample_patchsize] = attns[coords_i]*mask1
                #print(mask.max())
                img = np.float32(img)/255
                mask = cv2.resize(mask,(img.shape[1],img.shape[0]))
                heatmap = cv2.applyColorMap(np.uint8(255*mask), cv2.COLORMAP_JET)
                heatmap = np.float32(heatmap) / 255
                cam = heatmap + np.float32(img)
                cam = cam / np.max(cam)

                os.makedirs(jpg_dests[i].parent, exist_ok=True)
                cv2.imwrite(str(jpg_dests[i]), np.uint8(255 * cam))

                # Unpack predictions from tensor items and batch array
                pred = forward_pass_outputs['Y_hat'].item()
                correct_preds += (pred == label.item())
                prediction = {'Y_hat':pred,
                          'Y_prob':forward_pass_outputs['Y_prob'].tolist()[0],
                          'logits':forward_pass_outputs['logits'].tolist()[0],
                          'label':label.item(),
                          # 'tile_attns':attns.tolist(),
                          'attn_jpg':str(jpg_dests[i]),
                          'image_id':str(image_ids[i])}
                predictions_list.append(prediction)
                
                progress = {
                    'progress_done': i+1,
                    'progress_total': len(dataset),
                    'accuracy': correct_preds/(i+1),
                    'predictions': predictions_list,
                }
                print(f"{progress=}")
                self.callback_fn('testing-update', progress)
        # Returns list of predictions and accuracy
        return predictions_list, correct_preds/(len(dataset))

if __name__ == '__main__':
    features = [Path('feature_data/training/tiny_camel_train/negative/normal_002.h5'), 
                Path('feature_data/training/tiny_camel_train/negative/normal_001.h5'), 
                Path('feature_data/training/tiny_camel_train/positive/tumor_001.h5'), 
                Path('feature_data/training/tiny_camel_train/positive/tumor_002.h5')]
    p = TransMILPooler()
    reports = p.train(features)

 
       
        
                
                


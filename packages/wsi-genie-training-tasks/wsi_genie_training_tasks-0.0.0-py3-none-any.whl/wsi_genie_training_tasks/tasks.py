from pathlib import Path
from girder_worker.app import app
from girder_worker.utils import girder_job
from config import Config
from preprocessing.patcher import patch
from preprocessing.extractor import Extractor
from pooler import TransMILPooler

# TODO: Fill in the function with the correct argument signature
# and code that performs the task.
@girder_job(title='Example Task')
@app.task(bind=True)
def example_task(self):
    pass



@girder_job(title='Start Patching')
@app.task(bind=True)
def start_patching(self, slides_list, base_directory, patch_size=256, dataset_role='train'):
    print("***********************Patching")
    patch_files_list = []

    patch_directory = Path(base_directory, Config.PATCHES_FOLDER, dataset_role, f"size_{patch_size}")
    stitch_directory = Path(base_directory, Config.STITCHES_FOLDER, dataset_role, f"size_{patch_size}")

    for idx, wsi_file in enumerate(slides_list):
        patch_save_path = Path(patch_directory, wsi_file.parent.stem, wsi_file.with_suffix(".h5").name)
        stitch_save_path = Path(stitch_directory, wsi_file.parent.stem, wsi_file.with_suffix(".jpg").name)

        patch_file_path, stitch_file_path, pre_existing = patch(wsi_file, patch_size=patch_size,
                                                                patch_save_path=patch_save_path, 
                                                                stitch_save_path=stitch_save_path,
                                                                skip_existing=True)
        patch_files_list.append(patch_file_path)
        self.job_manager.write({'progress': (idx + 1) / len(slides_list)})

    return str(patch_directory), str(stitch_directory)

@girder_job(title='Start Feature Extraction')
@app.task(bind=True)
def start_feature_extraction(self, slides_list, base_directory, feature_extractor, patch_files_directory, dataset_role='train'):
    print("***********************Extracting")
    features_directory = Path(base_directory, Config.FEATURE_DATA_FOLDER)
    extractor = Extractor(model_name=feature_extractor)
    feature_files_list = []
    patch_directory = Path(Config.APPDATA_FOLDER, Config.PATCHES_FOLDER)
    for idx, wsi_file in enumerate(slides_list):
        parent_directory = Path(*wsi_file.parts[-2:])
        patch_path = Path(patch_files_directory, parent_directory).with_suffix(".h5")
        feature_save_path = Path(features_directory, feature_extractor, patch_path.relative_to(patch_directory)).with_suffix(".h5")
        feature_file_path, pre_existing = extractor.extract(wsi_file, feature_save_path=feature_save_path, patch_file_path=patch_path, skip_existing=True)
        feature_files_list.append(feature_file_path)
        self.job_manager.write({'progress': (idx + 1) / len(slides_list)})

    feature_map_size = extractor.get_feature_map_size()
    return feature_files_list, feature_map_size

@girder_job(title='Start Model Training')
@app.task(bind=True)
def start_model_training(self, feature_files, feature_map_size, model_save_path: Path, num_epochs, early_stopping, patience, validation_split, feature_extractor):
    trainer = TransMILPooler(num_epochs=num_epochs, input_size=feature_map_size, random_state=42, early_stopping=early_stopping, patience=patience, val_split=validation_split)
    model, class_map, progress = trainer.train(feature_files, feature_extractor)
    model_save_path.mkdir(parents=True, exist_ok=True)
    # # torch.save(model, Path(model_save_path, f'{Config.CLASSIFIER_NAME}'))
    # with open(Path(model_save_path, f'class_map.json'), "w") as outfile:
    #     outfile.write(json.dumps(class_map))

    # self.job_manager.write({'status': 'training-complete'})
    return progress

# -*- coding: utf-8 -*-

"""Top-level package for WSI Genie training tasks."""

__author__ = """Parth"""
__email__ = 'pas353@pitt.edu'
__version__ = '0.0.0'


from girder_worker import GirderWorkerPluginABC


class WsiGenieTrainingTasks(GirderWorkerPluginABC):
    def __init__(self, app, *args, **kwargs):
        self.app = app

    def task_imports(self):
        # Return a list of python importable paths to the
        # plugin's path directory
        return ['wsi_genie_training_tasks.tasks']

'''
CausalBench Utils:
Publish_all.py
This method publishes all available .zip files in a specified folder path as PUBLIC.
-kpkc
'''

import sys
import os
from unittest.mock import patch

#from Scripts.snkc import public

from causalbench.modules.dataset import Dataset
from causalbench.modules.model import Model
from causalbench.modules.metric import Metric
from causalbench.modules.context import Context

# # Specify the folder containing the zip files
folder_path = '../tests/'

# Function that mocks input and always returns 'Y'
def mock_input(prompt):
    if 'y' in prompt.lower() or 'n' in prompt.lower():
        return 'y'  # Automatically answer "Y" to yes/no prompts
    return 'y'  # Default response in other cases

response = input("=== Know that using this method will override further prompts, "
                 "and will publish everything unless stopped. Do you want to continue? (y/n): ===").strip().lower()

if response == 'y':
    print("Continuing...")
else:
    print("Exiting")
    sys.exit()
datasetAbalone = Dataset(module_id=1, version=1)
modelPC = Model(module_id=3, version=1)
modelGES = Model(module_id=2, version=1)
metricF1 = Metric(module_id=3, version=1)
metricPrecision = Metric(module_id=5, version=1)

context2: Context = Context.create(module_id=1,name='PC Hyperparameter Tuning',
                                       description='Tuning PC hyperparameter on Abalone',
                                       task='discovery.static',
                                       datasets=[(datasetAbalone, {'data': 'file1', 'ground_truth': 'file2'})],
                                       models=[(modelPC, {'alpha': 0.001}), (modelPC, {'alpha': 0.08})],
                                       metrics=[(metricF1, {}), (metricPrecision,{})])
context2.publish(public=True)
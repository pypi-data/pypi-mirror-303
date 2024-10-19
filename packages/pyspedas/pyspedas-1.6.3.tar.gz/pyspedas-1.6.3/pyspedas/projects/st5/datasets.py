from .load import load
from pyspedas.utilities.datasets import find_datasets

# This routine was originally in st5/__init__.py, until being moved to its own file.
# Please refer to __init__.py if you need to see the revision history before it was moved.

def datasets(instrument=None, label=True):
    return find_datasets(mission='ST5', instrument=instrument, label=label)

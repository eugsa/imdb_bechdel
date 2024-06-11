import inspect
import os
from config import *

def get_filepath(filename, path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, path + filename)
    return filepath
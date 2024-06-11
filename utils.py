import inspect
import os
from config import *

def get_filepath(function_name, path, file_extension):
  filename = function_name.split('generate_')[1] + file_extension
  script_dir = os.path.dirname(os.path.abspath(__file__))
  filepath = os.path.join(script_dir, path + filename)
  return filepath
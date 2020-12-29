import os, shutil

# GUI FUNCTIONS
from autogui.main import App, Button, Label, Font, Image, Table
from autogui.main import Dropdown, Popup, Inputfield, Slider, Checkbox

# UTIL FUNCTIONS
from autogui.auto import Auto


def remove_pycache_folder(path="./"):
	if os.path.exists(path+"autogui/__pycache__/"):
		shutil.rmtree(path+'autogui/__pycache__/')
remove_pycache_folder()


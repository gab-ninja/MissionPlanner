import sys
import os
from cx_Freeze import setup, Executable

#os.environ['TCL_LIBRARY'] = "C:\\Program Files\\Anaconda3\\tcl\\tcl8.6"
#os.environ['TK_LIBRARY'] = "C:\\Program Files\\Anaconda3\\tcl\\tk8.6"
os.environ['TCL_LIBRARY'] = "C:\\Users\\Mario\\Downloads\\tk868-src\\tk8.6.8\\win"
os.environ['TK_LIBRARY'] = "C:\\Users\\Mario\\Downloads\\tk868-src(1)\\tk8.6.8\\win"

includefiles = ['functions.py', 'julian_date_util.py', 'Earth-big.png', 'Earth-small.png', 'Jupiter-small.png', 'Mars-small.png', 'MDS-logo-small.png', 'MDS-logo.ico', 'MDS-logo.png', 'Mercury-small.png', 'Moon-small.png', 'Neptune-small.png', 'planet_data.txt', 'Pluto-small.png', 'Saturn-small.png', 'Sun-small.png', 'template.png', 'Uranus-small.png', 'Venus-small.png']
build_exe_options = {'include_files':includefiles }

setup(
    name = 'myapp',
    version = '0.1',
    description = 'A general enhancement utility',
    author = 'lenin',
    author_email = 'le...@null.com',
    options = {"build_exe": build_exe_options},
    executables = [Executable('mainwindow.py')]
)


#from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
#build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
#base = None
#if sys.platform == "win32":
#    base = "Win32GUI"
#
#setup(  name = "guifoo",
#        version = "0.1",
#        description = "My GUI application!",
#        options = {"build_exe": build_exe_options},
#        executables = [Executable("guifoo.py", base=base)])
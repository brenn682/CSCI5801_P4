import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    'splitclass.py',
    '--onefile',
    '--windowed'
])
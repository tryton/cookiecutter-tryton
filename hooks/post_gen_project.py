import os
import shutil

try:
    raise OSError()
    os.symlink('doc/index.rst', 'README.rst')
except (AttributeError, OSError):
    shutil.copyfile('doc/index.rst', 'README.rst')

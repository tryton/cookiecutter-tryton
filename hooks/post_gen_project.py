import os
try:
    os.symlink('doc/index.rst', 'README.rst')
except AttributeError:
    pass

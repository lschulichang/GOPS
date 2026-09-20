
import os, site, sys

# First, drop system-sites related paths.
original_sys_path = sys.path[:]
known_paths = set()
for path in {'e:\\miniconda\\envs\\gops\\lib\\site-packages', 'e:\\miniconda\\envs\\gops'}:
    site.addsitedir(path, known_paths=known_paths)
system_paths = set(
    os.path.normcase(path)
    for path in sys.path[len(original_sys_path):]
)
original_sys_path = [
    path for path in original_sys_path
    if os.path.normcase(path) not in system_paths
]
sys.path = original_sys_path

# Second, add lib directories.
# ensuring .pth file are processed.
for path in ['E:\\GOPS\\.setup-tmp\\pip-build-env-4d5wk2f2\\overlay\\Lib\\site-packages', 'E:\\GOPS\\.setup-tmp\\pip-build-env-4d5wk2f2\\normal\\Lib\\site-packages']:
    assert not path in sys.path
    site.addsitedir(path)

"""""" # start delvewheel patch
def _delvewheel_patch_1_8_2():
    import ctypes
    import os
    import platform
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'roughpy.libs'))
    is_conda_cpython = platform.python_implementation() == 'CPython' and (hasattr(ctypes.pythonapi, 'Anaconda_GetVersion') or 'packaged by conda-forge' in sys.version)
    if sys.version_info[:2] >= (3, 8) and not is_conda_cpython or sys.version_info[:2] >= (3, 10):
        if os.path.isdir(libs_dir):
            os.add_dll_directory(libs_dir)
    else:
        load_order_filepath = os.path.join(libs_dir, '.load-order-roughpy-0.1.2')
        if os.path.isfile(load_order_filepath):
            import ctypes.wintypes
            with open(os.path.join(libs_dir, '.load-order-roughpy-0.1.2')) as file:
                load_order = file.read().split()
            kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
            kernel32.LoadLibraryExW.restype = ctypes.wintypes.HMODULE
            kernel32.LoadLibraryExW.argtypes = ctypes.wintypes.LPCWSTR, ctypes.wintypes.HANDLE, ctypes.wintypes.DWORD
            for lib in load_order:
                lib_path = os.path.join(os.path.join(libs_dir, lib))
                if os.path.isfile(lib_path) and not kernel32.LoadLibraryExW(lib_path, None, 8):
                    raise OSError('Error loading {}; {}'.format(lib, ctypes.FormatError(ctypes.get_last_error())))


_delvewheel_patch_1_8_2()
del _delvewheel_patch_1_8_2
# end delvewheel patch

import importlib.metadata as _ilm
import os
import platform

from pathlib import Path as _Path

try:
    __version__ = _ilm.version("RoughPy")
except _ilm.PackageNotFoundError:
    __version__ = "0.0.0"


def _add_dynload_location(path: _Path):
    if platform.system() == "Windows":
        os.add_dll_directory(str(path))
        return


if platform.system() == "Windows":
    LIBS_DIR = _Path(__file__).parent.parent / "roughpy.libs"
    if LIBS_DIR.exists():
        os.add_dll_directory(str(LIBS_DIR))

try:
    iomp = _ilm.distribution("intel-openmp")
    libs = [f for f in iomp.files if f.name.startswith("libiomp5")]
    if libs:
        _add_dynload_location(libs[0].locate().resolve().parent)
    del iomp
    del libs
except _ilm.PackageNotFoundError:
    pass

import roughpy._roughpy
from roughpy._roughpy import *

from . import tensor_functions


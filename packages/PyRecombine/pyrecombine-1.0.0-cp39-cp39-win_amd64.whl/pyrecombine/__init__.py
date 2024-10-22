"""""" # start delvewheel patch
def _delvewheel_patch_1_8_2():
    import ctypes
    import os
    import platform
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'pyrecombine.libs'))
    is_conda_cpython = platform.python_implementation() == 'CPython' and (hasattr(ctypes.pythonapi, 'Anaconda_GetVersion') or 'packaged by conda-forge' in sys.version)
    if sys.version_info[:2] >= (3, 8) and not is_conda_cpython or sys.version_info[:2] >= (3, 10):
        if os.path.isdir(libs_dir):
            os.add_dll_directory(libs_dir)
    else:
        load_order_filepath = os.path.join(libs_dir, '.load-order-pyrecombine-1.0.0')
        if os.path.isfile(load_order_filepath):
            import ctypes.wintypes
            with open(os.path.join(libs_dir, '.load-order-pyrecombine-1.0.0')) as file:
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

import os
import platform
import fnmatch
import sysconfig

from importlib import metadata as _ilm
from pathlib import Path as _Path
from ctypes import CDLL as _CDLL



def _locate_file(module: str, name: str) -> _Path:
    """
    Locate a file within a module and return the correct absolute path to
    where the file is installed on the filesystem.

    This function raises an importlib.metadata.PackageNotFoundError upon
    failure.

    :param module: name of the module to locate a file within
    :param name: name of the file to find
    :return: Absolute path to the file as a pathlib.Path object
    """
    dist = _ilm.distribution(module)

    files = [dist.locate_file(path).resolve() for path in dist.files if fnmatch.fnmatch(path.name, name)]

    if not files:
        raise _ilm.PackageNotFoundError(f"Could not find {name} within {module}")

    file = files[0]
    assert file.exists()

    return file

if platform.system() == "Linux":

    # This is critical, the MKL libraries have complicated interdependencies
    # https://stackoverflow.com/a/53343430/9225581
    mode = os.RTLD_GLOBAL | os.RTLD_LAZY

    try:
        _IOMP = _CDLL(str(_locate_file("intel_openmp", "libiomp5.so")), mode=mode)
        # _MKL_CORE = _CDLL(str(_locate_file("mkl", "libmkl_core.so.2")), mode=mode)
        # _MKL_INTEL_THREAD = _CDLL(str(_locate_file("mkl", "libmkl_intel_thread.so.2")), mode=mode)
        # _MKL_ILP64 = _CDLL(str(_locate_file("mkl", "libmkl_intel_ilp64.so.2")), mode=mode)

    except _ilm.PackageNotFoundError as e:
        raise ImportError("Could not find the MKL libraries") from e

elif platform.system() == "Windows":
    try:
        for mod, name in [("intel_openmp", "libiomp5md.dll")]:
            loc = _locate_file(mod, name)
            os.add_dll_directory(str(loc.parent))
            # _CDLL(str(loc))
            print(f"Loaded {mod}/{name} from {loc}")

    except _ilm.PackageNotFoundError as e:
        raise ImportError("Could not find the MKL libraries") from e






from ._recombine import *

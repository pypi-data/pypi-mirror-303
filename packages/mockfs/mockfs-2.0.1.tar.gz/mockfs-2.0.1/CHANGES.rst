v2.0.1
======
    * ``setup.cfg`` was removed and replaced by ``pyproject.toml``.
    * Documentation is now available at
      `mockfs on readthedocs <https://mockfs.readthedocs.org>`_ in addition to the
      github-hosted pages site.

v2.0.0
======
    * `mockfs.MockFS` can now be used as a context manager.
    * The build system is now Python3-only and has been modernized for PEP-517/518.
    * `replace_builtins()` now patches `io.open` as well.
    * Code is now formatted using `cercis`.

v1.1.3
======
    * `replace_builtins()` now patches `codecs.open` as well.

v1.1.2
======
    * Restored Python 2 compatibility. Python 2 compatibility will be removed in a
      future release.
    * Properly handle writing bytes on Python 3.

v1.1.1
======
    * Skip patching `os.getcwdu` in `mockfs.install` on Python 3.
    * Code is now formatted using `black`.
    * Add Tox testing integration wtih Travis-CI.
    * Improve Python 3 compatibility.
    * Adopt `jaraco/skeleton <https://github.com/jaraco/skeleton>_`
      as our project skeleton.

v1.1.0
======
    * More Python 3 improvements.
    * Switch to pytest.

v1.0.2
======
    * Add Travis-CI testing.
    * Only patch `os.getcwdu` on Python 2.
    * Only patch `os.file` on Python 2.
    * `setuptools` packaging.
    * initial Python 2/3 support.
    * Raise `OSError` when `os.makedirs` is used on an existing path.

v1.0.1
======
    * Raise `IOError` when trying to write a file into a mockfs
      directory that does not exist.
    * Ensure that mockfs does close files that were never opened,
      eg. when exceptions are thrown while saving files.

v1.0.0
======
    * Support `open(path, 'rU')` for opening files.
    * Source tree reorganization.
    * Restored `install` and `uninstall` for the final v1.0 API.

v0.9.0
======
    * Add `os.getcwd` and `os.getcwdu`.
    * Enhance `os.rmdir` and `os.remove` to handle relative paths.
    * Add `os.chdir` and `os.path.abspath`.
    * Add `os.path.getsize`.
    * Add `shutil.rmtree`.
    * Add `os.unlink`
    * Implement `open` and `close` for files by integrating Michael Foord's
      storage.py.
    * New `setup` and `teardown` replacements for `install` and `uinistall`
      (REVERTED).

v0.8.0
======
    * Add `glob.glob`.
    * Add `os.makedirs`.
    * Add `os.rmdir`.
    * Add `os.remove`
    * Raise `OSError` from `os.listdir` on non-existant paths.

v0.6.0
======
    * Initial `glob` module support.
    * `distutils` packaging.

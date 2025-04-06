import os
import sys
import platform
import subprocess
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=""):
        super().__init__(name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

class CMakeBuild(build_ext):
    def run(self):
        # Verify CMake is installed
        try:
            subprocess.check_output(["cmake", "--version"])
        except OSError:
            raise RuntimeError("CMake must be installed to build the following extensions: " +
                               ", ".join(e.name for e in self.extensions))
        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        # The directory where the extension module will be placed
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        # Ensure that extdir ends with a path separator
        extdir = extdir if extdir.endswith(os.sep) else extdir + os.sep

        # Configure the CMake arguments
        cmake_args = [
            f'-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}',
            f'-DPYTHON_EXECUTABLE={sys.executable}',
        ]

        # If on Windows, you might need to adjust the generator
        cfg = 'Debug' if self.debug else 'Release'
        build_args = ['--config', cfg]

        if platform.system() == "Windows":
            cmake_args += [f'-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{cfg.upper()}={extdir}']
            if sys.maxsize > 2**32:
                cmake_args += ['-A', 'x64']
            build_args += ['--', '/m']
        else:
            build_args += ['--', f'-j{os.cpu_count()}']

        # Create the build directory if it doesn't exist
        build_temp = os.path.join(self.build_temp, ext.name)
        os.makedirs(build_temp, exist_ok=True)

        # Run CMake configure
        subprocess.check_call(
            ['cmake', ext.sourcedir] + cmake_args,
            cwd=build_temp
        )
        # Build the extension
        subprocess.check_call(
            ['cmake', '--build', '.'] + build_args,
            cwd=build_temp
        )

setup(
    name="pyinmean",
    version="0.1.0",
    author="Efraim Dahl, Peter van Kranenburg",
    author_email="efraimcdahl@gmail.com",
    description="Python Library for Inner Metric Analysis",
    long_description="Wrappings around IMACPP",
    ext_modules=[CMakeExtension("pyinmean")],
    cmdclass={"build_ext": CMakeBuild},
    zip_safe=False,
)

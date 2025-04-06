# pyinmean

<p align="center">
  <img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/efraimdahl/pyinmean/main.yml?branch=release">
  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/pyinmean">
  <img alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/pyinmean">
</p>

Python - **In**er**Me**tric**An**alysis
Python wrapper for c++ implementation of inner metric weight analysis for symbolic music.

Based on [imacpp](https://github.com/pvankranenburg/imacpp/tree/master) a
C++ library to perform Inner Metric Analysis [1] on a series on onsets. By Peter van Kranenburg and Chris Dyer.


# Usage

Install from PyPI
```bash
pip install pyinmean
```

```python
import pyinmean


#For inner metric weight
print(pyinmean.get_normalized_ima([0,1,4,5,6,7,10,14,20],False))
#For spectral weight 
print(pyinmean.get_normalized_ima([0,1,4,5,6,7,10,14,20],True))

```

# Building From Source
Requires cmake
```bash
git clone https://github.com/efraimdahl/pyinmean/

cd pyinmean

git submodule update --init

mkdir build

cd build

cmake ..

make

cd ..

pip install .
```

[1] Nestke, A. and Noll, T. (2001). Inner Metric Analysis. In Haluska, J. (ed.), Music and Mathematics, pp. 91–111. Bratislava: Tatra Mountains Publications.

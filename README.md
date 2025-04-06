# pyima
Python wrapper for c++ implementation of inner metric weight analysis for symbolic music.

Based on [imacpp](https://github.com/pvankranenburg/imacpp/tree/master) a
C++ library to perform Inner Metric Analysis [1] on a series on onsets. By Peter van Kranenburg and Chris Dyer.


# Usage

```python
import sys
import os
import pyinmean


#For inner metric weight
print(pyinmean.get_normalized_ima([0,1,4,5,6,7,10,14,20],False))
#For spectral weight 
print(pyinmean.get_normalized_ima([0,1,4,5,6,7,10,14,20],True))

```

[1] Nestke, A. and Noll, T. (2001). Inner Metric Analysis. In Haluska, J. (ed.), Music and Mathematics, pp. 91–111. Bratislava: Tatra Mountains Publications.
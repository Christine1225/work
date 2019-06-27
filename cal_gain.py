# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:22:30 2019
imx178 27dB
@author: zhuyu
"""
import math
import numpy as np
for i in np.arange(0.1,27.1, 0.1):
#    print(i/20)
    coe = i/20
#    coe = 1
    v= math.floor (1024 * math.pow(10, coe ))
    print(v)
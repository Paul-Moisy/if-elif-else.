# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 16:50:03 2021

@author: Paul.Moisy
"""
import numpy as np 

data = [1,2,3,4,4.6]

data_mean = np.mean(data)

if data_mean == 3:
    print("good")
    
elif data_mean > 3:
    print("data mean is greater than 3")
    
else: print("data mean is", data_mean," ,this is too low!")



    
    
    
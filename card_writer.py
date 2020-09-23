#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:52:42 2019

@author: Alan
"""

import numpy as np

filename = "tm.inp"
HEADER = '**++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n** V I F S T   T H E R M A L   M A P P I N G\n**++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n**\n*TEMPERATURE'
np.savetxt(filename,MAP, delimiter=',',
                         newline='\n', 
                         header=HEADER, 
                         footer='**\n', 
                         fmt="%i,%8.3f",
                         comments='',
                         encoding=None)
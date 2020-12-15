#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np


df = pd.read_csv('day1.csv', header = None, names=['number'])
df.head()


len(df)


# ## Part 1

get_ipython().run_cell_magic('time', '', 'i = 0\n\nfor i in range(i, len(df)):\n    j = i\n    for j in range(i, len(df)):\n        if df[\'number\'][i] + df[\'number\'][j] == 2020:\n            num1 = df[\'number\'][i]\n            num2 = df[\'number\'][j]\n            print(num1)\n            print(num2)\n            print("multiply result = " + str(num1 * num2))\n            break')


# ## Part 2

get_ipython().run_cell_magic('time', '', 'i = 0\n\nfor i in range(i, len(df)):\n    j = i\n    for j in range(j, len(df)):\n        k = j\n        for k in range(k, len(df)):\n            if df[\'number\'][i] + df[\'number\'][j] + df[\'number\'][k] == 2020:\n                num1 = df[\'number\'][i]\n                num2 = df[\'number\'][j]\n                num3 = df[\'number\'][k]\n                print(num1)\n                print(num2)\n                print(num3)\n                print("multiply result = " + str(num1 * num2 * num3))\n                break')





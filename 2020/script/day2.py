#!/usr/bin/env python
# coding: utf-8

import pandas as pd


df = pd.read_csv('day2.csv', header = None, names=['password'])
df.head()
# df.tail()


len(df)


# ## Part 1

get_ipython().run_cell_magic('time', '', 'i = 0\nvalid_pwd_count = 0\n\nfor i in range(i, len(df)):\n    parts = df[\'password\'][i].split(\' \')\n    numbers = parts[0].split(\'-\')\n    min_value = int(numbers[0])\n    max_value = int(numbers[1])\n    \n    given_letter = parts[1].replace(":","")\n    passwords = parts[2]\n    letter_count = passwords.count(given_letter)\n    \n    if (letter_count >= min_value) and (letter_count <= max_value):\n        valid_pwd_count = valid_pwd_count + 1\n\nprint(valid_pwd_count)')


# ## Part 2

get_ipython().run_cell_magic('time', '', 'i = 0\nvalid_pwd_count = 0\n\nfor i in range(i, len(df)):\n    parts = df[\'password\'][i].split(\' \')\n    numbers = parts[0].split(\'-\')\n    first = int(numbers[0]) - 1\n    second = int(numbers[1]) - 1\n    \n    given_letter = parts[1].replace(":","")\n    passwords = parts[2]\n    \n    if (passwords[first] == given_letter) ^ (passwords[second] == given_letter): # XOR Logic Gate\n        valid_pwd_count = valid_pwd_count + 1\n\nprint(valid_pwd_count)')





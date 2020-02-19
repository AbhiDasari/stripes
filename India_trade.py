# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:34:28 2020

@author: 761317
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
from matplotlib.colors import ListedColormap
import pandas as pd
FIRST = 1960
LAST = 2018
FIRST_REFERENCE = 2000
LAST_REFERENCE = 2005
LIM = 35
data=pd.read_csv("trade_ind.csv")
trade=data[data['Indicator Name']=='Trade (% of GDP)']

def floater(x):
    return float(x)
trade["Value"]=trade["Value"].apply(floater)

def inte(x):
    return int(x)
trade["Year"]=trade["Year"].apply(inte)

cmap = ListedColormap([
    '#08306b', '#08519c', '#2171b5', '#4292c6',
    '#6baed6', '#9ecae1', '#c6dbef', '#deebf7',
    '#fee0d2', '#fcbba1', '#fc9272', '#fb6a4a',
    '#ef3b2c', '#cb181d', '#a50f15', '#67000d',
])
trade=trade.set_index('Year')
trade=trade["Value"]



fig = plt.figure(figsize=(10, 10))

ax = fig.add_axes([0, 0, 1, 1])
ax.set_axis_off()
col = PatchCollection([
    Rectangle((y, 0), 10, 10)
    for y in range(FIRST, LAST + 1)
])

# set data, colormap and color limits
reference=Value.mean()
col.set_array(Value)
col.set_cmap(cmap)
col.set_clim(reference - LIM, reference + LIM)
ax.add_collection(col)


ax.set_ylim(0, 1)
ax.set_xlim(FIRST, LAST + 1)

fig.savefig('trade-stripes.png')

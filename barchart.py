#!/usr/bin/env python
from matplotlib import pyplot as plt, font_manager
import numpy as np
from palettable import colorbrewer

np.random.seed(0)

NAME = "barchart"
ticks_font = font_manager.FontProperties(family='Decima Mono')
plt.style.use(['./ethplot.mplstyle'])

LEFT = -0.035
fig, ax = plt.subplots()
fig.suptitle('A Bar Chart',
             horizontalalignment='left',
             weight='bold', fontsize=20,
             x=LEFT, y=1.078)
fig.text(LEFT, 1.0041, "Scores by group and gender.",
         horizontalalignment='left',
         weight='medium', fontsize=16, color='#555555')

N = 5
menMeans = (20, 35, 30, 35, 27)
menStd =   (2, 3, 4, 1, 2)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

colors = colorbrewer.diverging.RdYlBu_9.mpl_colors
rects1 = ax.bar(ind, menMeans, width, yerr=menStd, color=colors[1], ecolor='#777777')

womenMeans = (25, 32, 34, 20, 25)
womenStd =   (3, 5, 2, 3, 3)
rects2 = ax.bar(ind+width, womenMeans, width, yerr=womenStd, color=colors[-2], ecolor='#777777')

# add some text for labels, title and axes ticks
ax.set_ylabel('Scores', rotation='horizontal', horizontalalignment='left')
ax.yaxis.set_label_coords(LEFT, 1.03)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
ax.xaxis.grid(False)

ax.set_xticks(ind+width)
ax.set_xticklabels(('Group A', 'Group B', 'Group C', 'Group D', 'Group E'), weight='light')
ax.legend( (rects1[0], rects2[0]), ('Men', 'Women'), prop={ 'weight': 'light' }, ncol=2, bbox_to_anchor=(1.02, 1.1))

#plt.setp(ax.get_xticklabels(), fontproperties=ticks_font)
plt.setp(ax.get_yticklabels(), fontproperties=ticks_font)

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        t = ax.text(rect.get_x()+rect.get_width()/2., 1.0, '%d'%int(height),
                ha='center', va='bottom')
        t.set_fontproperties(ticks_font)

autolabel(rects1)
autolabel(rects2)

plt.savefig(NAME + ".png", format='png')

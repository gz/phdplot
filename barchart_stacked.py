from matplotlib import pyplot as plt, font_manager
import numpy as np
from palettable import tableau

ticks_font = font_manager.FontProperties(family='Decima Mono')
plt.style.use(['./ethplot.mplstyle'])

fig, ax = plt.subplots()

N = 4
measA = (1.285, 3.904, 0.957, 1.065)
measB = (0.123, 0.228, 2.525, 3.03)
measC = (1.907, 1.972, 1.969, 1.951)
measD = (1.997, 1.996, 1.975, 1.981)
measE = (6.253, 0.253, 5.253, 4.237)
measF = (0.511, 0.208, 1.579, 1.575)

matrix = []
matrix.append(measA)
matrix.append(measB)
matrix.append(measC)
matrix.append(measD)
matrix.append(measE)
matrix.append(measF)

ind = np.arange(N)  # the x locations for the groups
width = 0.5         # the width of the bars

colors = tableau.TableauLight_10.mpl_colors

rects1 = ax.bar(ind, matrix[0], width, color=colors[0], hatch='/', ec='black')
rects2 = ax.bar(ind, matrix[1], width, bottom=measA ,color=colors[1], hatch='+', ec='black')
rects3 = ax.bar(ind, matrix[2], width, bottom=[measA[i]+measB[i] for i in range(N)] ,color=colors[2], ec='black')
rects4 = ax.bar(ind, matrix[3], width, bottom=[measA[i]+measB[i]+measC[i] for i in range(N)], color=colors[3], hatch='\\', ec='black')
rects5 = ax.bar(ind, matrix[4], width, bottom=[measA[i]+measB[i]+measC[i]+measD[i] for i in range(N)], color=colors[4], hatch='X', ec='black')
rects6 = ax.bar(ind, matrix[5], width, bottom=[measA[i]+measB[i]+measC[i]+measD[i]+measE[i] for i in range(N)], color=colors[5], hatch='|', ec='black')

#ax.set_ylim([0, 18])

ax.set_ylabel('Execution time [s]')
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
ax.xaxis.grid(False)

ax.set_xticks(ind+width/2)
ax.set_xticklabels(('128', '256', '512', '1024'), weight='light')
ax.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0], rects6[0]),
          ('partitioning', 'window allocation', 'sorting', 'merging', 'joining', 'imbalance'),
          prop={ 'weight': 'light' }, ncol=3, bbox_to_anchor=(1.02, 1.15))

plt.setp(ax.get_xticklabels(), fontproperties=ticks_font)
plt.setp(ax.get_yticklabels(), fontproperties=ticks_font)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        t = ax.text(rect.get_x()+rect.get_width()/2., 1.0, '%d'%int(height),
                ha='center', va='bottom')
        t.set_fontproperties(ticks_font)


plt.savefig("barchart_stacked.png", format='png')

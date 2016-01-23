from matplotlib import pyplot as plt, font_manager
import numpy as np

np.random.seed(0)

NAME = "lineplot"
ticks_font = font_manager.FontProperties(family='Decima Mono')
plt.style.use(['./ethplot.mplstyle'])

fig = plt.figure()


fig.suptitle('Key-value System Throughput',
             horizontalalignment='left',
             weight='bold', fontsize=20,
             x=-0.035, y=1.078)
fig.text(-0.035, 1.0041, "While increasing the amount of SET requests.",
         horizontalalignment='left',
         weight='medium', fontsize=16, color='#555555')

ax1 = fig.add_subplot(1, 1, 1)
ax1.set_xlabel('SET rate [%]')
ax1.set_ylabel('Requests / s', rotation
               ='horizontal', horizontalalignment='left')
ax1.yaxis.set_label_coords(-0.035, 1.03)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.get_xaxis().tick_bottom()
ax1.get_yaxis().tick_left()

x = np.linspace(0, 10)

y = np.sin(x) + 0.5 * x + np.random.randn(50)
p = ax1.plot(x, y, label="System A")
ax1.annotate('System A', xy=(x[-5], y[-5]), xytext=(x[-5], y[-5]-2.8), weight='light', color=p[0].get_color())

y = np.sin(x) + x + np.random.randn(50)
p = ax1.plot(x, y, label="System B")
ax1.annotate('System B', xy=(x[-5], y[-5]), xytext=(x[-5], y[-5]+1.6), weight='light', color=p[0].get_color())

y = np.sin(x) + 2 * x + np.random.randn(50)
p = ax1.plot(x, y, label="System C")
ax1.annotate('System C', xy=(x[-5], y[-5]), xytext=(x[-5], y[-5]+1.0), weight='light', color=p[0].get_color())

y = np.sin(x) + 3 * x + np.random.randn(50)
p = ax1.plot(x, y, label="System D")
ax1.annotate('System D', xy=(x[-5], y[-5]), xytext=(x[-5], y[-5]-1.7), weight='light', color=p[0].get_color())

y = np.sin(x) + 4 * x + np.random.randn(50)
p = ax1.plot(x, y, label="System E")
ax1.annotate('System E', xy=(x[-5], y[-5]), xytext=(x[-5], y[-5]-1.3), weight='light', color=p[0].get_color())

for label in ax1.get_xticklabels():
    label.set_fontproperties(ticks_font)

for label in ax1.get_yticklabels():
    label.set_fontproperties(ticks_font)

plt.savefig(NAME + ".png", format='png')
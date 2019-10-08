import os
import sys

import datetime
import numpy as np

import matplotlib.dates as mdates
from matplotlib import pyplot as plt, font_manager

NAME = "timeseries"
ticks_font = font_manager.FontProperties(family='Decima Mono')
plt.style.use([os.path.join(sys.path[0], 'ethplot.mplstyle')])

DATA = [
    (228542030.21088627, datetime.datetime(2019, 10, 1, 21, 6, 56, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))),
    (221542030.21088627, datetime.datetime(2019, 10, 2, 21, 6, 56, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))),
    (224542030.21088627, datetime.datetime(2019, 10, 3, 21, 6, 56, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))),
    (228542030.21088627, datetime.datetime(2019, 10, 4, 21, 6, 56, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))),
    (228542030.21088627, datetime.datetime(2019, 10, 5, 21, 6, 56, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))),
    (208542030.21088627, datetime.datetime(2019, 10, 6, 21, 6, 56, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))),
    (228542030.21088627, datetime.datetime(2019, 10, 7, 21, 6, 56, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))),
    (248542030.21088627, datetime.datetime(2019, 10, 8, 21, 6, 56, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))), 
    (292280856.88659593, datetime.datetime(2019, 10, 8, 22, 11, 5, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200))))]

DATA2 = [
    (8542030.21088627, datetime.datetime(2019, 10, 1, 21, 6, 56, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))),
    (1542030.21088627, datetime.datetime(2019, 10, 2, 21, 6, 56, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))),
    (4542030.21088627, datetime.datetime(2019, 10, 3, 21, 6, 56, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))),
    (8542030.21088627, datetime.datetime(2019, 10, 4, 21, 6, 56, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))),
    (8542030.21088627, datetime.datetime(2019, 10, 5, 21, 6, 56, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))),
    (8542030.21088627, datetime.datetime(2019, 10, 6, 21, 6, 56, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))),
    (8542030.21088627, datetime.datetime(2019, 10, 7, 21, 6, 56, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))),
    (8542030.21088627, datetime.datetime(2019, 10, 8, 21, 6, 56, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))), 
    (2280856.88659593, datetime.datetime(2019, 10, 8, 22, 11, 5, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200))))]


fig = plt.figure()
fig.suptitle('Performance History', weight='bold', fontsize=20)

ax1 = fig.add_subplot(1, 1, 1)
ax1.set_ylabel('Requests / s')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.get_xaxis().tick_bottom()
ax1.get_yaxis().tick_left()

# Only show last 50 elements
DATA = DATA[-50:]
DATA2 = DATA2[-50:]

x = mdates.date2num(list(map(lambda x: x[1], DATA)))
y = list(map(lambda x: x[0], DATA))
ax1.plot_date(x, y, label="Baseline")

x = mdates.date2num(list(map(lambda x: x[1], DATA2)))
y = list(map(lambda x: x[0], DATA2))
ax1.plot_date(x, y, label="NR")
ax1.legend(loc='best')

fig.autofmt_xdate()
plt.setp(ax1.get_xticklabels(), fontproperties=ticks_font)
plt.setp(ax1.get_yticklabels(), fontproperties=ticks_font)

plt.savefig(NAME + ".png", format='png')

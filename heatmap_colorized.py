import numpy as np
import pandas as pd
import matplotlib.cm as cm
from StringIO import StringIO

from matplotlib import pyplot as plt, font_manager
from matplotlib.colors import Normalize, LinearSegmentedColormap

colors = LinearSegmentedColormap.from_list('seismic', ["#2ca25f", "#ffffff", "#ca0020"])

class MidpointNormalize(Normalize):
    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        # I'm ignoring masked values and all kinds of edge cases to make a
        # simple example...
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y))


def heatmap(name, data, title, text):
    fig, ax = plt.subplots()
    ticks_font = font_manager.FontProperties(family='Decima Mono')
    plt.style.use(['ethplot.mplstyle'])
    LEFT = 0.125
    fig.suptitle(title,
             horizontalalignment='left',
             weight='bold', fontsize=20,
             x=LEFT, y=1)
    t = fig.text(LEFT, 0.92, text,
                 horizontalalignment='left',
                 weight='medium', fontsize=16, color='#555555')

    labels1 = ['PR','HD','SSSP','SCC']
    labels2 = ['PR','HD','SSSP','SCC']
    ax.set_xticklabels(labels1)
    ax.set_yticklabels(labels2)
    ax.set_yticks(np.arange(data.shape[0]) + 0.5)
    ax.set_xticks(np.arange(data.shape[1]) + 0.5)

    ax.tick_params(pad=11)

    for label in ax.get_yticklabels():
        label.set_fontproperties(ticks_font)
    for label in ax.get_xticklabels():
        label.set_fontproperties(ticks_font)

    norm = MidpointNormalize(midpoint=1.0)
    c = plt.pcolor(data, cmap = colors, vmin=0.5, vmax=2.5, norm=norm)

    values = data.as_matrix()
    for x in range(data.shape[0]):
        for y in range(data.shape[1]):
            #color = 'white' if values[y][x] > 2.3 else 'black'
            color = 'black'
            plt.text(x + 0.5, y + 0.5, '%.2f' % values[y][x],
                     horizontalalignment='center',
                     verticalalignment='center',
                     color=color,
                     fontproperties=ticks_font)

    colorbar = plt.colorbar(c)
    for label in colorbar.ax.get_yticklabels():
        label.set_fontproperties(ticks_font)

    plt.savefig(name + ".png", format='png')
    #ppad_inched=0.08 here because otherwise it cuts off the numbers...
    #plt.savefig(name + ".pdf", format='pdf', pad_inches=0.08)

def main():
    title = "A Heatmap"
    text = "Normalized slowdown for a pair of operators."

    NAME = "heatmap_colorized"
    csv = StringIO("""PR,HD,SSSP,SCC
PR,1.52,1.21,1.16,0.85
HD,2.10,1.40,0.80,1.86
SSSP,2.50,0.71,2.00,0.76
SCC,2.52,1.27,1.70,0.62""")

    data = pd.read_csv(csv, index_col=0)
    heatmap(NAME, data, title, text)

if __name__ == "__main__":
    main()

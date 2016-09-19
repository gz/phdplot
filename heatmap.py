import matplotlib.cm as cm
from matplotlib import pyplot as plt, font_manager
import numpy as np
import pandas as pd
from StringIO import StringIO


def heatmap(name, data, title, text):
    fig, ax = plt.subplots()
    ticks_font = font_manager.FontProperties(family='Decima Mono')
    plt.style.use([os.path.join(sys.path[0], 'ethplot.mplstyle')])
    #savefig.pad_inches: 0.08

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

    plt.setp(ax.get_xticklabels(), fontproperties=ticks_font)
    plt.setp(ax.get_yticklabels(), fontproperties=ticks_font)

    c = plt.pcolor(data, cmap = cm.Greys, vmin=1.0, vmax=2.5)

    values = data.as_matrix()
    for x in range(data.shape[0]):
        for y in range(data.shape[1]):
            color = 'white' if values[y][x] > 2.3 else 'black'
            plt.text(x + 0.5, y + 0.5, '%.2f' % values[y][x],
                     horizontalalignment='center',
                     verticalalignment='center',
                     color=color,
                     fontproperties=ticks_font)

    colorbar = plt.colorbar(c)
    plt.setp(colorbar.ax.get_yticklabels(), fontproperties=ticks_font)

    plt.savefig(name + ".png", format='png')
    #ppad_inched=0.08 here because otherwise it cuts off the numbers...
    #plt.savefig(name + ".pdf", format='pdf', pad_inches=0.08)

def main():
    title = "A Heatmap"
    text = "Normalized slowdown for a pair of operators."
    NAME = "heatmap"

    csv = StringIO("""PR,HD,SSSP,SCC
PR,1.52,1.21,1.16,0.85
HD,2.10,1.40,0.80,1.86
SSSP,2.50,0.71,2.00,0.76
SCC,2.52,1.27,1.70,0.62""")

    data = pd.read_csv(csv, index_col=0)
    heatmap(NAME, data, title, text)


if __name__ == "__main__":
    main()

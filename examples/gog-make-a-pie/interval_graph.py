import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def plot_interval_graph(si, imagePath=None):
    fig = plt.figure(figsize=(6, 2))
    axes = fig.add_subplot(111)
    axes.set_xlim(0.0, 1.0)
    axes.set_ylim(0.0, 1.0)

    axes.get_xaxis().get_major_formatter().set_useOffset(False)
    axes.get_yaxis().get_major_formatter().set_useOffset(False)

    axes.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
    axes.xaxis.set_minor_locator(ticker.MultipleLocator(0.05))

    axes.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
    vline = plt.Line2D((0, si[0]), (0.95, 0.95), antialiased=True, lw=8, c='k')
    axes.add_line(vline)
    vline = plt.Line2D((si[0], si[1]), (0.75, 0.75), antialiased=True, lw=8, c='k')
    axes.add_line(vline)
    vline = plt.Line2D((si[1], si[2]), (0.55, 0.55), antialiased=True, lw=8, c='k')
    axes.add_line(vline)
    vline = plt.Line2D((si[2], si[3]), (0.35, 0.35), antialiased=True, lw=8, c='k')
    axes.add_line(vline)
    vline = plt.Line2D((si[3], si[4]), (0.15, 0.15), antialiased=True, lw=8, c='k')
    axes.add_line(vline)

    if imagePath:
        plt.savefig(imagePath, bbox_inches='tight', dpi=72, transparent=False)
    else:
        plt.show()


def runTest():
    msummary = [0.30, 0.15, 0.10, 0.07, 0.38]
    wsummary = [0.08, 0.11, 0.17, 0.32, 0.32]

    # compute the cumulative sum of these numbers
    msi = np.cumsum(msummary)
    wsi = np.cumsum(wsummary)

    plot_interval_graph(msi, "men.png")
    plot_interval_graph(wsi, "women.png")


runTest()

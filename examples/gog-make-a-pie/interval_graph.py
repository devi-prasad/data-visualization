import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def setup_figure_plot_env(title):
    fig = plt.figure(figsize=(6, 2), dpi=60, facecolor='white')
    fig.canvas.set_window_title(title)
    axes = fig.add_subplot(111, axisbg=(1, 1, 1))
    axes.set_axis_bgcolor('white')
    axes.grid(True, which='both') # False - to not draw the grid lines.
    axes.set_xlim(0.0, 1.0)
    axes.set_ylim(0.0, 0.7)
    axes.axis('on') # 'off' - to hide the axes
    #
    axes.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
    axes.xaxis.set_minor_locator(ticker.MultipleLocator(0.05))
    axes.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
    axes.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
    #
    mpl.rc('lines', linewidth = 4, color = 'k', antialiased=False)
    #


def show_or_save_plot(imagePath=None):
    if imagePath:
        plt.savefig(imagePath, bbox_inches='tight', dpi=90, transparent=False)
    else:
        plt.show()


###
# The summary data is mapped to x-axis of the Cartesian coordinate system.
# Neither data not the axis is scaled in any manner.
###
def draw_interval_graph(si):
    axes = plt.gca()
    hline = plt.Line2D((0, si[0]), (0.65, 0.65))
    axes.add_line(hline)
    hline = plt.Line2D((si[0], si[1]), (0.5, 0.5))
    axes.add_line(hline)
    hline = plt.Line2D((si[1], si[2]), (0.35, 0.35))
    axes.add_line(hline)
    hline = plt.Line2D((si[2], si[3]), (0.2, 0.2))
    axes.add_line(hline)
    hline = plt.Line2D((si[3], si[4]), (0.05, 0.05))
    axes.add_line(hline)


def plot_interval_graph(msi, title, imagePath):
    setup_figure_plot_env(title)
    draw_interval_graph(msi)
    show_or_save_plot(imagePath)


def transform_summary_data(summary):
    return np.cumsum(summary)


def plot_summary_interval_graph():
    msummary = [0.30, 0.15, 0.10, 0.07, 0.38]
    wsummary = [0.08, 0.11, 0.17, 0.32, 0.32]

    # compute the cumulative sum of these numbers
    msi = transform_summary_data(msummary)
    wsi = transform_summary_data(wsummary)

    ### view the plot on the screen
    #plot_interval_graph(msi, "Summary - Men", None)

    ### save the plot as an image
    plot_interval_graph(msi, "Summary - Men", "men.png")

    ### view the plot on the screen
    #plot_interval_graph(wsi, "Summary - Women", None)

    ### save the plot as an image
    plot_interval_graph(wsi, "Summary - Women", "women.png")


plot_summary_interval_graph()


from __futures__ import division
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.ticker as ticker

# An empty figure with no Axes. Default window title.
def draw_empty_figure(plt):
  plt.figure()
  plt.show()


# An empty figure with no Axes. A Window title.
def draw_empty_figure_with_canvas_title(plt):
  fig = plt.figure()
  fig.canvas.set_window_title('Matplotlib Experiments')
  plt.show()


# This is merely a shortcut to work with 'plt.figure()' instance.
def draw_empty_figure_with_canvas_title(plt):
  plt.title('Matplotlib Experiments')
  plt.show()


# Two empty figures with no Axes. Separate windows and titles.
def draw_empty_figures_with_canvas_titles(plt):
  fig1 = plt.figure()
  fig2 = plt.figure()
  fig1.canvas.set_window_title("A Visual Window")
  fig2.canvas.set_window_title("Another Visual Window")
  plt.show()


# Displays an Axes with default ticks and ticklabels.
# X and Y axes are marked with (0, 0.2, 0.4, 0.6, 0.8, 1.0) ticklabels.
def draw_plain_axes(plt):
  fig = plt.figure()
  fig.canvas.set_window_title('Matplotlib Experiments')
  axes = fig.add_subplot(111)
  fig.show()

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Two different ways to achive the same goal.
## Draw an empty plot with a grid
## The second method gives access to intermediate objects.

def draw_uniform_axes_grid(plt):
  plt.xlim(-12, 12)
  plt.ylim(0, 12)
  plt.grid(True, which='both')
  plt.show()


##
## check the difference: 'set_xlim' and 'set_ylim' are operations on axes.
##
def draw_uniform_figure_axes_grid(plt):
  fig = plt.figure()
  fig.canvas.set_window_title('Matplotlib Experiments')
  axes = fig.add_subplot(111)
  axes.set_xlim(0, 12)
  axes.set_ylim(0, 12)
  axes.grid(True, which='both')
  plt.show()

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Displays an Axes with a title, and default ticks and ticklabels.
# X and Y axes are marked with (0, 0.2, 0.4, 0.6, 0.8, 1.0) ticklabels.
# Axes has a dull green background
def draw_axes_with_title(plt):
  fig = plt.figure()
  fig.canvas.set_window_title('Matplotlib Experiments')
  axes = fig.add_subplot(111, axisbg=(0, 0.6, 0, 0.1))
  axes.set_title("A Simple Axes")
  fig.show()

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Displays an Axes with a title, and default ticks and ticklabels.
# Plots a diagonal line.
# We set the range of ticklabels on the X and Y axes.
# X and Y axes are marked with (0, 2, 4, 6, 8, 10, 12, 14) ticklabels.
def draw_straight_line_on_configured_axes(plt):
  fig = plt.figure()
  fig.canvas.set_window_title('Matplotlib Experiments')
  #
  axes = fig.add_subplot(111)
  axes.set_title("A Simple Axes")
  axes.set_xlim(0, 14)
  axes.set_ylim(0, 12)
  axes.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
  #
  plt.show()


def draw_straight_line_on_configured_axes(plt):
  plt.gcf().canvas.set_window_title('Matplotlib Experiments')
  plt.title("A Simple Axes")
  plt.xlim(0, 14)
  plt.ylim(0, 12)
  plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
  plt.show()

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Dsiplays an axes with bottom spline color and bottom ticks in red.
# Also sets the xaxis label color as red
def draw_straight_line_on_red_xaxis(plt):
  import matplotlib.pyplot as plt
  #
  fig = plt.figure()
  fig.canvas.set_window_title('Matplotlib Experiments')
  ax = fig.add_subplot(111)
  #
  ax.plot(range(10))
  ax.set_xlabel('X-axis')
  ax.set_ylabel('Y-axis')
  #
  ax.spines['bottom'].set_color('red')
  ax.spines['top'].set_color('red')
  ax.xaxis.label.set_color('red')
  ax.tick_params(axis='x', colors='red')
  #
  plt.show()



def draw_damped_undampled_oscillations(np, plt):
  X1 = np.linspace(0.0, 5.0)
  X2 = np.linspace(0.0, 2.0)
  #
  Y1 = np.cos(2 * np.pi * X1) * np.exp(-X1)
  Y2 = np.cos(2 * np.pi * X2)
  #
  axes = plt.subplot(211)
  axes.plot(X1, Y1, 'yo-')
  axes.set_ylabel('Damped oscillation')
  #
  axes = plt.subplot(212)
  axes.plot(X2, Y2, 'r.-', color='b')
  axes.set_xlabel('time (s)')
  axes.set_ylabel('Undamped')
  #
  axes.figure.canvas.set_window_title('A Plot of Two Oscillations')
  plt.show()


# Two independent figures with independent Axes.
# In the plot of a cubic curve, 
#   X axis = (0, 2, 4, 6, 8, 10) and Y axis = (0, 200, 400, 600, 800, 1000)
def draw_independent_axes_plots(plt):
  fig1 = plt.figure()
  fig2 = plt.figure()
  fig1.canvas.set_window_title("Visualization 1")
  fig2.canvas.set_window_title("Visualization 2")
  f1axes = fig1.add_subplot(111)
  f1axes.set_title("A Straight Line")
  f2axes = fig2.add_subplot(111)
  f2axes.set_title("A Cubic Curve")
  f1axes.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
  f2axes.plot([0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000])
  plt.show()


# Plot a sine curve.
def draw_sine(plt):
  fig = plt.figure()
  fig.canvas.set_window_title('Matplotlib Experiments')
  axes = fig.add_subplot(111)
  axes.set_title("Sine Graph")
  x = np.arange(0, 10., 0.0125)
  y = np.sin(x)
  axes.plot(x, y)
  plt.show()


# Plot sine and cosine curves on the same axes. Two different ranges.
def draw_sin_cosine(plt, np):
  X = np.linspace(0, 2 * np.pi, 200)
  Ya = np.sin(X)
  Yb = np.cos(X)
  plt.plot(X, Ya)
  plt.plot(X, Yb)
  plt.show()


# Render the sine curve to a PDF file.
def render_pdf_sine_curve(plt, np):
  fig = plt.figure()
  fig.canvas.set_window_title('Matplotlib Experiments')
  axes = fig.add_subplot(111)
  axes.set_title("Sine Graph")
  X = np.linspace(0, 2 * np.pi, 200)
  Y = np.sin(X)
  axes.plot(X, Y)
  plt.savefig("sine.pdf", format="pdf")



# draw sine wave with thick black line and cosine with blue dashed line.
# notice the use of RGBA style while drawing dashed (cosine) lines 
def draw_graphs_with_aesthetics(plt, np):
  fig = plt.figure()
  fig.canvas.set_window_title('Matplotlib Experiments')
  axes = fig.add_subplot(111)
  axes.set_title("Sine and Cosine in Style")
  axes.xlabel('X')
  axes.ylabel('Y')
  ##
  X = np.linspace(0, 6, 1024)
  Y1 = np.sin(X)
  Y2 = np.cos(X)
  axes.plot(X, Y1, c = 'k',  lw = 1.25, label = 'sin(X)')
  axes.plot(X, Y2, c = (0, 0, 1, 0.3), lw = 2.5, ls = '--', label = 'cos(X)')
  axes.legend('left')
  axes.axis('scaled')
  fig.show()


# drawing patches - a circle and a rectangle at specified locations.
# Check what happens if you DO NOT use 'scaled' axis
def draw_cirle_rectngle(plt, patches):
  shape = patches.Circle((8, 8), radius = 2., color = (0, 1, 0, 0.75))
  plt.gca().add_patch(shape)
  shape = patches.Rectangle((0, 0), width=1, height=4, color = 'k', alpha=0.6)
  plt.gca().add_patch(shape)
  plt.grid(True)
  plt.axis('scaled')
  plt.show()


# controlling the axis ticks to be spaced at 1 units.
# grid is drawn on minor ticks on Y axis too.
def draw_shapes_on_grid_plot(plt, ticker, patches):
  ax = plt.axes()
  ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
  ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
  ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
  #
  shape = patches.Circle((8, 8), radius = 2, color='y')
  ax.add_patch(shape)
  shape = patches.Rectangle((0, 0), width=1, height=4, color='0.6')
  ax.add_patch(shape)
  #
  ax.plot([5, 6, 7, 8, 9, 10, 11, 12], color='k', lw=2)
  #
  plt.grid(True, which='both')
  plt.axis('scaled')
  plt.show()



# This draws a vertial line, and a circle to its right.
# It is important to scale the axis so figures do not appear distorted.
def draw_vline_right_circle(plt, ticker, patches):
  axes = plt.axes()
  #
  axes.xaxis.set_major_locator(ticker.MultipleLocator(1))
  axes.yaxis.set_major_locator(ticker.MultipleLocator(2))
  axes.yaxis.set_minor_locator(ticker.MultipleLocator(1))
  #
  vline = plt.Line2D((5, 5), (0, 12), lw=3, c='b')
  axes.add_line(vline)
  #
  shape = patches.Circle((8, 8), radius = 2, color='y')
  axes.add_patch(shape)
  #
  axes.axis('scaled')
  plt.grid(True, which='both')
  plt.show()


def draw_vertical_line_and_filled_circle(plt, ticker, patches):
  axes = plt.axes()
  axes.axis('scaled')  # or equivalently, plt.axis('scaled')
  #
  axes.set_xlim(0, 12)
  axes.set_ylim(0, 12)
  #
  axes.xaxis.set_major_locator(ticker.MultipleLocator(1))
  axes.yaxis.set_major_locator(ticker.MultipleLocator(2))
  axes.yaxis.set_minor_locator(ticker.MultipleLocator(1))
  #
  vline = plt.Line2D((5, 5), (0, 12), lw=3, c='b')
  axes.add_line(vline)
  #
  shape = patches.Circle((8, 8), radius = 2, color='y')
  axes.add_patch(shape)
  #
  plt.grid(True, which='both')
  plt.show()



()
# draws a triangle in a grid

def draw_fine_grid(plt, ticker):
  plt.grid(True, which='both')
  axes = plt.axes()
  axes.xaxis.set_major_locator(ticker.MultipleLocator(1))
  axes.xaxis.set_minor_locator(ticker.MultipleLocator(1))
  axes.yaxis.set_major_locator(ticker.MultipleLocator(1))
  axes.yaxis.set_minor_locator(ticker.MultipleLocator(1))


def draw_grid_on_axes(axes, xmajor, xminor, ymajor, yminor, plt, ticker):
  plt.grid(True, which='both')
  axes.xaxis.set_major_locator(ticker.MultipleLocator(xmajor))
  axes.xaxis.set_minor_locator(ticker.MultipleLocator(xminor))
  axes.yaxis.set_major_locator(ticker.MultipleLocator(ymajor))
  axes.yaxis.set_minor_locator(ticker.MultipleLocator(yminor))


def draw_triangle(plt, ticker):
  plt.xlim(0, 12)
  plt.ylim(0, 10)
  draw_fine_grid(plt, ticker)
  verts = [[2, 1], [10, 1], [10, 8]]
  triangle = plt.Polygon(verts, fill=True, facecolor='m', edgecolor=None)
  plt.gca().add_patch(triangle)
  plt.show() 



def draw_regular_hexagon(plt, ticker):
  plt.axis('scaled')
  plt.xlim(0, 12)
  plt.ylim(0, 10)
  draw_fine_grid(plt, ticker)
  hexagon = patches.RegularPolygon(
    (5, 5),          # (x,y)
    6,               # number of vertices
    3,               # radius
    facecolor='y',
    fill=True)
  plt.gca().add_patch(hexagon)
  plt.show()



# Render sin and cos graphs on subplots.
def draw_sincos_subplots():
  fig = plt.figure()
  fig.canvas.set_window_title('Matplotlib Experiments')
  axes211 = fig.add_subplot(211)
  axes211.set_title("Sine Graph")
  axes212 = fig.add_subplot(212)
  axes212.set_title("Cosine Graph")
  X = np.linspace(0, 2 * np.pi, 200)
  sinY = np.sin(X)
  axes211.plot(X, sinY)
  cosY = np.cos(X)
  axes212.plot(X, cosY)
  plt.show()


# Render sin and cos graphs on subplots with fine grids.
def draw_sincos_grid_subplots():
  fig = plt.figure(figsize=(14,6), tight_layout=True)
  fig.canvas.set_window_title('Matplotlib Experiments')
  axes221 = fig.add_subplot(221)
  draw_grid_on_axes(axes221, 0.5, 0.25, 0.5, 0.25, plt, ticker)
  axes221.set_title("Sine Graph")
  axes224 = fig.add_subplot(224)
  draw_grid_on_axes(axes224, 0.5, 0.25, 0.5, 0.25, plt, ticker)
  axes224.set_title("Cosine Graph")
  X = np.linspace(0, 2 * np.pi, 200)
  sinY = np.sin(X)
  axes221.plot(X, sinY)
  cosY = np.cos(X)
  axes224.plot(X, cosY)
  plt.savefig("sincos.pdf", format="pdf")
  plt.show()



+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def arc_patch(axes, patches, center, radius, theta1, theta2, resolution=50, 
              **kwargs):
  # make sure axes is not empty
  if axes is None: ax = plt.gca()
  # generate the points
  theta = np.linspace(np.radians(theta1), np.radians(theta2), resolution)
  points = np.vstack((radius*np.cos(theta) + center[0], 
                      radius*np.sin(theta) + center[1]))
  # build the polygon and add it to the axes
  poly = patches.Polygon(points.T, closed=True, **kwargs)
  axes.add_patch(poly)
  return poly


def draw_filled_arc(plt):
  axes = plt.subplot()
  ##
  arc_patch(axes, patches, (0., 0.3), 0.25, 90, 180, fill=True, color='blue')
  #axes.set_title('Arc')
  axes.set_aspect('equal')
  axes.set_xlim(-1.25, 0.2)
  axes.set_ylim(0., 1.5)
  ##
  plt.axis('off')
  # plt.axis('tight')
  #
  plt.savefig("arc.png", bbox_inches='tight')
  plt.axis('on')
  plt.show()


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## spines with explicit ticks and stuff
def draw_spines(plt):
  fig = plt.figure(figsize=(9, 6), dpi=80)
  axes = fig.add_subplot(111)
  axes.spines['right'].set_color('none')
  axes.spines['top'].set_color('none')
  axes.spines['right'].set_visible(False)
  axes.spines['top'].set_visible(False)
  axes.xaxis.set_ticks_position('bottom')
  axes.spines['bottom'].set_position(('data', 0))
  axes.yaxis.set_ticks_position('left')
  axes.spines['left'].set_position(('data', 0.5))
  #
  axes.set_xlim(-1.8, 1.8)
  axes.set_ylim(-1.8, 1.8)
  plt.xticks([-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5],
             [r'-1.5', r'-1.0', r'-0.5', r'0', r'0.5', r'1.0', r'1.5'])
  plt.yticks([-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5],
             [r'-1.5', r'-1.0', r'-0.5', r'0', r'0.5', r'1.0', r'1.5'])
  plt.show()


def draw_sine_cosine_on_spines(np, plt):
  fig = plt.figure(figsize=(8,5), dpi=90)
  axes = fig.add_subplot(111)
  ##
  axes.spines['right'].set_color('none')
  axes.spines['top'].set_color('none')
  axes.xaxis.set_ticks_position('bottom')
  axes.spines['bottom'].set_position(('data',0))
  axes.yaxis.set_ticks_position('left')
  axes.spines['left'].set_position(('data',0))
  ##
  X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
  S, C = np.sin(X), np.cos(X)
  ##
  axes.plot(X, S, color="blue", linewidth=2, linestyle="-")
  axes.plot(X, C, color="magenta", linewidth=2, linestyle="-")
  ##
  axes.set_xlim(X.min() * 1.2, X.max() * 1.2)
  plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
             [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
  ##
  axes.set_ylim(C.min()*1.1,C.max()*1.1)
  plt.yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])
  axes.plot()
  plt.show()

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np
from fast_histogram import histogram2d

def density_scatter_plot(X, Y, n_bins = 100, colormap = 'plasma', ax = None):
    if ax is None :
        fig , ax = plt.subplots()
    else:
        fig = ax.get_figure()

    cmap = plt.get_cmap(colormap)
    bounds = [[np.nanmin(X), np.nanmax(X)], [np.nanmin(Y), np.nanmax(Y)]]
    h = histogram2d(X, Y, range=bounds, bins=n_bins)
    h = np.rot90(h)
    density = ax.imshow(h, extent=[bounds[0][0],bounds[0][1],bounds[1][0],bounds[1][1]], aspect='auto',\
               norm=colors.LogNorm(vmin=1, vmax=h.max()), cmap=cmap, interpolation = 'none')
    fig.colorbar(density, label='Number of points per pixel')
    return fig, ax

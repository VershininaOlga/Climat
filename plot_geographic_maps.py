import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

def plot_map_area(ax, coordinates, detailing = False):
    ax.set_extent(coordinates)
    
    if detailing == True:
        ax.stock_img()   # downsampled version of the Natural Earth shaded relief raster
        
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, alpha = 0.5)
    ax.add_feature(cfeature.LAKES, alpha = 0.5)
    ax.add_feature(cfeature.RIVERS)
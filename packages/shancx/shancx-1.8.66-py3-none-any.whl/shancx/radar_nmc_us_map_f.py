import matplotlib.pyplot as plt
import numpy as np
import datetime
from hjnwtx.colormap import cmp_hjnwtx  # Assuming this is your custom colormap library
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import os
from shancx import crDir

def drawUS(array_dt,ty="CR"):
    # env = [-119, -64, 22, 50]
    env = [-132.0, -47.0, 0, 57.0]
    now_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    outpath = f"./radar_nmc/US_{now_str}.png"
    crDir(outpath)

    # Create figure and set the coordinate system
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    # Set the extent for the United States
    ax.set_extent(env, ccrs.PlateCarree())  # Adjust as needed

    # Add the US map boundaries and features
    add_us_map(ax)
    
    # Add data layers
    if len(array_dt.shape) == 3:
        for i, img_ch_nel in enumerate(array_dt):
            ax.imshow(img_ch_nel, vmin=50, vmax=500, cmap=cmp_hjnwtx["radar_nmc"], transform=ccrs.PlateCarree(), extent=env)
            plt.colorbar(ax.images[0], ax=ax, orientation='vertical')
            plt.savefig(f"{outpath}_layer_{i}.png")
            plt.clf()  # Clear the figure to draw the next channel image
    elif len(array_dt.shape) == 2 and ty =="pre":
        # ax.imshow(array_dt, vmin=0, vmax=100, cmap=cmp_hjnwtx["radar_nmc"], transform=ccrs.PlateCarree(), extent=env)   #pre_tqw
        ax.imshow(array_dt, vmin=0, vmax=10, cmap=cmp_hjnwtx["pre_tqw"], transform=ccrs.PlateCarree(), extent=env)   #pre_tqw
        plt.colorbar(ax.images[0], ax=ax, orientation='vertical')
        plt.savefig(outpath)
    else :
        ax.imshow(array_dt, vmin=0, vmax=72, cmap=cmp_hjnwtx["radar_nmc"], transform=ccrs.PlateCarree(), extent=env)
        # ax.imshow(array_dt, vmin=0, vmax=10, cmap=cmp_hjnwtx["pre_tqw"], transform=ccrs.PlateCarree(), extent=[-119, -64, 22, 50])   #pre_tqw
        plt.colorbar(ax.images[0], ax=ax, orientation='vertical')
        plt.savefig(outpath)

    plt.close(fig)

def add_us_map(ax):
    # Add geographic features for the US
    ax.add_feature(cfeature.COASTLINE, edgecolor='gray')
    ax.add_feature(cfeature.BORDERS, linestyle=':', edgecolor='gray')
    ax.add_feature(cfeature.LAKES, alpha=0.8)
    
    # Adding state boundaries
    if os.path.exists('/home/scx/ne_10m_admin_1_states_provinces.shp'):
        states = '/home/scx/ne_10m_admin_1_states_provinces.shp'
    else:
        states = shpreader.natural_earth(resolution='10m', category='cultural', name='admin_1_states_provinces')  # Automatically download 

    states_features = shpreader.Reader(states).geometries()
    
    ax.add_geometries(states_features, ccrs.PlateCarree(), facecolor='none', edgecolor='gray', linestyle=':', linewidth=0.5, alpha=0.8)

# Example usage
# Assuming array_dt is your data array, pass it to drawUS
# array_dt = np.random.rand(3, 100, 100)  # Example random data; replace with your actual data
# drawUS(array_dt)

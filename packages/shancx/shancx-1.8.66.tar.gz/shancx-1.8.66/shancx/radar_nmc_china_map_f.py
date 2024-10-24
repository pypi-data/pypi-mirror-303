import matplotlib.pyplot as plt
import numpy as np
import datetime
from hjnwtx.colormap import cmp_hjnwtx  # 假设这是您的自定义颜色映射库
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import os
from shancx import crDir

def drawCN(array_dt,ty="CR"):
    env = [73, 135, 18, 54]   #US  [-119, -64, 22, 50]
    now_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    outpath = f"./radar_nmc/CN_{now_str}.png"
    crDir(outpath)

    # 创建绘图和设置坐标系
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    # 设置图像显示的范围
    ax.set_extent(env, ccrs.PlateCarree())  # 根据需要调整    [-119, -64, 22, 50]

    # 添加中国地图的边界和特征，包括省份轮廓
    add_china_map(ax)
    
    # 添加数据层
    if len(array_dt.shape) == 3:
        for i, img_ch_nel in enumerate(array_dt):
            ax.imshow(img_ch_nel, vmin=50, vmax=500, cmap=cmp_hjnwtx["radar_nmc"], transform=ccrs.PlateCarree(), extent=env)
            plt.colorbar(ax.images[0], ax=ax, orientation='vertical')
            plt.savefig(f"{outpath}_layer_{i}.png")
            plt.clf()  # 清除图形以绘制下一个通道图像
    elif len(array_dt.shape) == 2 and ty=="pre":
        # ax.imshow(array_dt, vmin=0, vmax=100, cmap=cmp_hjnwtx["radar_nmc"], transform=ccrs.PlateCarree(), extent=env)
        ax.imshow(array_dt, vmin=0, vmax=10, cmap=cmp_hjnwtx["pre_tqw"], transform=ccrs.PlateCarree(), extent=[-119, -64, 22, 50])   #pre_tqw
        plt.colorbar(ax.images[0], ax=ax, orientation='vertical')
        plt.savefig(outpath)
    else :
        ax.imshow(array_dt, vmin=0, vmax=72, cmap=cmp_hjnwtx["radar_nmc"], transform=ccrs.PlateCarree(), extent=env)
        # ax.imshow(array_dt, vmin=0, vmax=10, cmap=cmp_hjnwtx["pre_tqw"], transform=ccrs.PlateCarree(), extent=[-119, -64, 22, 50])   #pre_tqw
        plt.colorbar(ax.images[0], ax=ax, orientation='vertical')
        plt.savefig(outpath)
    plt.close(fig)

def add_china_map(ax):
    # 在地图上添加地形特征
    ax.add_feature(cfeature.COASTLINE, edgecolor='gray')
    ax.add_feature(cfeature.BORDERS, linestyle=':', edgecolor='gray')
    ax.add_feature(cfeature.LAKES, alpha=0.8)
    # 添加省份轮廓
    if os.path.exists('/home/scx/ne_10m_admin_1_states_provinces.shp'):
        provinces = '/home/scx/ne_10m_admin_1_states_provinces.shp'
    else :
        provinces = shpreader.natural_earth(resolution='10m', category='cultural', name='admin_1_states_provinces')   ###自动下载 
    provinces_features = shpreader.Reader(provinces).geometries()
    """
    本地路径读取 #'/home/scx/.local/share/cartopy/shapefiles/natural_earth/cultural/ne_10m_admin_1_states_provinces.shp'   #ne_10m_admin_1_states_provinces.shx 
    # shapefile_path = '/home/scx/.local/share/cartopy/shapefiles/natural_earth/cultural/admin_1_states_provinces.shp'
    # provinces_features = shpreader.Reader(shapefile_path).geometries()
    """
    ax.add_geometries(provinces_features, ccrs.PlateCarree(), facecolor='none', edgecolor='gray', linestyle=':', linewidth=0.5, alpha=0.8)

 
# 示例用法



import matplotlib.pyplot as plt
import numpy as np
import datetime
from hjnwtx.colormap import cmp_hjnwtx  # 假设这是您的自定义颜色映射库
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
from shancx import crDir
import os

def drawCNXY(array_dt,XY = [3,2]):  #x_coords2,y_coords2
    now_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    outpath = f"./radar_nmc/{now_str}.png"
    crDir(outpath)

    # 创建绘图和设置坐标系
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    
    # 设置图像显示的范围
    ax.set_extent([73, 135, 18, 54], ccrs.PlateCarree())  # 根据需要调整

    # 添加中国地图的边界和特征，包括省份轮廓
    add_china_map(ax)    
    # 添加数据层
    if len(array_dt.shape) == 3:
        for i, img_ch_nel in enumerate(array_dt):
            ax.imshow(img_ch_nel, vmin=50, vmax=500, cmap=cmp_hjnwtx["radar_nmc"], transform=ccrs.PlateCarree(), extent=[73, 134.99, 12.21, 54.2])
            plt.colorbar(ax.images[0], ax=ax, orientation='vertical')
            plt.savefig(f"{outpath}_layer_{i}.png")
            plt.clf()  # 清除图形以绘制下一个通道图像
    elif len(array_dt.shape) == 2:
        ax.imshow(array_dt, vmin=0, vmax=10, cmap=cmp_hjnwtx["pre_tqw"], transform=ccrs.PlateCarree(), extent=[73, 134.99, 12.21, 54.2])
        x_coords2 = XY[0]
        y_coords2 = XY[1]
        plt.plot(list(x_coords2), list(y_coords2), 'ro', markersize=1)
        plt.colorbar(ax.images[0], ax=ax, orientation='vertical')
        plt.savefig(outpath)
    plt.close(fig)

def add_china_map(ax):
    # 在地图上添加地形特征
    ax.add_feature(cfeature.COASTLINE, edgecolor='gray')
    ax.add_feature(cfeature.BORDERS, linestyle=':', edgecolor='gray')
    ax.add_feature(cfeature.LAKES, alpha=0.8)
    # 添加省份轮廓
    if os.path.exists('/home/scx/ne_10m_admin_1_states_provinces.shp'):
        provinces = '/home/scx/ne_10m_admin_1_states_provinces.shp'
    else :
        provinces = shpreader.natural_earth(resolution='10m', category='cultural', name='admin_1_states_provinces')   ###自动下载 
    provinces_features = shpreader.Reader(provinces).geometries()
    """
    本地路径读取 #'/home/scx/.local/share/cartopy/shapefiles/natural_earth/cultural/ne_10m_admin_1_states_provinces.shp'   #ne_10m_admin_1_states_provinces.shx 
    # shapefile_path = '/home/scx/.local/share/cartopy/shapefiles/natural_earth/cultural/admin_1_states_provinces.shp'
    # provinces_features = shpreader.Reader(shapefile_path).geometries()
    """
    ax.add_geometries(provinces_features, ccrs.PlateCarree(), facecolor='none', edgecolor='gray', linestyle=':', linewidth=0.5, alpha=0.8)
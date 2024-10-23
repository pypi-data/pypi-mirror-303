import pygrib
import numpy as np
import rasterio
import netCDF4 as nc
# grib2 to npy
def grib22npy(grib2_path, save=False, npy_path=None):
    """
    将grib2文件转为npy文件
    :param save:
    :param grib2_path: grib2文件路径
    :param npy_path: npy文件路径
    :return:
    """
    grbs = pygrib.open(grib2_path)
    data = []
    for grb in grbs:
        data.append(grb.values)
    n = np.array(data)
    if save:
        np.save(npy_path, n)
    return n


def tif2npy(tif_path, save=False, npy_path=None):
    """
    将tif文件转为npy文件
    :param save:
    :param tif_path: tif文件路径
    :param npy_path: npy文件路径
    :return:
    """
    with rasterio.open(tif_path) as src:
        data = src.read()
    if save:
        np.save(npy_path, data)
    return data

# def nc2npy(nc_path, save=False, npy_path=None):
#     """
#     将nc文件转为npy文件
#     :param save:
#     :param nc_path: nc文件路径
#     :param npy_path: npy文件路径
#     :return:
#     """
#     if type(nc_path) == str:
#         nc_data = nc.Dataset(nc_path)
#     else:
#         nc_data = nc_path
#     with raster


if __name__ == '__main__':
    npy = grib22npy('temp/202202/ART_ATM_GLB_0P10_6HOR_ANAL_2022020100_20240603001655_HGT.grib2', './temp/test.npy')
    print()

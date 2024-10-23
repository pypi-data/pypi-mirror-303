import fiona
import rasterio
from rasterio.warp import transform_geom
from shapely.geometry import shape
from rasterio.mask import mask
from willchan.utils.mutil_task import MultiTasks


def china(shapefile_path, rasterfile_path, field=[]):
    dic = {}
    with fiona.open(shapefile_path, 'r') as shapefile:
        vector_crs = shapefile.crs
        # 打开栅格文件
        with rasterio.open(rasterfile_path) as raster:
            for feature in shapefile:
                list = []
                # 获取要素的id
                fid = feature['id']
                # 根据shp属性字段获取如行政区划名等
                for f in field:
                    list.append(feature['properties'].get(f))
                key = fid + ',' + ','.join(list)
                # 获取要素的几何形状
                geom = shape(feature['geometry'])
                geom = transform_geom(vector_crs, raster.crs, geom)
                # 使用掩膜函数获取覆盖的栅格数据
                out_image, out_transform = mask(raster, [geom], crop=True)
                out_image = out_image[out_image > 0]
                # 计算覆盖的栅格像元的值的和
                total_value = out_image.sum()
                dic[key] = total_value
                print(rf'{key}:', total_value)
            return dic


if __name__ == '__main__':
    shapefile_path = r'E:\科研文件\LI\全部数据\全国县级\行政边界_区县级.shp'
    rasterfile_path = rf'E:\科研文件\LI\全部数据\用电量\2019\EC2019.tif'
    china(shapefile_path, rasterfile_path, ['City'])
    pass

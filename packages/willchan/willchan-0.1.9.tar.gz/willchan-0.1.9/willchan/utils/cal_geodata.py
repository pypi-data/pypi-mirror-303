import fiona
import rasterio
from rasterio.warp import transform_geom
from shapely.geometry import shape
from rasterio.mask import mask
from willchan.utils.mutil_task import MultiTasks


def sum_raster_in_shp(shapefile_path, rasterfile_path, field=[]) -> dict:
    """
    cal the sum of raster value in the geometry of feature in shapefile
    :param shapefile_path: the path of shapefile
    :param rasterfile_path: the path of rasterfile
    :param field: the field of shapefile, such as ['City', 'Province']
    :return: a dict, key is id, fields, value is the sum of raster value in the geometry of feature
    """
    dic = {}
    with fiona.open(shapefile_path, 'r') as shapefile:
        vector_crs = shapefile.crs
        with rasterio.open(rasterfile_path) as raster:
            for feature in shapefile:
                variables = []
                # get fid
                fid = feature['id']
                # get shp fields
                for f in field:
                    variables.append(feature['properties'].get(f))
                key = fid + ',' + ','.join(variables)
                # get the geometry
                geom = shape(feature['geometry'])
                geom = transform_geom(vector_crs, raster.crs, geom)
                # mask the raster in geometry
                out_image, out_transform = mask(raster, [geom], crop=True)
                out_image = out_image[out_image > 0]
                # calculate the sum of raster value
                total_value = out_image.sum()
                dic[key] = total_value
                print(rf'{key}:', total_value)
            return dic


if __name__ == '__main__':
    shapefile_path = r'E:\科研文件\LI\全部数据\全国县级\行政边界_区县级.shp'
    rasterfile_path = rf'E:\科研文件\LI\全部数据\用电量\2019\EC2019.tif'
    sum_raster_in_shp(shapefile_path, rasterfile_path, ['City'])
    pass

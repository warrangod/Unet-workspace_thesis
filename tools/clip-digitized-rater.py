import processing
import os

out_path = 'Path/to/raster/output'
raster_path = 'Path/to/image/original'
vector_path = 'Path/to/digitized-mask/vector'
vec = []

def checkExtent(vector, raster):
    vec_extent = vector.extent()
    ras_extent = raster.extent()
    return vec_extent.xMaximum() < ras_extent.xMaximum() and vec_extent.xMinimum() > ras_extent.xMinimum() and vec_extent.yMaximum() < ras_extent.yMaximum() and  vec_extent.yMinimum() > ras_extent.yMinimum()

for root, sub, files in os.walk(vector_path):
    for filename in files:
        if filename.endswith('.gpkg'):
            vec.append(os.path.join(root, filename))
            try:
                os.mkdir(os.path.join(out_path, filename.split('.')[0]))
            except:
                print('Could not create sub: {}'.format(filename.split('.')[0]))
                pass
for root, sub, files in os.walk(raster_path):
    for filename in files:
        if filename.endswith('red.tif'):
            red = os.path.join(root,filename)
            blue = red.replace('red', 'blue')
            green = red.replace('red', 'green')
            nir = red.replace('red', 'nir')
            red_edge = red.replace('red', 'red_edge')
            dsm = red.replace('red', 'dsm')
            dtm = red.replace('red', 'dtm')

            red_raster = QgsRasterLayer(red, 'tempR')
            for i in vec:
                vector = QgsVectorLayer(i, 'tempVector{}'.format(i))
                if checkExtent(vector, red_raster):
                    print('yeah clipping {} , {}'.format((i.split('/')[-1].split('.')[0]), red.split('/')[-1]))
                    blue_raster = QgsRasterLayer(blue, 'tempB')
                    green_raster = QgsRasterLayer(green, 'tempG')
                    nir_raster = QgsRasterLayer(nir, 'tempN')
                    red_edge_raster = QgsRasterLayer(red_edge, 'tempRE')
                    dsm_raster = QgsRasterLayer(dsm, 'tempD')
                    dtm_raster  = QgsRasterLayer(dtm, 'tempD')
                    name = i.split('/')[-1].split('.')[0].split('/')[-1]
                    
                    outras = os.path.join(out_path, name, name + '_red.tif')
                    print(outras)
                    parameter = {  'INPUT': red_raster,
                                    'MASK': vector,
                                    'NODATA': None,
                                    'CROP_TO_CUTLINE': True,
                                    'OUTPUT': outras}
                    try:
                        processing.run('gdal:cliprasterbymasklayer', parameter)
                    except:
                        print('ERROR: Could not clip layer {}'.format(name))
                    
                    outras = os.path.join(out_path, name, name + '_blue.tif')
                    print(outras)
                    parameter = {  'INPUT': blue_raster,
                                    'MASK': vector,
                                    'NODATA': None,
                                    'CROP_TO_CUTLINE': True,
                                    'OUTPUT': outras}
                    try:
                        processing.run('gdal:cliprasterbymasklayer', parameter)
                    except:
                        print('ERROR: Could not clip layer {}'.format(name))

                    outras = os.path.join(out_path, name, name + '_green.tif')
                    print(outras)
                    parameter = {  'INPUT': green_raster,
                                    'MASK': vector,
                                    'NODATA': None,
                                    'CROP_TO_CUTLINE': True,
                                    'OUTPUT': outras}
                    try:
                        processing.run('gdal:cliprasterbymasklayer', parameter)
                    except:
                        print('ERROR: Could not clip layer {}'.format(name))

                    outras = os.path.join(out_path, name, name + '_nir.tif')
                    print(outras)
                    parameter = {  'INPUT': nir_raster,
                                    'MASK': vector,
                                    'NODATA': None,
                                    'CROP_TO_CUTLINE': True,
                                    'OUTPUT': outras}
                    try:
                        processing.run('gdal:cliprasterbymasklayer', parameter)
                    except:
                        print('ERROR: Could not clip layer {}'.format(name))

                    outras = os.path.join(out_path, name, name + '_rededge.tif')
                    print(outras)
                    parameter = {  'INPUT': red_edge_raster,
                                    'MASK': vector,
                                    'NODATA': None,
                                    'CROP_TO_CUTLINE': True,
                                    'OUTPUT': outras}
                    try:
                        processing.run('gdal:cliprasterbymasklayer', parameter)
                    except:
                        print('ERROR: Could not clip layer {}'.format(name))

                    outras = os.path.join(out_path, name, name + '_dsm.tif')
                    print(outras)
                    parameter = {  'INPUT': dsm_raster,
                                    'MASK': vector,
                                    'NODATA': None,
                                    'CROP_TO_CUTLINE': True,
                                    'OUTPUT': outras}
                    try:
                        processing.run('gdal:cliprasterbymasklayer', parameter)
                    except:
                        print('ERROR: Could not clip layer {}'.format(name))
                    
                    outras = os.path.join(out_path, name, name + '_dtm.tif')
                    print(outras)
                    parameter = {  'INPUT': dtm_raster,
                                    'MASK': vector,
                                    'NODATA': None,
                                    'CROP_TO_CUTLINE': True,
                                    'OUTPUT': outras}
                    try:
                        processing.run('gdal:cliprasterbymasklayer', parameter)
                    except:
                        print('ERROR: Could not clip layer {}'.format(name))

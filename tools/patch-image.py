from PIL import Image
import math
import os
from patchify import patchify
import numpy as np

path = 'Path/to/image/original'
pathout = 'Path/to/patched_image/output'
Image.MAX_IMAGE_PIXELS = None

for item in os.listdir(path):
    cerrent = os.path.join(path, item)
    for f in os.listdir(cerrent):
        if f.endswith('.tif'):
            print(f)
            id_plane = f.split('_')[0]
            out_dir = os.path.join(pathout, id_plane)

            if not os.path.exists(out_dir):
                os.mkdir(out_dir)

            deg_step = 10

            for a in range(0, 180//deg_step):
                deg = a*deg_step
                im = Image.open(os.path.join(cerrent,f))
                im = im.rotate(deg, expand=True)
                im = np.array(im)

                if 'rgb' in f:
                    patches = patchify(im, (256,256,3), step=128)
                elif 'mask' in f:
                    im[im<0] = -32768
                    patches = patchify(im, (256,256), step=128)


                for i in range(len(patches)):
                    for j in range(len(patches[i])):
                        image_out = os.path.join(out_dir, '{}-{}d_{}_{}.tif'.format(f.split('.')[0], deg, i, j))
                        if 'rgb' in f:
                            Image.fromarray(patches[i][j][0]).save(image_out)
                        elif 'mask' in f:
                            Image.fromarray(patches[i][j]).save(image_out)
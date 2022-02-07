Unet-workspace

This is my private repo for master degree thesis "Semantic segmentation of sugarcane plantation from multispectral images using deep learning"

Enviroment are setup with Anaconda env and use Jupyter notebook as an IDE for dev

tools dirctiory
    - clip-digitized-rater.py
    - patch-image.py

"clip-digitized-rater.py"   
script python for clip raster with digitized raster as a ground truth for machine learning. Using PyQgis API.


"patch-image.py"
script python for split raster image into small-patch for training with rotation and overlaped technique to augmetation data.
Using patchify lib install via pip install patchify

"Multiclass_Sugarcane_Unet.ipynb"
ipynb for execute training evaluation and prensent results
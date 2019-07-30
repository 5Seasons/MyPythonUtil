import SimpleITK as sitk
import numpy as np
import csv
import os
from PIL import Image
import matplotlib.pyplot as plt
# 对Ipython notebook 生效
# %matplotlib inline

work_path = 'D:\\project\\lung\\'
os.chdir(work_path)
csv_file = 'CSVFILES\\candidates_V2.csv'
img_path = 'subset0\\'
file_name = '1.3.6.1.4.1.14519.5.2.1.6279.6001.105756658031515062000744821260.mhd'

def load_itk_image(filename):
    itkimage = sitk.ReadImage(filename)
    numpyImage = sitk.GetArrayFromImage(itkimage)
    numpyOrigin = np.array(list(reversed(itkimage.GetOrigin())))
    numpySpacing = np.array(list(reversed(itkimage.GetSpacing())))
    return numpyImage, numpyOrigin, numpySpacing

def readCSV(filename):
    lines = []
    with open(filename) as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            lines.append(line)
    return lines

def worldToVoxelCoord(worldCoord, origin, spacing):
    stretchedVoxelCoord = np.absolute(worldCoord - origin)
    voxelCoord = stretchedVoxelCoord / spacing
    return voxelCoord

def normalizePlanes(npzarray):
    maxHU = 400.
    minHU = -1000.
    npzarray = (npzarray - minHU) / (maxHU - minHU)
    npzarray[npzarray>1] = 1.
    npzarray[npzarray<0] = 0.
    return npzarray

numpyImage, numpyOrigin, numpySpacing = load_itk_image(img_path+file_name)
cands = readCSV(csv_file)
cand=cands[1]
worldCoord = np.asarray([float(cand[3]),float(cand[2]),float(cand[1])])
voxelCoord = worldToVoxelCoord(worldCoord, numpyOrigin, numpySpacing)
voxelCoord = np.asarray([int(x) for x in voxelCoord])
voxelWidth = 65

patch = numpyImage[voxelCoord[0],voxelCoord[1] - voxelWidth/2:voxelCoord[1]+voxelWidth/2,voxelCoord[2]-voxelWidth/2:voxelCoord[2]+voxelWidth/2]
patch = normalizePlanes(patch)

itkimage = sitk.ReadImage(img_path+file_name)
numpyImage = sitk.GetArrayFromImage(itkimage)
    
patch.shape
plt.imshow(patch, cmap='gray')
plt.show()

from skimage import measure, feature
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
p = numpyImage.transpose(2,1,0)
p[p<-2000]=0
x=p[0]
y=p[1]
z=p[2]
ax.scatter(x,y,z)
plt.show()
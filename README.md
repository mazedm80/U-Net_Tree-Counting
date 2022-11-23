# Tree identification and counting in a natural growth forest using high-resolution satellite images

## 1.Introduction:
Tree cover mapping and counting play an essential role in applications like resource
inventories, wildlife habitat mapping, and biodiversity assessment. Monitoring in terms
of counting provides valuable information for various stakeholders.
In this research, I have utilised the high resolution four bands (Red, Green, Blue,
Infrared) PlanetScope 3 meters data to identify and count a single tree in the natural
growth forest. To achieve this goal, I developed a binary segmentation model using U-Net
architecture and a blob detection technique to
count the trees in Python. Both patch-based and pixel-based methods were used to train
the model. High temporal PlanetScope data comes in a 3m resolution, so it is suitable for
the classification task. However, the trees are not a big object compared to the 3m
resolution, so single tree identification will be an exciting challenge. In the forest
monitoring context, single tree detection is essential for many applications, including
resource inventories, wildlife habitat mapping, and biodiversity assessment. This project
has the primary aim of using remote sensing multi-spectral imagery to build a U-Net-like
CNN model that allows the identification and counting of trees. 
The promising results of this thesis confirm that high-resolution satellite
data combined with the proposed U-Net model can be beneficial for region-wide analysis
while keeping the cost low compared to other methods.

## 2. Project Structure:
Below you can find the file structure of the [github](https://github.com/mazedm80/U-Net_Tree-Counting) project:
<pre><code class="lang-txt">
├───data
├───images
├───logs
│   ├───Dice
│   ├───ELU
│   ├───IoU
│   ├───RELU
├───results
└───utility
│   │   plot.py
│   │   postprocess.py
│   │   preprocess.py
│
│   image_patch.ipynb
│   requirments.txt
│   Test_block.ipynb
│   U-net.ipynb
</code></pre>

## 3.Notebook files:
- image_patch.ipynb: Image processing and dataset creation.
- U-net.ipynb: Model defination and training and saving the model.
- Test_block.ipynb: Testing on the image blocks and extracting results.

## 4.Project Dependencies:
All the dependencies are listen in the requirments.txt file which can be installed into any virtual environment.
I have install gdal into [anaconda](https://www.anaconda.com/) environment with python 3.8.
<code class="lang-txt"><pre>
earthpy==0.9.4
fiona==1.8.20
gdal==3.3.3
geopandas==0.10.2
ipykernel==6.4.1
ipython==7.29.0
jupyter==1.0.0
keras==2.6.0
matplotlib==3.4.3
numpy==1.21.2
opencv==4.5.1
pandas==1.3.4
patchify==0.2.3
pillow==8.3.2
scikit-image==0.18.3
scikit-learn==1.0.1
shapely==1.8.0
tensorboard==2.6.0
tensorflow==2.6.0
</pre></code>

## 5.Conclusion:
Code is very far from being polished and perfect, as this project is created as a University thesis requirement.
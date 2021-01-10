# Python for data analysis project - Blocks classification dataset

![alt text](https://2.bp.blogspot.com/_JAoQEwT08KM/RoHt-Qelu9I/AAAAAAAACKk/ALlOTuCuO_E/w1200-h630-p-k-no-nu/RLSA_main.GIF)

## Project goal

##### The aim of this project is to analyze and make machine learning models on the "Page Blocks Classification" dataset by UCI.

### Page Blocks Classification dataset

https://archive.ics.uci.edu/ml/datasets/Page+Blocks+Classification 

The problem consists of classifying all the blocks of the page layout of a document that has been detected by a segmentation process. This is an essential step in document analysis in order to separate text from graphic areas. Indeed, the five classes are: text (1), horizontal line (2), picture (3), vertical line (4) and graphic (5).

**Data Set Information**

The 5473 examples comes from 54 distinct documents. Each observation concerns one block. All attributes are numeric. Data are in a format readable by C4.5. Missing Attribute Values: No missing value.

**Attribute Information**

height: integer. | Height of the block;

lenght: integer. | Length of the block;

area: integer. | Area of the block (height * lenght);

eccen: continuous. | Eccentricity of the block (lenght / height);

p_black: continuous. | Percentage of black pixels within the block (blackpix / area);

p_and: continuous. | Percentage of black pixels after the application of the Run Length Smoothing Algorithm (RLSA) (blackand / area);

mean_tr: continuous. | Mean number of white-black transitions (blackpix / wb_trans);

blackpix: integer. | Total number of black pixels in the original bitmap of the block;

blackand: integer. | Total number of black pixels in the bitmap of the block after the RLSA;

wb_trans: integer. | Number of white-black transitions in the original bitmap of the block;

prediction: integer. | Block classes : text (1), horizontal line (2), picture (3), vertical line (4) and graphic (5).

### Content of the project
1. page-blocks.csv : Page Blocks Classification dataset 
2. Blocks_classification.ipynb : jupyter notebook with data visualization and data modeling about the Page Blocks Classification dataset
3. api
4. Blocks classification presentation.pdf : presentation explaining the purpose of the project and its results

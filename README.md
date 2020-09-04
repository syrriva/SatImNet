# SatImNet
An open collection of training sets for satellite image classification and segmentation tasks

* A pre-print of a publication that describes the methodology behind the data sets structure and demonstrates a data fusion based satellite image classification can be found at https://arxiv.org/abs/2006.10623;​
* The native location of **SatImNet** collection is in the *EOS* storage system of the **Big Data Analytics Platform** (/eos/jeodpp/data/base/MachineLearning);
* The data are also provided via FTP: https://jeodpp.jrc.ec.europa.eu/ftp/public/MachineLearning/SatImNet/
* This repository contains the Python scripts (in the form of Jupyter notebooks) to access and query the **SatImNet** collection via FTP;
* Any feedback is very much welcome.

## Python 3 packages
The Jupyter notebooks have been tested with two Docker images having the following Python requirements:  
* [requirements_1.txt](https://github.com/syrriva/SatImNet/blob/master/Requirements/requirements_1.txt)
* [requirements_2.txt](https://github.com/syrriva/SatImNet/blob/master/Requirements/requirements_2.txt)

## Examples of Queries
```
# Use the string 'path' as 3rd argument in case you would like to retrieve the file paths only.

# Search for jpg files and class: 'PermanentCrop'
query = Query(content['tree'], 
               {'genre': 'jpg', 'class': ['PermanentCrop']}, 'path')
```
```
# Search for files having specific number of bands
query = Query(content['tree'], 
               {'type': 'file', 'metainfo_numofbands': 13})
```
```
# Search for masks having specific name
query = Query(content['tree'], 
               {'type': 'file', 'name': 'vienna', 'path': 'label'}, 'path')
```
```
# Search for files having specific size in terms of rows and columns
query = Query(content['tree'], 
               {'type': 'file', 'metainfo_columns': [100, 300], 'metainfo_rows': [100, 300]})
```

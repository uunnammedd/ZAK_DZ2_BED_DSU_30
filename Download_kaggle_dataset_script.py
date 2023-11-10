# !pip install opendatasets

import opendatasets as od

od.download("https://www.kaggle.com/datasets/rajyellow46/wine-quality/?select=winequalityN.csv","/content")
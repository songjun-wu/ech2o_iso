import numpy as np
import pandas as pd
import csv

df = pd.read_csv("./Spatial_250m/SpeciesParams.tab", header=None)

df.to_csv('SpeciesParams.tab', sep='\t', header=None, index=None)

for i in range(38):
    print(df.iloc[4], df.iloc[4].dtype)


#print(df)


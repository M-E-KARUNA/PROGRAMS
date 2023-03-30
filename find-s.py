import pandas as pd
import numpy as np
data=pd.read_csv("/storage/emulated/0/Audio/data.csv")
length=len(data.columns) 
spec_hyp=np.array(["¢"]*(length-1))
print("Initial Hypothesis",spec_hyp)
pos_sample=data[data.EnjoySport=="Yes"]
length=len(pos_sample)
total_attributes=np.array(data.columns)[:-1]
spec_hyp=np.array(pos_sample.loc[0])[:-1]
index=pos_sample.index[1:]
for i in index :
    for ind,att in enumerate(total_attributes):
        if spec_hyp[ind]!=pos_sample.loc[i][att]:
            spec_hyp[ind]="?"
  
               
print("General Hypothesis",spec_hyp) 
#by using a simple logic
print("another way")
print(["?" if len(set(pos_sample[att]))>1 else pos_sample.loc[0][att] for att in total_attributes])

#pandas
import pandas as pd
import numpy as np

d={ "stnames":["vishwa","akhil","dhaamu","rudra","rajesh","subba_Rayudu","ranganath","gagan","arjun","rama"],
   "tel":np.random.randint(low=45,high=99,size=10),
   "hin":np.random.randint(low=45,high=98,size=10),
   "eng":np.random.randint(low=35,high=96,size=10),
   "mat":np.random.randint(low=30,high=100,size=10),
   "sci":np.random.randint(low=38,high=97,size=10),
   "soc":np.random.randint(low=35,high=94,size=10),
   "evs":np.random.randint(low=35,high=96,size=10)
 }
df=pd.DataFrame(d)
print(df)

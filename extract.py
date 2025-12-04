print("extract the data from mysql")

import pandas as  pd

data={
    id:[1,2,3,4,5],
    "name":['a','b','c','d','e'],
    "marks":[10,20,30,40,50]
}

data=pd.DataFrame(data)
print(data)


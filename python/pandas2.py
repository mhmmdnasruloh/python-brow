"""
import pandas as pd

dataset = {
    'cars' : ["honda","civic","bmw"],
    'nomer' : ['1','2','3']
}

cobain = pd.DataFrame (dataset)
print(cobain) 

import pandas as pd
a = [1,9,2]
tes =pd.Series(a)
print(tes[2:0])

import pandas as pd
a = [1,9,8]
tes = pd.Series (a,index=["x","y","g"])
print ( tes)



import pandas as pd
calori = {"day1" : 50, "day2" : 30, "day3" : 12 }
acc = pd.Series (calori,index=["50","30"])
print(acc) 


import pandas as pd
data ={
    "nama" : [111,222,333],
    "waktu" : [323,123,321]
} 
cek = pd.DataFrame(data)
print (cek.loc[0])
"""
import pandas as pd
data = {
    arul = ( "ini adalah nama ") ,
}

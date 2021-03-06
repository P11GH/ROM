import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import json
import math


def rmse(x,y):
   sum=0
   for i in range(len(x)):
        sum=sum+(x.iloc[i]-y.iloc[i])*(x[i]-y[i])
   return math.sqrt(sum/len(x))

info = json.load(open('chiller'))
cc=info["cc"]
cop=info["cop"]

tab2=pd.read_csv('validation_result.csv')


x=np.arange(200000)


plt.scatter(tab2['real'],tab2['prediction'],color='y')



plt.plot(x,x+cc*2*0.1/cop,label='10%XRated Power (RMSE:'+str(round(rmse(tab2['real'],tab2['prediction'])/(cc*2/cop)*100))+'%)',color='r')
plt.plot(x,x-cc*2*0.1/cop,color='r')

#plt.plot(x[7000:],tab[tout][7000:],label='testing data')

plt.xlabel('Real [W]',fontsize=10)
plt.ylabel('Prediction [W]',fontsize=10)
#plt.xticks(xnum,xlab)
plt.xlim(0,200000)
plt.ylim(0,200000)
plt.legend()
plt.savefig('validation.png',bbox_inches = 'tight',pad_inches = 0)
plt.show()

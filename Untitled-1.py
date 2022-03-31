

from cmath import log
import math

loaded = []
fair = []
faceValue= [1,2,1,5,6,2,1,6,2,4]
l1 = log(1/2, 10)
l2 = log(1/10, 10)
l3 = log(.95, 10)
l4 = log(.05, 10)
l5 = log(1/6, 10)
l = 0
f = 0
for i in range(len(faceValue)):
    tmp = 0
    print(i)
    if(i==0):
        if(faceValue[i] == 6):
            loaded[i] = l1 + l4
            fair[i] = l1 + l5
        else:
            loaded[i] = l1 + l2
            fair[i] = l1 + l5
    else:
        if(faceValue[i] == 6):
            tmp = max(loaded[i-1] + l4,fair[i-1] + l4) + l1
            loaded[i] = tmp
            tmp = max(loaded[i-1] + l4,fair[i-1] + l3) + l5
            fair[i] = tmp
        else:
            tmp = max(loaded[i-1] + l3,fair[i-1] + l4) + l2
            loaded[i] = tmp
            tmp = max(loaded[i-1] + l4,fair[i-1] + l3) + l5
            fair[i] = tmp
            
 
import csv
import random

output = [1,3,3,2,1,2,1,1,2,2,3,1,3,1,2,3,1,2,3,2,3,1,3,3,2,3,3,2,3,1,3,
2,3,3,2,3,2,3,2,3,2,3,2,1,3,2,3,2,2,3,2,1,3,1,2,3,2,2,2,1,3,1,3,1,2,2,2,3,1,
1,2,1,2,3,1,2,2,3,2,3,1,3,1,3,3,2,2,3,1,2,2,3,1,2,3,1,2,3,1,3,3,2,3,2,2,3,1,
2,1,1,2,3,2,3,2,3,1,3,1,3,2,3,3,2,1,3,2,3,2,3,2,2,2,2,3,2,2,3,3,2,1,3,2,1,3,
1,3,1,3,3,3,2,3,2,1,3,2,2,2,3,2,3,1,3,1,2,3,2,3,2,2,2,3,2,2,1,3,2,2,1,2,3,2,
1,3,2,3,3,2,1,3,2,2,2,1,3,1,1,3,2,1,3,3,1,3,2,3,3,3,3,2,3,2,2,2,2,2,1,3,2,2,
2,2,2,2,2,1,3,2,1,1,2,1,3,3,1,2,3,1,3,3,1,1,2,3,3,3,2,3,2,1,1,1,2,1,2,3,1,1,
3,1,3,1,3,2,2,1,2,2,2,1,1,3,2,2,2,2,2,3,1,3,3,2,1,3,2,3,2,2,3,2,3,3,3,1,2,2,
2,3,2,3,2,2,2,3,3,2,3,1,2,2,2,2,3,3,1,2,2,2,3,2,1,3,3,3,2,3,3,1,3,1,1,2,2,3,
2,3,2,3,3,1,3,1,3,2,2,3,1,3,3,2,2,1,3,3,2,2,1,3,2,2,1,3,3,2,3,2,2,3,2,3,2,2,
3,1,3,2,3,2,3,2,2,1,2,3,1,3,2,3,2,2,1,2,2,1,3,2,3,2,2,1,2,1,3,2,3,2,3,3,2,2,
3,2,1,3,2,1,2,2,3,3,3,2,3,3,1,2,3,2,2,3,2,1,3,2,3,2,2,1,2,1,2,3,2,2,2,2,3,2,
3,1,3,1,3,2,2,3,1,1,2,2,3,2,3,3,2,3,1,3,2,2,3,3,1,2,2,3,1,1,3,2,3,1,3,1,3,2,
3,1,3,2,2,3,1,2,3,2,2,2,3,3,1,3,2,1,1,2,2,2,2,2,1,1,2,1,1,3,1,2,3,1,2,3,2,3,
2,2,3,2,3,1,3,2,3,1,2,2,3,2,2,1,2,1,3,3,3,3,2,3,2,3,1,2,2,1,3,3,1,2,3,2,1,2,
1,3,2,2,1,3,2,3,2,1,2,2,2,2,2,3,2,3,1,3,1,3,2,3,3,1,3,2,2,2,3,1,3,2,2,2,1,3,
3,2,1,3,2,1,1,2,2,1,3,2,1,2,3,2,3,2,3,3,1,3,3,3,2,1,1,3,1,1,3,2,2,3,1,3,2,3,
2,1,3,3,3,1,2,3,1,1,1,3,2,1,3,2,1,2,3,1,3,2,3,2,1,3,2,2,2,2,3,2,2,2,3,1,2,1,
1,2,1,3,3,1,3,3,2,2,2,1,3,2,2,1,3,1,3,1,3,2,3,3,3,1,3,2,2,3,2,2,3,3,1,3,1,3,
2,3,2,1,3,3,3,2,3,2,2,3,2,2,2,2,2,2,3,1,1,3,2,3,3,2,3,1,3,2,1,3,1,3,2,3,1,2,
3,2,1,3,2,2,3,3,2,2,2,2,2,2,3,3,2,2,2,3,3,1,3,1,3,3,2,2,2,3,1,2,2,3,3,2,3,3,
1,2,3,2,2,2,1,2,3,3,2,1,2,3,1,3,2,2,3,2,3,2,2,3,2,2,3,3,3,3,1,3,3,2,3,1,3,2,
3,2,2,2,3,1,3,1,2,2,2,3,2,3,2,3,2,2,3,1,1,3,1,3,2,3,2,3,3,3,2,3,1,3,3,1,3,1,
3,1,3,2,3,1,3,1,3,3,1,3,2,2,3,2,2,1,2,1,1,2,1,3,1,2,3,2,3,1,2,3,2,1,1,3,2,1,
3,2,1,2,2,2,2,2,3,2,1,3,2,1,2,2,3,1,2,3,3,2,2,1,3,1,3,2,3,1,3,1,3,2,1,2,2,1,
3,1,3,2,2,2,3,2,2,3,2,3,1,3,3,2,2,3,2,2,3,2,1,2,2,3,3,1,3,2,1,2,2,3,3,2,1,3,
1,3,1,3,2,2,2,3,2,1,3,1,3,1,2,2,2,3,1,3]
#1 == sunny 
#2 == cloudy      
#3 == rainy


print("---------------------------------------")
sunny = 0
rainy = 0
cloudy = 0
for day in output:
        if(day == 1):
                sunny+=1
        if(day == 2):
                cloudy+=1
        if(day == 3):
                rainy+=1
        
print("sunny:",sunny)
print(sunny/1000.00)
print("rainy:",rainy)
print(rainy/1000.00)
print("cloudy:",cloudy)
print(cloudy/1000.00)

afterS = 0
afterC = 0
afterR = 0
for i in range(1000):
        if(i == 999):
                break
        if(output[i] == 1):
                if(output[i+1] == 1):
                        afterS+=1
                elif(output[i+1] == 2):
                        afterC+=1
                elif(output[i+1]== 3):
                        afterR+=1
beforeS = 0
beforeC = 0
beforeR = 0
for i in range(1000):
        if(i == 0):
                pass
        if(output[i] == 1):
                if(output[i-1] == 1):
                        beforeS+=1
                elif(output[i-1] == 2):
                        beforeC+=1
                elif(output[i-1] == 3):
                        beforeR+=1

print("---------------------------------------")
print("after sunny is sunny:",afterS)
print(afterS/sunny)
print("after sunny is cloudy:",afterC)
print(afterC/sunny)
print("after sunny is rainy:",afterR)
print(afterR/sunny)
print("---------------------------------------")
print("before sunny is sunny:",beforeS)
print(beforeS/sunny)
print("before sunny is cloudy:",beforeC)
print(beforeC/sunny)
print("before sunny is rainy:",beforeR)
print(beforeR/sunny)
print("---------------------------------------")

            
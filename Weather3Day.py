import csv
import random

output = []
#1 == sunny 
#2 == cloudy      
#3 == rainy
weatherState = 1
output.append(1)
for i in range(999):
        x = random.randint(1,10)
        
        if(weatherState == 1):
                if(x == 1):
                        weatherState = 2
                        output.append(2)
                elif(x <= 5):
                        weatherState = 1
                        output.append(1)
                else:
                        weatherState = 3
                        output.append(3)
        elif(weatherState == 2):
                if(x <= 2):
                        weatherState = 1
                        output.append(1)
                elif(x <= 6):
                        weatherState = 2
                        output.append(2)
                else:
                        weatherState = 3
                        output.append(3)
        else:
                if(x <= 2):
                        weatherState = 1
                        output.append(1)
                elif(x <= 5):
                        weatherState = 3
                        output.append(3)
                else:
                        weatherState = 2
                        output.append(2)

print("---------------------------------------")
print("Total:",len(output))
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



                        

textfile = open("output.txt","w")
textfile.write("[")
c = 0
for element in output:
        if c != len(output):
                textfile.write(str(element)+",")
                c += 1
        if c == len(output):
                textfile.write(str(element))
textfile.write("]")
textfile.close





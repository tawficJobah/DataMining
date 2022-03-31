#By: Edgar Jr Bacallo , Tawfic Jobah, Aldair Martinez
#import matplotlib.pyplot as plt


import random
import csv
import math
import sys
import itertools
import time
import math


a = [71,68,68,66,77,69,72,74,70,72,70,69,72,75,68,69,67,70,70,70,71,66,66,79,70,64,73,71,69,73,75,71,65,74,71,71,68,74,68,69,70,67,73,68,70,66,69,69,75,66]
b = [180,160,205,175,213,175,250,211,220,160,195,155,230,250,200,196,170,215,167,202,165,163,175,215,212,135,230,176,178,200,168,205,150,198,151,194,150,275,170,193,135,188,175,190,215,145,155,185,222,190]
#a = [0,1,2,3,4,5,6,7,8,9]
#b = [2.1,4.7,4.8,6.6,8.5,9.9,10.1,10.9,11.7,13.1]
smallest_sum = 1000.0

for in1 in range(40): 
    for in2 in range(60):
        sum = 0.0 
        for i in range(50):
            sum += abs(in1*a[i] + in2- b[i])
        if a == 0 and b == 0: 
            smallest_sum = sum 
            print("Changed: ", smallest_sum)
        if smallest_sum > sum: 
            smallest_sum = sum
            print("Changed: ", smallest_sum)
            print("in1: ", in1, ", in2: ", in2)      
print(smallest_sum/10)

#Calculates for A
sumOfA = 0
for i in a:
    sumOfA = sumOfA + i
aAppend = []
print("sum of A: ", sumOfA)
meanOfA = sumOfA/50.00
for i in a:
    aAppend.append(pow((i - meanOfA),2))
sumOfSquare = 0
for i in aAppend:
    sumOfSquare = sumOfSquare + i
print("Sum of square: ", sumOfSquare)
#calculates for B
sumOfB = 0
for i in b:
    sumOfB = sumOfB + i
bAppend = []
print("sum of B: ", sumOfB)
meanOfB = sumOfB/50.00
print("Mean of B: ",meanOfB)

sumOfProducts = []
for i, j in zip(a,b):
    temp = (i - meanOfA) * (j - meanOfB)
    sumOfProducts.append(temp)

sop = 0
for i in sumOfProducts:
    sop = sop + i
print(sop)

slope = sop/sumOfSquare
bIntercept = meanOfB - (slope * meanOfA)
print("-----------------------------")
print("Slope: ", slope)
print("b Intercept: ",bIntercept)
print("-----------------------------")


#plt.scatter(a, b, label= "stars", color= "green",
#            marker= "*", s=30)


# corresponding y axis values
# plotting the points
#plt.plot(a,b)
# naming the x axis
#plt.xlabel('a')
# naming the y axis
#plt.ylabel('b')
# giving a title to my graph
#plt.title('plots')
# function to show the plot
#plt.show()
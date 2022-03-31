#By: Edgar Jr Bacallo , Tawfic Jobah, Aldair Martinez
import random
import csv
import math
import sys
import itertools
import time
import math
# p = probability
F = "F"
L = "L" 
ev_trial = [1,2,1,5,6,2,1,6,2,4]
a_t = [] #eval a)
b_t = [] #eval b)
c_t = [] #eval c)
for i in range(10):
    b_t.append("l")
for i in range(10):
    b_t.append("f")
for i in range(20):
    a_t.append("f")
    c_t.append("l")

logHalf = math.log(1.00/2.00,10)
logTenth = math.log(1.00/10.00,10)
logFair = math.log(.95,10)
logSwitch = math.log(.05,10)
logFairDie = math.log(1.00/6.00,10)

def bruteforce():
    out_a = -1000000
    out_b = 1
    out_ret = 0
    obj = ['f','l']
    current_list_val = []
    current_list_val = list(itertools.product(obj, repeat = len(ev_trial)))
    g = 0
    high_prob_list = []
    lowest_prob_list = []
    #######################################################
    for x in range(len(current_list_val)):
        #g += 1
        #print(g)
        if x == 0: #FIRST CHECK
            p = logSwitch #initialized p
            for i in range(len(ev_trial)):
                if current_list_val[x][i] == "f":
                    if i == 0: #if first was fair
                        p += logFairDie
                    elif current_list_val[x][i-1] == "f": # not transition
                        p += logFair + logFairDie
                    elif current_list_val[x][i-1] == "l": # transition
                        p += logSwitch * logFairDie 
                elif current_list_val[x][i] == "l":
                    if i == 0: #if first was loaded
                        if ev_trial[i] == 6:
                            p += logHalf
                        else:
                            p += logTenth
                    elif current_list_val[x][i-1] == "l": #not transition
                        if ev_trial[i] == 6:
                            p += logFair + logHalf
                        else:
                            p += logFair + logTenth
                    elif current_list_val[x][i-1] == "f": # transition
                        if ev_trial[i] == 6:
                            p += logSwitch + logHalf
                        else:
                            p += logFair + logTenth
                out_ret = p
                high_prob_list = list(current_list_val[x]).copy()
        else: 
            p = logSwitch #initialized p
            for i in range(len(ev_trial)):
                if current_list_val[x][i] == "f":
                    if i == 0: #if first was fair
                        p += logFairDie
                    elif current_list_val[x][i-1] == "f": # not transition
                        p += logFair + logFairDie
                    elif current_list_val[x][i-1] == "l": # transition
                        p += logSwitch + logFairDie
                elif current_list_val[x][i] == "l":
                    if i == 0: #if first was loaded
                        if ev_trial[i] == 6:
                            p += logHalf
                        else:
                            p += logTenth
                    elif current_list_val[x][i-1] == "l": #not transition
                        if ev_trial[i] == 6:
                            p += logFair + logHalf
                        else:
                            p += logFair + logTenth
                    elif current_list_val[x][i-1] == "f": # transition
                        if ev_trial[i] == 6:
                            p += logSwitch + logHalf
                        else:
                            p += logFair + logTenth
                out_a = p
            if out_a > out_ret:
                out_ret = out_a
                high_prob_list = list(current_list_val[x]).copy()
                print("highest probability checked at iteration: ", x+1)
            elif out_b > out_a:
                out_b = out_a
                lowest_prob_list = list(current_list_val[x]).copy()
    print ("highest probability list=", high_prob_list)
    print ("% = ", out_ret)
    print ("iterations = ", g)
    print ("lowest probability list = ", lowest_prob_list)
    print ("% = ", out_b)
                           
def main():
    p = 0.5 # total probability // initial prob 0.5 because either fair or loaded
    list_val = []
    val = int(input("Enter: \n 1 for a) \n 2 for b) \n 3 for c) \n 4 for brute \n"))
    if val == 1:
        list_val = a_t.copy()
    elif val == 2:
        list_val = b_t.copy()
    elif val == 3:
        list_val = c_t.copy()
    #print(list_val)    
    elif val == 4: 
        print("attempting... bruteforce()\n")
        bruteforce()
    if val != 4:
        for i in range(20):
            if list_val[i] == "f":
                if i == 0: #if first was fair
                    p *= 1/6.0
                elif list_val[i-1] == "f": # not transition
                    p *= 0.95 * 1/6.0
                elif list_val[i-1] == "l": # transition
                    p *= 0.05 * 1/6.0 
            elif list_val[i] == "l":
                if i == 0: #if first was loaded
                    if ev_trial[i] == 6:
                        p *= 1/2.0
                    else:
                        p *= 1/10.0
                elif list_val[i-1] == "l": #not transition
                    if ev_trial[i] == 6:
                        p *= 0.95 * 1/2.0
                    else:
                        p *= 0.95 * 1/10.0
                elif list_val[i-1] == "f": # transition
                    if ev_trial[i] == 6:
                        p *= 0.05 * 1/2.0
                    else:
                        p *= 0.95 * 1/10.0
        if val == 1:    
            print("input = ", a_t)
            print("for a) % = ", p)
        if val == 2:
            print("input = ", b_t)
            print("for b) % = ", p)
        if val == 3:
            print("input = ", c_t)
            print("for c) % = ", p)

main()
time.sleep(10)
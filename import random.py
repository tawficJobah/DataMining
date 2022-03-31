import random 
import csv


def main(): 
    weather = ["Sunny", "Rainy"]
    output = []
    output.append(random.randint(1,2)) #initial state no weight but ranomd
    #sunny = 1
    #rainy = 2
    #x be the randint for next weather
    for i in range(1000):
        x = random.randint(1,10)
        i += 1
        if output[i-1] == 1:
            if x >1:
                output.append(1)
            else:
                output.append(2)
        if output[i-1] == 2:
            if x > 5:
                output.append(1)
            else:
                output.append(2)
        if i == 999:
            break
    print(output)
    #print len(output)
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

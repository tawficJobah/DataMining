

import math

from sklearn import neighbors


known_Column_A = [5.1,4.9,4.7,4.6,5,5.4,4.6,5,4.4,4.9,5.4,4.8,4.8,5.1,4.6,5.1,4.8,5,5,5.2,5.2,5.5,4.9,4.4,5.1,5,4.5,4.4,5,5.1,4.8,5.1,4.6,6.9,5.5,6.5,5.7,6.3,5.2,5,5.9,6,6.1,5.8,6.2,5.6,5.9,6.1,6.3,6.1,6.4,5.8,6,5.4,6,6.7,6.3,5.6,5.5,5.5,6.1,5.8,5,5.6,5.7,5.7,6.2,6.3,6.5,7.6,4.9,7.3,6.7,7.2,6.5,6.4,6.8,5.7,5.8,6.4,6.5,7.7,7.7,7.7,6.3,6.7,7.2,6.2,6.1,6.4,6.1,7.7,6.3,6.4,6,6.9,6.7,6.9,5.8,6.8 ]
known_Column_B = [3.5,3,3.2,3.1,3.6,3.9,3.4,3.4,2.9,3.1,3.7,3.4,3,3.7,3.6,3.3,3.4,3,3.4,3.5,3.4,3.5,3.1,3,3.4,3.5,2.3,3.2,3.5,3.8,3,3.8,3.2,3.1,2.3,2.8,2.8,3.3,2.7,2,3,2.2,2.9,2.7,2.2,2.5,3.2,2.8,2.5,2.8,2.9,2.7,2.7,3,3.4,3.1,2.3,3,2.5,2.6,3,2.6,2.3,2.7,3,2.9,2.9,2.9,3,3,2.5,2.9,2.5,3.6,3.2,2.7,3,2.5,2.8,3.2,3,3.8,2.6,2.8,2.7,3.3,3.2,2.8,3,2.8,2.6,3,3.4,3.1,3,3.1,3.1,3.1,2.7,3.2]
known_Column_C = [1.4,1.4,1.3,1.5,1.4,1.7,1.4,1.5,1.4,1.5,1.5,1.6,1.4,1.5,1,1.7,1.9,1.6,1.6,1.5,1.4,1.3,1.5,1.3,1.5,1.3,1.3,1.3,1.6,1.9,1.4,1.6,1.4,4.9,4,4.6,4.5,4.7,3.9,3.5,4.2,4,4.7,4.1,4.5,3.9,4.8,4,4.9,4.7,4.3,3.9,5.1,4.5,4.5,4.7,4.4,4.1,4,4.4,4.6,4,3.3,4.2,4.2,4.2,4.3,5.6,5.8,6.6,4.5,6.3,5.8,6.1,5.1,5.3,5.5,5,5.1,5.3,5.5,6.7,6.9,6.7,4.9,5.7,6,4.8,4.9,5.6,5.6,6.1,5.6,5.5,4.8,5.4,5.6,5.1,5.1,5.9]
known_Column_D = [0.2,0.2,0.2,0.2,0.2,0.4,0.3,0.2,0.2,0.1,0.2,0.2,0.1,0.4,0.2,0.5,0.2,0.2,0.4,0.2,0.2,0.2,0.1,0.2,0.2,0.3,0.3,0.2,0.6,0.4,0.3,0.2,0.2,1.5,1.3,1.5,1.3,1.6,1.4,1,1.5,1,1.4,1,1.5,1.1,1.8,1.3,1.5,1.2,1.3,1.2,1.6,1.5,1.6,1.5,1.3,1.3,1.3,1.2,1.4,1.2,1,1.3,1.2,1.3,1.3,1.8,2.2,2.1,1.7,1.8,1.8,2.5,2,1.9,2.1,2,2.4,2.3,1.8,2.2,2.3,2,1.8,2.1,1.8,1.8,1.8,2.1,1.4,2.3,2.4,1.8,1.8,2.1,2.4,2.3,1.9,2.3]
known_Column_E = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]

unknown_A = [4.3,5.8,6,5,7,6.6,5.7,6.3,6.9,6.3,5.4,5.1,5.7,4.9,5.8,5.1,7.1,6.4,5.3,5.6]
unknown_B = [3,4,2.2,3.3,3.2,2.9,2.8,3.3,3.2,2.8,3.9,3.5,3.8,2.4,2.7,2.5,3,3.2,3.7,2.8]
unknown_C = [1.1,1.2,5,1.4,4.7,4.6,4.1,6,5.7,5.1,1.3,1.4,1.7,3.3,5.1,3,5.9,4.5,1.5,4.9]
unknown_D = [0.1,0.2,1.5,0.2,1.4,1.3,1.3,2.5,2.3,1.5,0.4,0.3,0.3,1,1.9,1.1,2.1,1.5,0.2,2]

def Distance(xone,xtwo,yone,ytwo,wone,wtwo,zone,ztwo):
    return math.sqrt(math.pow((xone - xtwo), 2) + math.pow((yone - ytwo), 2) + math.pow((wone - wtwo), 2) + math.pow((zone - ztwo), 2))

def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return math.sqrt(distance)

def KNN(known,unknown,k):
    distances = list()
    for known_row in known:
        dist = euclidean_distance(unknown,known_row)
        distances.append((known,dist))
        distances.sort(key=lambda tup: tup[1])
        neighbors = list()
        for i in range(k):
            neighbors.append(distances[i][0])
    return neighbors
train = []

for unknownflower in range(1):
    smallestDistance = 0.0
    tmp = 0
    ans = []
    distance = []
    anstmp = 0
    tempArray = []
    for knownFlower in range(len(known_Column_A)):
        tmp = Distance(known_Column_A[knownFlower],unknown_A[unknownflower],
                        known_Column_B[knownFlower],unknown_B[unknownflower],
                        known_Column_C[knownFlower],unknown_C[unknownflower], 
                        known_Column_D[knownFlower],unknown_D[unknownflower])
        tempArray.append(tmp)
        if(tmp > smallestDistance):
            smallestDistance = tmp
            anstmp = known_Column_E[knownFlower]
    tempArray.sort(reverse=True)
    #print(tempArray)
    #print("-----------------------------")
    ans.append(anstmp)
    distance.append(smallestDistance)
    #print(ans,smallestDistance)



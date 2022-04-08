from cmath import log
import csv
import math

def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    return num
def manhattanDistance(row1,row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += abs(row1[i] - row2[i])
    return distance

def distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += math.pow(row1[i] - row2[i],2)
	return math.sqrt(distance)

def get_neighbors(known, unkown, k):
	distances = list()
	for known_row in known:
		dist = distance(unkown, known_row)
		distances.append((known_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(k):
		neighbors.append(distances[i][0])
	return neighbors

filename = "KNN.csv"
known = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in csvreader:
        known.append(row)
    print("Total no. of rows: %d"%(csvreader.line_num))

filename = "testing.csv"
unknownWhole = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in csvreader:
        unknownWhole.append(row)
    print("Total no. of rows: %d"%(csvreader.line_num))

for unknown in unknownWhole:
    neighbors = get_neighbors(known,unknown,7)
    flowerType = []
    for neighbor in neighbors:
        flowerType.append(neighbor[4])

    print("Flower class: ", most_frequent(flowerType))

newUnknown = []
newKnown = []
for i in range(len(known)):
    if(i < 20):
        newUnknown.append(known[i])
    else:
        newKnown.append(known[i])

print(newUnknown)




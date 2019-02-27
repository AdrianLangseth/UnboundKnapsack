import time
# Python3 program to find maximum
# achievable value with a knapsack
# of weight W and multiple instances allowed.

# Returns the maximum value
# with knapsack of W capacity
def unboundedKnapsack(capacity: int, weight: list, value: list, num):
    """
    Algoritme for (g)løsning av 0-1 unbounded knapsack problem
    :param capacity: capacity
    :param weight: List of weights of items
    :param value: List of values corresponding to item
    :param num: Amount of items
    :return:
    """

    # dp[i] is going to store maximum value with knapsack capacity i.
    dp = [0 for i1 in range(capacity + 1)]
    indeces = [[0 for i3 in range(num)] for i2 in range(capacity + 1)]
    ans = 0

    # Build table Knapsack[][] in bottom up manner
    for i in range(capacity + 1):
        for j in range(num):
            if weight[j] <= i:
                # dp[i] = max(dp[i], dp[i - weight[j]] + value[j])
                if dp[i] < dp[i - weight[j]] + value[j]:
                    dp[i] = dp[i - weight[j]] + value[j]
                    k = indeces[i - weight[j]]
                    q = k.copy()
                    q[j] += 1
                    indeces[i] = q

    return dp[capacity], indeces[capacity]


def get_from_excel(filename):
    f = open(filename, 'r', encoding='utf8', errors='ignore')
    namelist = []
    prisliste = []
    volummengde = []

    thisline = f.readline()
    thisline = thisline.strip('\n')
    thislineMatrix = thisline.split(';')

    print(str(thislineMatrix[1]) + str(thislineMatrix[3] + str(thislineMatrix[4])))

    for line in f.readlines():
        try:
            thisline = line.split(';')
            namelist.append(thisline[0])
            prisliste.append(thisline[1])
            time.sleep(0.08)
            volum = float(thisline[2])
            alkohol = float(thisline[3])
            volummengde.append(volum * alkohol)
        except:
            break

    return namelist, prisliste, volummengde


def matrix_round_float_to_int(floatList):
    for i in range(len(floatList)):
        try:
            time.sleep(0.05)
            floatList[i] = round(float(floatList[i]))
        except ValueError:
            break
    return floatList



def list_to_indeces(list):
    indexlist=[]
    for i in range(len(list)):
        if list[i] >= 1:
            indexlist.append((i, list[i]))
    return indexlist


'''
# Driver program
W = 20
val = [3, 6, 4]
wt = [1, 2, 3]
n = len(val)

print(unboundedKnapsack(W, wt, val, n))

'''

Konto = 1025


Navneliste, prisliste, volumliste = get_from_excel('poldata2.csv')
x=7
prisliste = prisliste[0:498]
Navneliste = Navneliste[0:498]
volumliste = volumliste[0:498]
print('ok')
prisliste = matrix_round_float_to_int(prisliste)
y = 7


cash, indeces = unboundedKnapsack(Konto, prisliste, volumliste, len(volumliste))
print(cash, list_to_indeces(indeces))

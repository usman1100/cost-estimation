# %% [markdown]
# ## Setup
# 
# 1. Importing libraries
# 2. Creating utility methods

# %%
import pandas as pd
import math


def ManhattanDistance(point_array_1:list, point_array_2:list):
    
    length_1 = len(point_array_1)
    length_2 = len(point_array_2)

    if length_2 != length_1:
        raise Exception("The dimensions of given points are not equal")
    

    else:
        sum = 0
        for i in range(length_1):
            sum += abs(point_array_1[i] - point_array_2[i])
        
        return sum
    
def Euclidean(x:list, y:list):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return distance

# %% [markdown]
# ## Datasets
# 
# 1. Loading datasets
# 2. Normaliznig datasets to use in models

# %%
# Loading training dataset
train_data_url = '../UCP-Plus.csv'
data = pd.read_csv(train_data_url)
df = data
efforts = data["Effort"] # Extracting effort column
values = df.values.tolist() # Converting dataframe to list
l = len(values) # Number of rows in the dataset


test_data_url = "../testData.csv"
testDF = pd.read_csv(test_data_url) # Loading test dataset
testEfforts = testDF["Real_Effort"] # Extracting effort column

testData = testDF.values.tolist() # Converting dataframe to list
l_test = len(testData) # Number of rows in test dataset




# %% [markdown]
# ## Method for calulating closest analogies

# %%


def getClosestCases(datapoint, k=2, onlyAvg=True):
    
    manDistances = [] # List of manhattan distances
    eucDistances = [] # List of euclidean distances
    average = [] # List of average distances


    for i in range(1, l):

        # i-th point of the dataset
        compared = values[i]


        euc = Euclidean(datapoint, compared) # calculating euclidean distance
        eucDistances.append({"distance":euc, "index":i}) # appending result to list


        man = ManhattanDistance(datapoint, compared) # calculating manhattan distance
        manDistances.append({"distance":man, "index":i}) # appending result to list


        avg = (euc + man)/2 # calculating average of manhattan and euclidean distances
        average.append({"distance":avg, "index":i}) # appending result to list

    # Sorting all distances
    average = sorted(average, key = lambda i: i['distance'])
    manDistances = sorted(manDistances, key = lambda i: i['distance'])
    eucDistances = sorted(eucDistances, key = lambda i: i['distance'])

    # using the average of both distances
    if onlyAvg:
        return average[:k]
    else:
        return average[:k], manDistances[:k], eucDistances[:k]



# %% [markdown]
# ## Results of Test Data #1

# %%
cases_1 = getClosestCases(testData[0])
print("Closest 2 Analogies")
for case in cases_1:
    print("Test Data Project #" + str(case["index"]) + "\t -- Project Effort: " + str(round(case["distance"], 1)))
    

# %% [markdown]
# ## Results of Test Data #2

# %%
cases_2 = getClosestCases(testData[1])
print("Closest 2 Analogies")
for case in cases_2:
    print("Test Data Project #" + str(case["index"]) + "\t -- Project Effort: " + str(round(case["distance"], 1)))
    

# %% [markdown]
# ## Results of Test Data #3

# %%
cases_3 = getClosestCases(testData[2])
print("Closest 2 Analogies")
for case in cases_3:
    print("Test Data Project #" + str(case["index"]) + "\t -- Project Effort: " + str(round(case["distance"], 1)))

# %% [markdown]
# ## Results of Test Data #4

# %%
cases_4 = getClosestCases(testData[3])
print("Closest 2 Analogies")
for case in cases_4:
    print("Test Data Project #" + str(case["index"]) + "\t -- Project Effort: " + str(round(case["distance"], 1)))
    

# %% [markdown]
# ## Calculation Results for Test Data Project #1

# %%
def printResults(datapoint):

    manDistances = [] # List of manhattan distances
    eucDistances = [] # List of euclidean distances
    average = [] # List of average distances


    for i in range(1, l):

        # i-th point of the dataset
        compared = values[i]


        euc = Euclidean(datapoint, compared) # calculating euclidean distance
        man = ManhattanDistance(datapoint, compared) # calculating manhattan distance
        avg = (euc + man)/2 # calculating average of manhattan and euclidean distances

        print(compared)
        break
    


    
    

# %%
printResults(testData[0])
printResults(testData[1])

# %%




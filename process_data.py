import pandas as pd
import numpy as np

# 2 arrays used to fill with data - a = column 1 and b = column 2
a = []
b = []


# open raw data file.
# change "data.txt" to the name of your input file. You may need to include the path to the file.
with open("data.txt","r") as file:
        # split data line by line
        data=iter(file.read().split())

        while True:
                try:
                        # a1 = first string or word in column1
                        a1= next(data)
                        # b1 = ''      ''   ''   '' '' column2
                        b1= next(data)
                        #print(a,b) # used to debug
                        # append to both arrays
                        a.append(a1)
                        b.append(b1)

                except StopIteration:
                        print("No more pair")
                        break

# turn a and b into numpy arrays
a_np = np.array(a)
b_np = np.array(b)

# create two column file, voltage and current may be subject to change
df = pd.DataFrame({"Voltage" : a_np, "Current" : b_np})

# turn it into a csv and save it to a specific directory. obviously you will need to change the file path
df.to_csv(r'~/Desktop/Spring 21/EE 584/post_process.csv', index=None)

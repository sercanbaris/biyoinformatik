import os
import pandas as pd

for file in os.listdir():
    if file.endswith('.xlsx'):
        df = pd.read_excel(file)
        print(file[:6], df.columns[4], df.iloc[:, 4].mean(), df.iloc[:, 5].mean(), df.iloc[:, 6].mean(), df.iloc[:, 7].mean(), 
              df.iloc[:, 8].mean(), df.iloc[:, 9].mean())
        with open('output.txt', 'a') as output_file:
            output_file.write(file[:6] + " " + str(df.iloc[:, 4].mean()) + " " + str(df.iloc[:, 5].mean()) + " " + str(df.iloc[:, 6].mean()) + " " + str(df.iloc[:, 7].mean()) + " " + str(df.iloc[:, 8].mean()) + " " + str(df.iloc[:, 9].mean()) + '\n')

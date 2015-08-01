__author__ = 'Steve'
# testing
import matplotlib.pyplot as plt
import numpy as np
import csv
from performance import parse

RUN_FILE = 'pythonrunning.csv'

def main():
    # Call our parse function with required file an delimiter
    new_data, race_count = parse(RUN_FILE, ',')
    print("this is our data", new_data)
    print("There were this number of races: ", race_count)
    print(new_data[0].keys())
    #  for dict_item in new_data:
        #  print(type(dict_item["Name"]))
        #  print(dict_item["Date"])

if __name__ == "__main__":
    main()


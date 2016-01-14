# testing
# import matplotlib.pyplot as plt
# import numpy as np
import csv
import tkinter as tk
from collections import Counter
import os as system

#TODO Get total distance for runners / get program to stop!

TIME_TRIAL_DISTANCE = 3.0 


# Working through https://automatetheboringstuff.com/chapter12/#calibre_link-64
# 10 July 2015 branched to follow newcoder.io tutorial on data visualization
# 11 November 2015 Added to desktop

RUN_FILE = 'timetrial/timetrial.csv'


def parse(raw_file, delimiter):
    """
    :param raw_file: probably csv file
    :param delimiter: specify delimiter #TODO add default arg : ','
    :return: parsed data
    Parses a raw CSV file to a JSON-line object.
    """

    # open csv file
    opened_file = open(raw_file)

    # read csv file
    csv_data = csv.reader(opened_file, delimiter=delimiter)  # first delimiter is csv.reader variable name
    # csv_data object is now an iterator meaning we can get each element one at a time

    # build data structure to return parsed data
    parsed_data = []  # this will store every row of data
    
    #  racer_count = 0
    fields = csv_data.__next__()  # this will be the column headers; we can use .next() because csv_data is an iterator
    for row in csv_data:
        if row[1] == "": # there is no text in the runner field so no data to process
            pass
        else:
            parsed_data.append(dict(zip(fields, row)))  # Creates a new dict item for each row with col header as key
        #  racer_count += 1  # This is number of racers not races
    # count number of races
    runners_in_race = Counter(item['Date'] for item in parsed_data)  # stores the number of races
    print("number of races is: ", len(runners_in_race))
    print("the races are: ")
    for k, v in runners_in_race.items():
        print(k, "-->", v)
    # close csv file
    opened_file.close()

    return parsed_data


def visualize_races(data_file):
    """
    :return: There is no data returned here but an image of the graph is saved to the working directory
    """

    #  use 'counter' to count the races
    dates = []
    # counter = Counter(item['Date'] for item in data_file) #  list comprehension: pythonic loop construction
    runner_counter = Counter(item['Runner'] for item in data_file)  # stores the number of races per runner
    print("runner counter is: ", runner_counter)
    runner_list = [runner for runner in sorted(runner_counter)]  # stores list of runners full names
    runner_list.pop(0)  # first value is the null value
    print("Runner list is :", runner_list)
    runner_data = [runner_counter[runner] for runner in runner_counter]  # Creates list of data points
    runner_data.pop(0)  # first value is all the null rows so we can remove it
    runner_tuple = tuple(sorted(runner_list))  # This will be the label. The results may be in a different order
    #  for runner in runner_tuple : print("next runner is : ", runner, "with ", runner_counter[runner], "runs")
    #  TODO edit x-axis label to reflect correct order - not alphabetical
    #  print("runner_data is : ", runner_data)
    #  print("runners :", runner_tuple)
    #  print("runner_list", runner_list)

    # Give more room so x-axis labels aren't cut off
    plt.subplots_adjust(bottom=0.6)  # subplots can be used to adjust spacing around the graph

    #  separate the x-axis (runners) from the counter variable for the y-axis - races per runner

    #  assign y-axis (counter) data to a matplotlib plot instance
    #  runner_data = runner_data.sort
    print("************ Runner Data ************ ", runner_data)
    plt.plot(runner_data)

    #  create the number of ticks needed and assign labels
    plt.xticks(range(len(runner_tuple)), runner_tuple, rotation=90)

    #  save the plot
    plt.savefig("Runners.png")

    #  close the plot file
    plt.clf()


def visualize_type(new_data):
    """
    :return:
    """

    # grab parsed data
    # new_data is passed as parameter until I work out how to parse(MY_FILE, ",") from here

    # create counter to count category entries
    counter = Counter(item['Category'] for item in new_data)
    print(counter)

    #  Add total distance run
    print("first item in data is : ", new_data[0])
    # set the labels based on keys, order doesn't matter so can just use counter.keys()
    labels = tuple(counter.keys())

    # Set exactly where the labels hit the x-axis
    # xlocations uses np.arange to store an array that we can manipulate better than range()
    xlocations = np.arange(len(labels)) + 0.5

    # Set width of each bar
    width = 0.5

    # Assign data to a bar plot
    plt.bar(xlocations, counter.values(), width=width)

    # Assign labels and tick location to x-axis
    plt.xticks(xlocations + width / 2, labels, rotation=90)

    # Give more room so x-axis labels aren't cut off
    plt.subplots_adjust(bottom=0.4)  # subplots can be used to adjust spacing around the graph

    # Increase size of graph
    plt.rcParams['figure.figsize'] = 12, 8 # figure.figsize is a 'key' that takes height and width params

    # save the plot
    plt.savefig("categories.png")

    # close plot figure
    plt.clf()

    return

def get_runners_list(new_data): 
    runner_counter = Counter(item['Runner'] for item in new_data)  # stores the number of races per runner
    print("runner counter is: ", runner_counter)
    runners_list = [runner for runner in sorted(runner_counter)]  # stores list of runners full names
    runners_list.pop(0)  # first value is the null value
    print("Runner list is :", runners_list)
    return runners_list

def get_distances(new_data):
    total_distance = 0
    for race in new_data:
        if race['Runner'] != "" :
            total_distance += float(TIME_TRIAL_DISTANCE)
    return total_distance

def get_runners(new_data): # go through the data file to get a list of runners
    runner_counter = Counter(item['Runner'] for item in data_file)  # stores the number of races per runner
    print("runner counter is: ", runner_counter)
    runners_list = [runner for runner in sorted(runner_counter)]  # stores list of runners full names
    runners_list.pop(0)  # first value is the null value
    print("Runner list is :", runners_list)
    return(runners_list)


def get_runners_distances(new_data, runners_list): #TODO this is not working
    runners_distances = {} # Dictionary to store cumulative distances
    for runner in runners_list :
        runners_distances[runner] = 0 # set to 0 ready to add race distances
    print('runners distance dict is: ', runners_distances)
    for race in new_data:
        print('name is: ', race['Runner'], 'distance is : ', TIME_TRIAL_DISTANCE)
        try:
            runners_distances[race['Runner']] += float(TIME_TRIAL_DISTANCE)
            print(race['Runner'], ' has raced ', runners_distances[race['Runner']], ' at the end of the ', race['Race'], 'race') # TODO need to use formats here
            # Error Need to trap last race
        except:
            pass # we have reached the end of the races . TODO trap this better we are also storing null values. Look at csv file.
        print("Time Trial")
    return runners_distances

def present_race_information(total_miles, championship_miles):
    # Tkinter testing
    top = tk.Tk()
    F = tk.Frame(top)
    dir(top)
    F.pack()
    total_miles_report = 'All Miles Total: ' + str(int(total_miles + 0.5))
    championship_miles_report = 'Championship Miles Total: ' + str(int(championship_miles + 0.5))
    lFunMiles = tk.Label(F, text=total_miles_report)
    lFunMiles.pack()
    lChampionshipMiles = tk.Label(F, text=championship_miles_report)
    lChampionshipMiles.pack()
    top.mainloop()


def main():
    # Call our parse function with required file an delimiter
    new_data = parse(RUN_FILE, ',')
    print("The keys in the data are:", new_data[0].keys())
    runners_list = get_runners_list(new_data)
    print("Runners are: ", runners_list)
    runners_distances = get_runners_distances(new_data, runners_list)
    print("Runners distances are:", runners_distances)
    total_distance = get_distances(new_data)
    print('Total distance run : ', total_distance)
    # present_race_information(total_distance)

if __name__ == "__main__":
    main()

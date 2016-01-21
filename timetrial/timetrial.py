# testing
# import matplotlib.pyplot as plt
# import numpy as np
import csv
import tkinter as tk
from collections import Counter
import os as system

#TODO Get fastest time. runner_summary function shoud do this
#TODO Finally found problem with tuples: needed to initialise as list i.e. : [0,0,0] instead of 0,0,0

TIME_TRIAL_DISTANCE = 3.0 


# Working through https://automatetheboringstuff.com/chapter12/#calibre_link-64
# 10 July 2015 branched to follow newcoder.io tutorial on data visualization
# 11 November 2015 Added to desktop

# RUN_FILE = 'timetrial/timetrial.csv' # this is fullfile
RUN_FILE = 'timetrial/timetrialtest.csv' # this is test file


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
    parsed_data = []  # this list will store every row of data
    fields = csv_data.__next__()  # this will be the column headers; we can use .next() because csv_data is an iterator
    for row in csv_data:
        if row[1] == "": # there is no text in the runner field so no data to process
            pass
        else:
            parsed_data.append(dict(zip(fields, row)))  # Creates a new dict item for each row with col header as key and stores in a list
        #  racer_count += 1  # This is number of racers not races
    print("data list is: ", parsed_data)
    print("Type of parsed_data is: ", type(parsed_data))
    # close csv file
    opened_file.close()
    return parsed_data

def races_summary(race_data):
    # count number of races, races per day, and races per runner
    runners_by_date = Counter(item['Date'] for item in race_data)  # each element contains date and number of runners for that date
    races_by_runner = Counter(item['Runner'] for item in race_data)  # each element contains runner and number of races for that runner
    print("number of races is: ", len(runners_by_date))
    #print("the races are: ")
    #for k, v in runners_by_date.items():
    #    print(k, "-->", v)
    #print("The races by each runner: ")
    #for k, v in races_by_runner.items():
    #    print(k, "-->", v)
    return

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

def get_runners_starting_list(new_data): 
    runner_counter = Counter(item['Runner'] for item in new_data)  # stores the number of races per runner
    print("runner counter is: ", runner_counter)
    runners_list = [runner for runner in sorted(runner_counter)]  # stores list of runners full names
    # create list of runners including name, number of races, distance and time
    runners_summary ={}
    # runners_summary['fields'] = 'races', 'total_distance', 'total_time'
    for runner in runners_list:
        runners_summary[runner] = [0, 0, 0]
    print("Runners summary at start is: ", runners_summary)


    print("Runner list is :", runners_list)
    print("************")
    return runners_list, runners_summary

def get_distances(new_data):
    total_distance = 0
    for race in new_data:
        if race['Runner'] != "" :
            total_distance += float(TIME_TRIAL_DISTANCE)
    return total_distance

def get_runners_summary(new_data, runners_summary): #TODO get max pace
    print("*** get_runners_summary starts ***")
    runners_pace_dict = {}
    #for runner in runners_list :
    #    runners_pace_dict[runner] = '' # set to '' ready to add runners pace
    #print('*** runners pace dict is: ', type(runners_pace_dict), runners_pace_dict) # debug only
    for result in new_data:
        # print("result item is:", type(result), result)
        #print(result['Runner'], "'s pace was : ", result['Pace'])
        #runners_pace_dict[result['Runner']] = result['Pace']
        #print("All runners paces are: ", runners_pace_dict)

        #try:
        #    runners_distances[race['Runner']] += float(TIME_TRIAL_DISTANCE)
        #    print(race['Runner'], ' has raced ', runners_distances[race['Runner']], ' at the end of the ', race['Race'], 'race') # TODO need to use formats here
        #    # Error Need to trap last race
        #except:
        #    print("Error: get_runners_summary exception reached")
        #    pass # we have reached the end of the races . TODO trap this better we are also storing null values. Look at csv file.
        
        print(result)
        print("runner field 3 type is is: ", type(runners_summary[result['Runner']][0]))
        print("runners_summary element type is: ", type(runners_summary[result['Runner']]))
        runners_summary[result['Runner']][0] = 3
    print("*** Runners Summary is now : ", runners_summary)
    print("*** get_runners_summary ends ***")    
    return runners_summary

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
    race_data = parse(RUN_FILE, ',')
    races_summary(race_data)
    print("The keys in the data are:", race_data[0].keys())
    runners_list, runners_summary = get_runners_starting_list(race_data)
    print("Runners are: ", runners_list)
    runners_distances = get_runners_summary(race_data, runners_summary)
    print("Runners distances are:", runners_distances)
    total_distance = get_distances(race_data)
    print('Total distance run : ', total_distance)
    # present_race_information(total_distance)

if __name__ == "__main__":
    main()

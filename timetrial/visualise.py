import matplotlib.pyplot as plt
import numpy as np
import tkinter as
from collections import Counter

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

# present_race_information(total_distance)

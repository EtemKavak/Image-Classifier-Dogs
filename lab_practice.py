

# 1. Imports python modules

from time import time, sleep


# set start time
start_time = time()


# set the end_time
sleep(75) # temp code to simulate the timing code
end_time = time()

# set tot_time to computes overall runtime 
tot_time = end_time - start_time
# The print statement prints Overall runtime in hh:mm:ss format
# hours = int(tot_time / 3600))
# minutes = int(((tot_time % 3600) / 60))
# seconds = int(((tot_time % 3600) % 60))
print("\n** Total Elapsed Runtime:", tot_time, "in seconds.")
print("\n** Total Elapsed Runtime:",
	str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
	+ str(int((tot_time%3600)%60)) )


# 2. Command Line Arguments

# a module that makes it easy to write user-friendly command line interfaces for command line arguments
import argparse

# Creates Argument Parser object named parser
parser = argparse.ArgumentParser()

# Argument 1: that'sd a path to a folder
parser.add_argument('--dir', type=str, default='my_folder/', 
	help='path to folder of images')

# Argument 2: that's a integer
parser.add_argument('--num', type = int, default = 1,
                       help = 'Number (integer) input')

# Assigns variable args to parse_args()
args = parser.parse_args()

# Accesses values of Arguments 1 and 2 by printng them
print("Argument 1:", args .dir, " Argument 2:", args .num)





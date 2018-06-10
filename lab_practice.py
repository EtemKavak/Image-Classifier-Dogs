

########### 1. Imports python modules ##########

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


############ 2. Command Line Arguments ##########

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


########## 3. Creating Pet Image Labels ##########

# 3.1 Reading files from a folder

# import only the listdir function from OS
from os import listdir

# retrieve the filenames from folder pet_images/
filename_list = listdir("pet_images/")

print("\nPrints 10 filenames from folder pet_images/")

for idx in range(0,10,1):
	print("%2d file: %-25s" % (idx + 1, filename_list[idx]))

# 3.2 Dictionary for pet image filenames and labels

# create empty dict named pet_dic
pet_dic = dict() 

# determines number of items in dict
items_in_dic = len(pet_dic)
print("\nEmpty Dictionary pet_dic - n items=", items_in_dic)

# add key_value pairs to dictotionary ONLY when key doesn't already exist
keys = ["beagle_0239.jpg", "Boston_terrier_02259.jpg"]
values = ["beagle", "boston terrier"]

for idx in range(0, len(keys), 1):
	if keys[idx] not in pet_dic:
		pet_dic[keys[idx]] = values[idx]
	else:
		print("** Warning: Key=", keys[idx],
			"already exists in pet_dict pet_dic:")

# iterating through a dict printing all keys & their associated values
print("\n Printing all key-value pairs in dict pet_dic")
for key in pet_dic:
	print("key=", key, "  Value=", pet_dic[key])

# 3.3 Creating pet image labels from filenames

"""
lower() -- places letters in lower case only
split() -- returns a list of words from a string ( delimiter or whitespace)
strip() -- returns string with leading & trailing characters removed
isalpha() -- returns true only when string contains only alphabetic characters, returns false otherwise
"""

# set pet_image variable to a filename
pet_image = "Boston_terrier_02259.jpg"

# set string to lower case letters
low_pet_image = pet_image.lower()

# splits lower case string by _ to break into words
word_list_pet_image = low_pet_image.split("_")

# create pet_name starting as empty string
pet_name = ""

# loop to check if word in pet name is only alphabetic characters and append

for word in word_list_pet_image:
	if word.isalpha():
		pet_name += word + " "

# strip off starting/trailing witespace characters
pet_name = pet_name.strip()

# print resulting pet_name
print("\nFilename =", pet_image, "   Label=", pet_name)

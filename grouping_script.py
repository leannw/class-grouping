# read the csv
# get list of filename, group pairs
# iterate the current folder
# for each file in the folder,
#   check if it exists in the list of pairs
#   if it does, (optionally create folder) and move to group folder

import csv
import os

with open('joined_species.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        filename = row[0] + '.jpg' #change ".jpg" if the image extention is different
        group = row[5] #if grouping by family

        try:
          os.mkdir(group)
        except OSError:
          1
          
          #script and CSV should be palced in same file as all the images
        os.rename(filename, group + '/' + filename)


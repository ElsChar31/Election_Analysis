# The data we must retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who receive votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

import csv
import os

# Assign a variable for the file to load and the path.

file_to_load = os.path.join("Resources 4", "election_results.csv")

# Assign a variable to save the file to a path.

file_to_load = os.path.join("analysis", "election_analysis")

# Open the election results and read the file.

with open(file_to_load) as election_data:

    file_reader = csv.reader(election data)


    #read and print the header row.
    
    headers  = next(file_reader)

    print(headers)

    # To do: read and analyze the data here.

    # Print the file object

    print(election_data)

# Close the file


# Create a filename variable to a direct or indirect path to the file.

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.

open(file_to_save, "w")

    # Write some data to the file.

    txt_file.write("Hello World")

    #Write three counties to the file.

        txt_file.write("Arapahoe\nDenver\nJefferson")

# Add our dependencies

import csv

import os

#Assign a variable to load a file from a path.



        

        

#Close the file

outfile.close()
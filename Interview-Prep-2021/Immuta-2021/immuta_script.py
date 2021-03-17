#!/usr/bin/env python
"""
This script answers Question 4 and proposes solutions to Question 5 for the Immuta technical assesment.
Python version 3.5.9 was used to create and run this script.
"""

__author__ = "Yingquan Li"
__date__ = "3/16/21"
__contact__ = "yli12313@umd.edu"
__version__ = "1.0.0"

##########################
## Base Code (Provided) ##
##########################
import requests                 ## PLEASE GET THIS LIBRARY TO RUN SCRIPT
import pprint                   ## PLEASE GET THIS LIBRARY TO RUN SCRIPT
from collections import Counter ## PLEASE GET THIS LIBRARY TO RUN SCRIPT

session = requests.Session()
base_url = "https://umd-2.trial.immutacloud.com" # PLEASE UPDATE TO YOUR base_url TO RUN SCRIPT
api_key = "19e7b54844d043e6948c18f2365f0e68"     # PLEASE UPDATE TO YOUR api_key TO RUN SCRIPT
response = session.post(base_url + "/bim/apikey/authenticate", data = {"apikey": api_key})
auth_token = response.json()["token"] 
session.headers["Authorization"] = "Bearer {}".format(auth_token)

###########################################################################
## 4. Now use the API to programatically answer the following questions: ##
###########################################################################

######################################################
##   a. How many data sources are in your instance? ## 
######################################################

endpoint = "/dataSource"
DATA_SOURCES_FOUND = int(session.get(base_url + endpoint).json()["count"])
print("There are: " + str(DATA_SOURCES_FOUND) + " data sources.\n")

#################################################################
##   b. How many columns have tags on them?                    ##
##   c. What is the tag that has been most frequently applied? ##
#################################################################

# Define variables needed
TAGGED_COLUMNS = 0
TAGS = []

# Function needed
def return_metadata(endpoint):
	"""Returns the metadata per data source."""
	return session.get(base_url + endpoint).json()['metadata']

# Answering (b.): Finds the columns per individual Data Source that are tagged. Sum the number of tagged columns across 
# all data sources.
# Answering (c.): Find all column tags from all Data Sources, extracting the tag values. Find the most frequently 
# occuring column tag, it's frequency count and the top 10 most frequently occuring column tags.
for i in range(1, DATA_SOURCES_FOUND + 1):
	# Part (b.) logic
	returned = return_metadata('/dictionary/' + str(i))
	returned = [x for x in returned if 'tags' in x.keys()]
	TAGGED_COLUMNS += len(returned)

	# part (c.) logic
	tags = [val["tags"] for val in returned]
	for j in range(len(tags)):
		TAGS.extend([x['name'] for x in tags[j]])

# Print answer for (b.)
print("There are: " + str(TAGGED_COLUMNS) + " tagged columns that were found.\n")

# Print answer for (c.)
c = Counter(TAGS)
print("The most common tag is: " + c.most_common(1)[0][0] + ". The frequency of this tag is across all Data Sources is: " + str(c.most_common(1)[0][1]) + ".")
print()
pprint.pprint(c.most_common(10))

#################################################
## 5. Automation Ideas for Relational Database ##
#################################################
# 1) Make use of bash scripting and awk and sed command-line utility functions for data parsing.
# 2) Build a Python library that handles JSON parsing.
# 3) Explore alternative technologies: Perl, Spark, Scala, and COTS Software as a last resort after exhausting all 
#    efforts to automate and build interally.










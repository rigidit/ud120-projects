#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)
### 146 data points (people) in the dataset
print len(enron_data["SKILLING JEFFREY K"])
### 21 features are available for each person
pois = 0
for p in enron_data:
    if enron_data[p]["poi"]==1:
        pois = pois + 1
print pois
### 18 persons of interest are in database
print "PRENTICE JAMES", enron_data["PRENTICE JAMES"]["total_stock_value"]
### 1095040 is the total value of the stock belonging to James Prentice
print "COLWELL WESLEY", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
### 11 email messages do we have from Wesley Colwell to persons of interest
print "SKILLING JEFFREY K", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
### 19250000 - the value of stock options exercised by Jeffrey K Skilling

### Of these three individuals (Lay, Skilling and Fastow), who took home the most money?
for p in enron_data:
    if "LAY" in p:
        print p, enron_data[p]["total_payments"]
    if "SKILLING" in p:
        print p, enron_data[p]["total_payments"]
    if "FASTOW" in p:
        print p, enron_data[p]["total_payments"]
### LAY KENNETH L 103559793
### FASTOW ANDREW S 2424083
### SKILLING JEFFREY K 8682716
### LAY KENNETH took home the most money
quantified_salary = 0
known_email_address = 0
for p in enron_data:
    if not math.isnan(float(enron_data[p]["salary"])):
        quantified_salary = quantified_salary + 1
    if "NaN" not in enron_data[p]["email_address"]:
        known_email_address = known_email_address + 1
print "quantified_salary", quantified_salary
print "known_email_address", known_email_address
### quantified_salary 95
### known_email_address 111
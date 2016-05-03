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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print 'number of people: ' + str(len(enron_data))

print 'number of features: ' + str(len(enron_data.values()[0]))

print 'number of pois: ' + str(len({k: v for k, v in enron_data.iteritems() if v['poi'] == 1})) 

print 'James Prentices stocks value: ' + str(enron_data["PRENTICE JAMES"]["total_stock_value"])

print 'Wesley Colwell emails to POI: ' + str(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

print 'Jeffrey Skilling stocks value: ' + str(enron_data["SKILLING JEFFREY K"])

print 'Andrew Fastow total payments: ' + str(enron_data["FASTOW ANDREW S"]["total_payments"])

print 'Jeffrey Skilling total payments: ' + str(enron_data["SKILLING JEFFREY K"]["total_payments"])

print 'Kenneth Lay total payments: ' + str(enron_data["LAY KENNETH L"]["total_payments"])


salary = 0
email = 0
percentageTotalPaymentsFilled = 0
percentagePoiTotalPaymentsFilled = 0
numberOfPoi = 0

for k, v in enron_data.iteritems():
    if (enron_data[k]['salary'] == 'NaN'):
        salary += 1
    if (enron_data[k]['email_address'] == 'NaN'):
        email += 1
    if (enron_data[k]['total_payments'] == 'NaN'):
        percentageTotalPaymentsFilled += 1
    if (enron_data[k]['total_payments'] == 'NaN' and enron_data[k]['poi'] == 1):
        percentagePoiTotalPaymentsFilled += 1
    if (enron_data[k]['poi'] == 1):
        numberOfPoi += 1

print 'total people in dataset: ' + str(len(enron_data))
print 'total people with NaN for payment: ' + str(percentageTotalPaymentsFilled)
print 'number of poi: ' + str(numberOfPoi)

print 'total with salary defined: ' + str(len(enron_data) - salary)
print 'total with email defined: ' + str(len(enron_data) - email)    
        
percentageTotalPaymentsFilled = percentageTotalPaymentsFilled * 100 / float(len(enron_data))
print 'percentage with payments filled: ' + str(percentageTotalPaymentsFilled)

percentagePoiTotalPaymentsFilled = percentagePoiTotalPaymentsFilled * 100 / float(len(enron_data))
print 'percentage poi with payments filled: ' + str(percentagePoiTotalPaymentsFilled)






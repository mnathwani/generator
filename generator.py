#!/usr/bin/python

import sys
import time
import datetime
import random

from pytz import timezone


line_count = int(sys.argv[1])

timestr = time.strftime("%Y%m%d-%H%M%S")

f = open('./type_data_'+timestr+'.log','w')
 

# risk types

with open('risk_types.txt') as risk_types_file:
	risk_types = risk_types_file.read().splitlines()


# currency

with open('currency.txt') as currency_file:
	currency = currency_file.read().splitlines()


# resources

with open('resources.txt') as resources_file:
	resources = resources_file.read().splitlines()


# time buckets

with open('time_buckets.txt') as time_buckets_file:
	time_buckets = time_buckets_file.read().splitlines()


# codes

with open('codes.txt') as codes_file:
	codes = codes_file.read().splitlines()


# requests

with open('requests.txt') as requests_file:
	requests = requests_file.read().splitlines()


event_time = datetime.datetime(2013,10,10).replace(tzinfo=timezone('UTC'))
 

for i in range(0,line_count):
	increment = datetime.timedelta(seconds=random.randint(30,300))
	event_time += increment
	ccy = random.choice(currency)
	risk_type = random.choice(risk_types)
	tenor = random.choice(time_buckets)
	code = random.choice(codes)
	request= random.choice(requests)
	f.write('[%s],%s,%s,%s,%s\n' % (event_time.strftime('%d/%b/%Y'),risk_type,ccy,tenor,random.randint(2000,5000)))

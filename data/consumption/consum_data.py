import csv
import sys
import os
from django.core.wsgi import get_wsgi_application
from decimal import Decimal
import datetime

file_path = '/home/dilmac/development/gastestenv/gas/smap-coding-challenge/dashboard'
print(file_path, ' The path')
sys.path.append(file_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dashboard.settings")

application = get_wsgi_application()

import django

# django.setup()

from consumption.models import Consumption

data = csv.reader(open('/home/dilmac/development/gastestenv/gas/smap-coding-challenge/data/consumption/3000.csv'), delimiter=',')

for row in data:
	if row[0] != 'create_date_time':
		consum = Consumption()
		consum.create_date_time = row[0]
		consum.consumption = row[1]
		consum.save()
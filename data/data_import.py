# from __future__ import unicode_literals

import django
import csv
import os, sys



# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dashboard.settings")

# from django.conf import settings
from django.core.management import setup_environ
import settings
setup_environ(settings)

from dashboard.consumption import models

print  Consumption.objects.get(pk=1)
# file = ('user_data.csv')


# con_obj = Consumption.objects.all()

# for obj in con_obj:
# 	print(obj)

# with open(file) as csv_file:

# 	csv_reader = csv.reader(csv_file, delimiter=',')

# 	for row in csv_reader:
# 		print(row)



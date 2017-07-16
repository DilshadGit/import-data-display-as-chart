import django
import csv


fiel = ('../data/user_data.csv')

csv_file = open(file)
csv_reader = csv.reader(csv_file,delimiter=',')

for row in csv_reader:
	print(row)

csv_file.close()
# if __name__ == "__main__":
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dashboard.settings")
#     from django.core.management import execute_from_command_line

#     execute_from_command_line(sys.argv)
#     from dashboard import settings
#     from .consumption.models import Consumptions

#     cons = Consumptions.objects.get().all(user_id, create_date_time, consumption)
#     for con in cons:
#     	print(con.user_data.csv, con.create_date_time, con.consumption)
#     	print('==='* 20)

#     fiels = ('data/user_data.csv')

# def process_exception(exception, row):
# 	import traceback
# 	import sys

# 	exc_info = sys.exc_info()
# 	print "######################## Exception #############################"
# 	print '\n'.join(traceback.format_exception(*(exc_info or sys.exc_info())))
# 	print row
# 	print "################################################################"

if __name__ == "__main__":
	django.setup()

	for file in fiels:
		csv_file = open(file, 'rU')
		reader = csv.DictReader(csv_file)

	for field in reader.fieldnames:
		print field




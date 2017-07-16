# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from .models import Consumption

from rest_framework.views import APIView
from rest_framework.response import Response


User = get_user_model()

def home(request):
	context = {}
	return render(request, 'layout.html', context)

def summary(request):
	consumptions = Consumption.objects.all()
	total = 0
	for x in consumptions:
		total += x.consumption
	
	# print total, ' Total'

	
	context = {
	  'message': 'Hello!',
	  'consumptions': consumptions,
	  'total': total,
	}
	return render(request, 'consumption/summary.html', context)

def detail(request):
	

	context = {
		'message': 'Details'
	}
	return render(request, 'consumption/detail.html', context)


def get_data_from_store(request, *args, **kwargs):
	data = {
		'sales': 100,
		'customers': 10,
	}
	return JsonResponse(data)


class ChartData(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        """
        	Return a list of all users.
        """

        qs_count = User.objects.all().count()
        con_count = Consumption.objects.all().count()
        print(con_count, ' <<<')
        consumptions = Consumption.objects.all()
        total = 0
        avg = 0
        for x in consumptions:
        	total += x.consumption
        	avg = total / con_count
        print(avg)

        labels = ["Users", "Consumption", "Total", "Avg"]
        default_items = [qs_count, con_count, total, avg, con_count]
        data = {
			'labels': labels,
			'default': default_items,
			'Users': qs_count,
			'Consumption': con_count,
			'Totel': total,
			'Avg': avg,
		}
        return Response(data)
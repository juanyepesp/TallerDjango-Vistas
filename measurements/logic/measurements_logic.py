import json
from django.contrib.postgres import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from ..models import Measurement


def get_measurements():
    measurements = Measurement.objects.all()
    return measurements


def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement


def update_measurement(var_pk, new_var):
    measurement = get_measurement(var_pk)
    measurement.value = new_var["value"]
    measurement.unit = new_var["unit"]
    measurement.place = new_var["place"]
    measurement.save()
    return measurement


def create_measurement(var):
    measurement = Measurement(value=var["value"], place=var["place"], unit=var["unit"])
    measurement.save()
    return measurement


def delete_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    measurement.delete()
    return measurement

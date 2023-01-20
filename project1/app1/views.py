from urllib import request
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

#Test (not related to assignment)
from re import template
from django.http import HttpResponse
from django.template import loader

# Just for viewing datasets
##Not feasible to implement when the dataset is very big
#class DataSetViewSet(viewsets.ModelViewSet):
#    queryset = DataSet.objects.all()
#    serializer_class = DataSetSerializer

class OrganismViewSet(viewsets.ModelViewSet):
    queryset = Organism.objects.all()
    serializer_class = OrganismSerializer

class PfamDesViewSet(viewsets.ModelViewSet):
    queryset = PfamDes.objects.all()
    serializer_class = PfamDesSerializer

class ProteinSeqViewSet(viewsets.ModelViewSet):
    queryset = ProteinSequence.objects.all()
    serializer_class = ProteinSeqSerializer

#Test (not related to assignment)
def testForm(request):
    template = loader.get_template('test.html')
    return HttpResponse(template.render())

def submitted(request):
    template = loader.get_template('submitted.html')
    return HttpResponse(template.render())

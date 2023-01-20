from django.contrib import admin
from .models import *

# list of models
dataModel = [ProteinSequence, PfamDes, Organism, DataSet]
# Register models
admin.site.register(dataModel)

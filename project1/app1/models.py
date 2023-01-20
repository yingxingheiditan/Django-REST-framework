from django.db import models

# Create your models here.

class ProteinSequence(models.Model):
    protein = models.CharField(max_length=50, null=False, blank=False, unique=True)
    sequence = models.CharField(max_length=500)

class PfamDes(models.Model):
    domain = models.CharField(max_length=50, null=False, blank=False, unique=True)
    domain_des = models.CharField(max_length=255)

class Organism(models.Model):
    organism = models.IntegerField(null=False, blank=False, unique=True)
    organism_clade = models.CharField(max_length=50, null=False, blank=False)
    organism_name = models.CharField(max_length=255, null=False, blank=False)

class DataSet(models.Model):
    protein = models.ForeignKey(ProteinSequence, to_field="protein", on_delete=models.CASCADE)
    organism = models.ForeignKey(Organism, to_field="organism", on_delete=models.CASCADE)
    domain = models.ForeignKey(PfamDes, to_field="domain", on_delete=models.CASCADE)
    domain_start = models.IntegerField()
    domain_end = models.IntegerField()
    protein_length = models.IntegerField()
    
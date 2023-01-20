import factory
from django.test import TestCase
from django.conf import settings
from django.core.files import File
from random import randint, choice

from .models import *

class ProteinSeqFactory(factory.django.DjangoModelFactory):
    #dummy data
    protein = "A0A016S8J7"
    sequence = "MVIGVGFLLVLFSSSVLGILNAGVQLRIEELFDTPGHTNNWAVLVCTSRFWFNYRHVSNVLALYHTVKRLGIPDSNIILMLAEDVPCNPRNPRPEAAVLSA"

    class Meta:
        model = ProteinSequence

class PfamDesFactory(factory.django.DjangoModelFactory):
    #dummy data
    domain = "PF01650"
    domain_des = "PeptidaseC13family"

    class Meta:
        model = PfamDes

class OrganismFactory(factory.django.DjangoModelFactory):
    #dummy data
    organism = 53326
    organism_clade = "E"
    organism_name = "Ancylostoma ceylanicum"

    class Meta:
        model = Organism

class DataSetFactory(factory.django.DjangoModelFactory):
    #dummy data
    domain_start = randint(1, 100000)
    domain_end = domain_start+randint(1, 100000)
    protein_length = randint(100, 100000)
    protein = factory.SubFactory(ProteinSeqFactory)
    domain = factory.SubFactory(PfamDesFactory)
    organism = factory.SubFactory(OrganismFactory)

    class Meta:
        model = DataSet

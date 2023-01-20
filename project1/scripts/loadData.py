import os
import sys
import django
import csv
from collections import defaultdict

sys.path.append(r'D:\topic1_files\topic1\assignment1\project1')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')
django.setup()

from app1.models import *

#ProteinSequence
data_file = r'D:\topic1_files\topic1\assignment1\project1\csvFiles\assignment_data_sequences.csv'
proteinSequence = defaultdict(list)

with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        proteinSequence[row[0]]=row[1]

ProteinSequence.objects.all().delete()

proteinSequence_row = {} 

for protein, sequence in proteinSequence.items():
    row = ProteinSequence.objects.create(protein=protein, sequence=sequence)
    row.save()
    proteinSequence_row[protein] = row

#pFamDes
data_file = r'D:\topic1_files\topic1\assignment1\project1\csvFiles\pfam_descriptions.csv'
pfamDescriptions = defaultdict(list)

with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        pfamDescriptions[row[0]]=row[1]

PfamDes.objects.all().delete()

pfamDescriptions_row = {} 

for domain, domain_des in pfamDescriptions.items():
    row = PfamDes.objects.create(domain=domain, domain_des=domain_des)
    row.save()
    pfamDescriptions_row[domain] = row
    
#Organism and DataSet
data_file = r'D:\topic1_files\topic1\assignment1\project1\csvFiles\assignment_data_set.csv'
organismList = defaultdict(list)
rowList = defaultdict(list)

with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    rowIndex = 0
    for row in csv_reader:
        organismList[row[1]]={"clade":row[2],"name":row[3]}
        rowList[rowIndex]={"protein":row[0],"organism":row[1],"domain":row[5],"domain_start":row[6], "domain_end":row[7],"protein_length":row[8]}
        rowIndex +=1

Organism.objects.all().delete()
DataSet.objects.all().delete()

organismList_row = {} 

for organism, organism_value in organismList.items():
    row = Organism.objects.create(organism=organism, organism_clade=organism_value["clade"],organism_name=organism_value["name"])
    row.save()
    organismList_row[organism] = row

for i, row_data in rowList.items():
    try:
        proteinSequence_row[row_data["protein"]]
    except KeyError:
        proteinRowToSave = ProteinSequence.objects.create(protein=row_data["protein"], sequence='')
        proteinRowToSave.save()
        proteinSequence_row[row_data["protein"]] = proteinRowToSave
    try:
        pfamDescriptions_row[row_data["domain"]]
    except KeyError:
        pfamRowToSave = PfamDes.objects.create(domain=row_data["domain"], doman_des='')
        pfamRowToSave.save()
        pfamDescriptions_row[row_data["domain"]] = pfamRowToSave
    row = DataSet.objects.create(protein=proteinSequence_row[row_data["protein"]], organism=organismList_row[row_data["organism"]], domain=pfamDescriptions_row[row_data["domain"]], domain_start=row_data["domain_start"], domain_end=row_data["domain_end"], protein_length=row_data["protein_length"])
    row.save()

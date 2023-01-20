from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

##########################dataset_detail##########################
#view by protein_id
@api_view(['GET'])
def view_dataset_detail(request, pk):
    try:
        dataset = DataSet.objects.filter(protein=pk)
    except DataSet.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = DataSetSerializer(dataset, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def post_dataset_detail(request):
    serializer = DataSetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#update & delete by row id
@api_view(['POST', 'GET'])
def update_dataset_detail(request, pk):
    try:
        dataset = DataSet.objects.get(id=pk)
    except DataSet.DoesNotExist:
        return HttpResponse(status=404)
    serializer = DataSetSerializer(instance=dataset,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', 'GET'])
def delete_dataset_detail(request, pk):
    try:
        dataset = DataSet.objects.get(id=pk)
    except DataSet.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = DataSetSerializer(dataset)
        return Response(serializer.data)
    if request.method == 'DELETE':
        dataset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##########################proteinsequence_detail##########################
@api_view(['GET'])
def view_proteinseq_detail(request, pk):
    try:
        proteinseq = ProteinSequence.objects.get(protein=pk)
    except ProteinSequence.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ProteinSeqSerializer(proteinseq)
        return Response(serializer.data)

@api_view(['POST'])
def post_proteinseq_detail(request):
    serializer = ProteinSeqSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
def update_proteinseq_detail(request, pk):
    try:
        proteinseq = ProteinSequence.objects.get(id=pk)
    except ProteinSequence.DoesNotExist:
        return HttpResponse(status=404)
    serializer = ProteinSeqSerializer(instance=proteinseq,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', 'GET'])
def delete_proteinseq_detail(request, pk):
    try:
        proteinseq = ProteinSequence.objects.get(id=pk)
    except ProteinSequence.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ProteinSeqSerializer(proteinseq)
        return Response(serializer.data)
    if request.method == 'DELETE':
        proteinseq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##########################pfam_detail##########################
@api_view(['GET'])
def view_pfam_detail(request, pk):
    try:
        pfam = PfamDes.objects.get(domain=pk)
    except PfamDes.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = PfamDesSerializer(pfam)
        return Response(serializer.data)

@api_view(['POST'])
def post_pfam_detail(request):
    serializer = PfamDesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
def update_pfam_detail(request, pk):
    try:
        pfam = PfamDes.objects.get(id=pk)
    except PfamDes.DoesNotExist:
        return HttpResponse(status=404)
    serializer = PfamDesSerializer(instance=pfam,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', 'GET'])
def delete_pfam_detail(request, pk):
    try:
        pfam = PfamDes.objects.get(id=pk)
    except PfamDes.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = PfamDesSerializer(pfam)
        return Response(serializer.data)
    if request.method == 'DELETE':
        pfam.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##########################organism_detail##########################
@api_view(['GET'])
def view_organism_detail(request, pk):
    try:
        organism = Organism.objects.get(organism=pk)
    except Organism.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = OrganismSerializer(organism)
        return Response(serializer.data)

@api_view(['POST'])
def post_organism_detail(request):
    serializer = OrganismSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
def update_organism_detail(request, pk):
    try:
        organism = Organism.objects.get(id=pk)
    except Organism.DoesNotExist:
        return HttpResponse(status=404)
    serializer = OrganismSerializer(instance=organism,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', 'GET'])
def delete_organism_detail(request, pk):
    try:
        organism = Organism.objects.get(id=pk)
    except Organism.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = OrganismSerializer(organism)
        return Response(serializer.data)
    if request.method == 'DELETE':
        organism.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##########################views from coursera example##########################
#view list of all proteins for a given organism
@api_view(['GET'])
def protein_organism_detail(request, pk):
    try:
        dataset = DataSet.objects.filter(organism=pk)
    except DataSet.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        
        serializer = ProteinOrganismSerializer(dataset, many=True)
        
        return Response(serializer.data)

#view list of all domains in all the proteins for a given organism
@api_view(['GET'])
def domain_organism_detail(request, pk):
    try:
        dataset = DataSet.objects.filter(organism=pk)
    except DataSet.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        print(DomainOrganismSerializer(dataset, many=True).data)
        
        serializer = DomainOrganismSerializer(dataset, many=True)
        
        return Response(serializer.data)

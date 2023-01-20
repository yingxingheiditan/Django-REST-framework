from rest_framework import serializers
from .models import *

class ProteinSeqSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ProteinSequence
        fields = ['id', 'protein', 'sequence']

class PfamDesSerializer(serializers.ModelSerializer):
    class Meta:
        model =  PfamDes
        fields = ['id', 'domain', 'domain_des']

class OrganismSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Organism
        fields = ['id', 'organism', 'organism_clade', 'organism_name']

class DataSetSerializer(serializers.ModelSerializer):
    protein = ProteinSeqSerializer(read_only=True)
    organism = OrganismSerializer(read_only=True)
    domain = PfamDesSerializer(read_only=True)
    
    class Meta:
        model =  DataSet
        fields = ['id', 'protein', 'organism', 'domain', 'domain_start', 'domain_end', 'protein_length']

    def create(self, validated_data):
        protein_data = self.initial_data.get('protein')
        organism_data = self.initial_data.get('organism')
        domain_data = self.initial_data.get('domain')
        dataset = DataSet(**{**validated_data,
                        'protein': ProteinSequence.objects.get(protein=protein_data['protein']),
                        'organism': Organism.objects.get(organism=organism_data['organism']),
                        'domain': PfamDes.objects.get(domain=domain_data['domain']),
                        })
        dataset.save()
        return dataset

#To view coursera examples
class ProteinOrganismSerializer(serializers.ModelSerializer):

    class Meta:
        model =  DataSet
        fields = ['id', 'organism_id', 'protein_id']

class DomainOrganismSerializer(serializers.ModelSerializer):
    domain = PfamDesSerializer()

    class Meta:
        model =  DataSet
        fields = ['id', 'domain']

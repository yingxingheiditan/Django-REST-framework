import json
from urllib import response
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from .model_factories import *
from .serializers import *

##########################dataset_test##########################
class DataSetSerializerTest(APITestCase):
    dataset = None
    datasetserialiser = None

    def setUp(self):
        self.dataset = DataSetFactory.create(pk=1, protein_id='A0A016S8J7')
        self.datasetserialiser = DataSetSerializer(instance=self.dataset)

    def tearDown(self):
        ProteinSequence.objects.all().delete()
        PfamDes.objects.all().delete()
        Organism.objects.all().delete()
        DataSet.objects.all().delete()
        ProteinSeqFactory.reset_sequence(0)
        PfamDesFactory.reset_sequence(0)
        OrganismFactory.reset_sequence(0)
        DataSetFactory.reset_sequence(0)
    
    def test_datasetSerializer(self):
        data = self.datasetserialiser.data
        self.assertEqual(set(data.keys()), set(['id', 'protein', 'organism', 'domain', 'domain_start', 'domain_end', 'protein_length']))

    #Test for foreign key attributes (need to locate to the respective 2nd set)
    def test_datasetSerializerProteinSeqForeignKey(self):
        data = self.datasetserialiser.data
        protein_data = data['protein']
        self.assertEqual(set(protein_data.keys()), set(['id', 'protein', 'sequence']))
    
    def test_datasetSerializerOrganismForeignKey(self):
        data = self.datasetserialiser.data
        protein_data = data['organism']
        self.assertEqual(set(protein_data.keys()), set(['id', 'organism', 'organism_clade', 'organism_name']))

    def test_datasetSerializerPfamDesForeignKey(self):
        data = self.datasetserialiser.data
        protein_data = data['domain']
        self.assertEqual(set(protein_data.keys()), set(['id', 'domain', 'domain_des']))


class DataSetTest(APITestCase):
    dataset = None
    good_url = ''
    bad_url = ''
    delete_url = ''

    def setUp(self):
        self.dataset = DataSetFactory.create(protein_id='A0A016S8J7')
        self.good_url = reverse('dataset_api', kwargs={'pk': 'A0A016S8J7'})
        self.bad_url = 'api/protein/ABC/'
        self.delete_url = reverse('dataset-delete', kwargs={'pk': 1})

    #after testing, return database to the same state
    def tearDown(self):
        ProteinSequence.objects.all().delete()
        PfamDes.objects.all().delete()
        Organism.objects.all().delete()
        DataSet.objects.all().delete()
        ProteinSeqFactory.reset_sequence(0)
        PfamDesFactory.reset_sequence(0)
        OrganismFactory.reset_sequence(0)
        DataSetFactory.reset_sequence(0)

    def test_dataSetDetailReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
        #check if data is correct
        data = json.loads(response.content)
        #data is a list containing a dict, to get the nested dict containing the protein 'id':
        protein_data = data[0].get('protein')
        self.assertTrue('protein' in protein_data)
        self.assertEqual(protein_data['protein'], 'A0A016S8J7')

    def test_dataSetDetailReturnFailOnBadPk(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)
    
    def test_dataSetDetailDeleteIsSuccessful(self):
        response = self.client.delete(self.delete_url, format='json')
        self.assertEqual(response.status_code, 204)

##########################proteinseq_test##########################
class ProteinSeqSerializerTest(APITestCase):
    proteinseq = None
    proteinseqserialiser = None

    def setUp(self):
        self.proteinseq = ProteinSeqFactory.create(pk=1, protein='A0A456CF04')
        self.proteinseqserialiser = ProteinSeqSerializer(instance=self.proteinseq)

    def tearDown(self):
        ProteinSequence.objects.all().delete()
        ProteinSeqFactory.reset_sequence(0)
    
    def test_proteinSeqSerializer(self):
        data = self.proteinseqserialiser.data
        self.assertEqual(set(data.keys()), set(['id', 'protein', 'sequence']))

class ProteinSeqTest(APITestCase):
    proteinseq = None
    good_url = ''
    bad_url = ''
    delete_url = ''

    def setUp(self):
        #created random new protein seq: A0A456CF04
        self.proteinseq = ProteinSeqFactory.create(pk=1, protein='A0A456CF04')
        self.good_url = reverse('proteinseq_api', kwargs={'pk': 'A0A456CF04'})
        self.bad_url = 'api/proteinseq/ABC/'
        self.delete_url = reverse('proteinseq-delete', kwargs={'pk': 1})

    #after testing, return database to the same state
    def tearDown(self):
        ProteinSequence.objects.all().delete()
        ProteinSeqFactory.reset_sequence(0)

    def test_proteinSeqDetailReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
        #check if data is correct
        data = json.loads(response.content)
        self.assertTrue('protein' in data)
        self.assertEqual(data['protein'], 'A0A456CF04')
    
    def test_proteinSeqDetailReturnFailOnBadPk(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)
    
    def test_proteinSeqDetailDeleteIsSuccessful(self):
        response = self.client.delete(self.delete_url, format='json')
        self.assertEqual(response.status_code, 204)
    
##########################pfam_test##########################
class PfamDesSerializerTest(APITestCase):
    pfam = None
    pfamserialiser = None

    def setUp(self):
        #create new random domain: PF12345
        self.pfam = PfamDesFactory.create(pk=1, domain='PF12345')
        self.pfamserialiser = PfamDesSerializer(instance=self.pfam)

    def tearDown(self):
        PfamDes.objects.all().delete()
        PfamDesFactory.reset_sequence(0)
    
    def test_pfamDesSerializer(self):
        data = self.pfamserialiser.data
        self.assertEqual(set(data.keys()), set(['id', 'domain', 'domain_des']))

class PfamDesTest(APITestCase):
    pfam = None
    good_url = ''
    bad_url = ''
    delete_url = ''

    def setUp(self):
        #create new random domain: PF12345
        self.pfam = PfamDesFactory.create(pk=1, domain='PF12345')
        self.good_url = reverse('pfam_api', kwargs={'pk': 'PF12345'})
        self.bad_url = 'api/pfam/1/'
        self.delete_url = reverse('pfam-delete', kwargs={'pk': 1})

    #after testing, return database to the same state
    def tearDown(self):
        PfamDes.objects.all().delete()
        PfamDesFactory.reset_sequence(0)

    def test_pfamDesDetailReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
        #check if data is correct
        data = json.loads(response.content)
        self.assertTrue('domain' in data)
        self.assertEqual(data['domain'], 'PF12345')
    
    def test_pfamDesDetailReturnFailOnBadPk(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)
    
    def test_pfamDesDetailDeleteIsSuccessful(self):
        response = self.client.delete(self.delete_url, format='json')
        self.assertEqual(response.status_code, 204)

##########################organism_test##########################
class OrganismSerializerTest(APITestCase):
    organism = None
    organismserialiser = None

    def setUp(self):
        #create new random organism: 54321
        self.organism = OrganismFactory.create(pk=1, organism=54321)
        self.organismserialiser = OrganismSerializer(instance=self.organism)

    def tearDown(self):
        Organism.objects.all().delete()
        OrganismFactory.reset_sequence(0)
    
    def test_organismSerializer(self):
        data = self.organismserialiser.data
        self.assertEqual(set(data.keys()), set(['id', 'organism', 'organism_clade', 'organism_name']))

class PfamDesTest(APITestCase):
    organism = None
    good_url = ''
    bad_url = ''
    delete_url = ''

    def setUp(self):
        #create new random organism: 54321
        self.organism = OrganismFactory.create(pk=1, organism='54321')
        self.good_url = reverse('organism_api', kwargs={'pk': '54321'})
        self.bad_url = 'api/organism/ABD/'
        self.delete_url = reverse('organism-delete', kwargs={'pk': 1})

    #after testing, return database to the same state
    def tearDown(self):
        Organism.objects.all().delete()
        OrganismFactory.reset_sequence(0)

    def test_organismDetailReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
        #check if data is correct
        data = json.loads(response.content)
        self.assertTrue('organism' in data)
        self.assertEqual(data['organism'], 54321)
    
    def test_organismDetailReturnFailOnBadPk(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)
    
    def test_organismDetailDeleteIsSuccessful(self):
        response = self.client.delete(self.delete_url, format='json')
        self.assertEqual(response.status_code, 204)

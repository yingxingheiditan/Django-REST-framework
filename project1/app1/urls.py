from django.urls import include, path
from rest_framework import routers
from .import views
from . import api

router = routers.DefaultRouter()
#router.register(r'datasets', views.DataSetViewSet)
router.register(r'proteinsequenceset', views.ProteinSeqViewSet)
router.register(r'pfamdesset', views.PfamDesViewSet)
router.register(r'organismset', views.OrganismViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='restframework')),
    #dataset
    path('api/protein/<str:pk>', api.view_dataset_detail, name='dataset_api'),
    path('dataset-post/', api.post_dataset_detail, name='dataset-post'),
    path('dataset-update/<int:pk>', api.update_dataset_detail, name='dataset-update'),
    path('dataset-delete/<int:pk>', api.delete_dataset_detail, name='dataset-delete'),
    #proteinsequence
    path('api/proteinseq/<str:pk>', api.view_proteinseq_detail, name='proteinseq_api'),
    path('proteinseq-post/', api.post_proteinseq_detail, name='proteinseq-post'),
    path('proteinseq-update/<int:pk>', api.update_proteinseq_detail, name='proteinseq-update'),
    path('proteinseq-delete/<int:pk>', api.delete_proteinseq_detail, name='proteinseq-delete'),
    #pfam/domain
    path('api/pfam/<str:pk>', api.view_pfam_detail, name='pfam_api'),
    path('pfam-post/', api.post_pfam_detail, name='pfam-post'),
    path('pfam-update/<int:pk>', api.update_pfam_detail, name='pfam-update'),
    path('pfam-delete/<int:pk>', api.delete_pfam_detail, name='pfam-delete'),
    #organism
    path('api/organism/<int:pk>', api.view_organism_detail, name='organism_api'),
    path('organism-post/', api.post_organism_detail, name='organism-post'),
    path('organism-update/<int:pk>', api.update_organism_detail, name='organism-update'),
    path('organism-delete/<int:pk>', api.delete_organism_detail, name='organism-delete'),
    #other api views (from example in coursera)
    path('api/proteins/<int:pk>', api.protein_organism_detail),
    path('api/pfams/<int:pk>', api.domain_organism_detail),
    #test (not related to assignment)
    path('test/', views.testForm, name='testForm'),
    path('submitted/', views.submitted, name='submitted'),
]

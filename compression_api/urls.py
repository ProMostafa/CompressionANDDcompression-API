from django.urls import path ,include
from .import views
from rest_framework.routers import DefaultRouter
router =DefaultRouter()
router.register('list-files',views.List_Files_viewset,basename='list-files')
#router.register('Compression',views.Compression,basename='compression')


urlpatterns = [
    path('api-viewset',include(router.urls)),
    path('compression-data/',views.Compression,name='compression-data'),
    #path('delete',views.delete,name='delete'), for test
    path('decompression-data/',views.DeCompression,name='decompression-data'),
    path('delete-list-data/',views.Remove_List_Data,name='delete-list-data'),
    path('Compression-API/',views.api_root,name='action'),
    path('call-viewset/',views.call_viewset,name='call-viewset')
]

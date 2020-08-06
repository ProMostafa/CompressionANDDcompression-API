
from django.contrib import admin
from django.urls import path ,include
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view
from compression_api import views

API_TITLE = "Compression && DeCompression-API"
API_DESCRIPTION = "API That Using To Compressions Files and Dwonload It , And DeCompressions Files And Show Extracing Files"

schema_view=get_swagger_view(title=API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('compression_api.urls')),
    path('docs/',include_docs_urls(title=API_TITLE,description=API_DESCRIPTION)),
    path('swagger-docs/',schema_view)
]
# this function call once when server run 
# Delete Temporary files , compression , decompression file from server after 1 day 
views.Delete_Temporary_After_Every_Day()

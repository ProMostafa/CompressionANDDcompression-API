import os, time, sys
import zipfile
import random
import shutil
from datetime import datetime
from threading import Timer
from django.shortcuts import render ,redirect
from django.http import FileResponse ,HttpResponse
from rest_framework import viewsets ,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from .models import File
from .serializers import FileSerializer

# Create your views here.
#file_code = 1
#flag=True
class List_Files_viewset(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer


# Aftre compression all uploading data remove from model
def Compression(request):
    files=File.objects.all()
    file_code=random.randint(0,100)
    path="dwonload/files"+str(file_code)+".zip"
    with zipfile.ZipFile(path,"w",compression=zipfile.ZIP_DEFLATED) as compress_files:
        for file in files:
            compress_files.write(file.file.path)
        respose=FileResponse(open(path,'rb'))
    File.objects.all().delete()
    #file_code+=1
    return respose

# Decompression files and then ( extract in client device ) Need User interaction forntend design 
# but for now it show extract file  in API
def DeCompression(request):
    files=File.objects.all()
    path="Extractall_Files"
    for file in files:
        with zipfile.ZipFile(file.file.path, 'r') as zip_ref:
            zip_ref.extractall(path)
    File.objects.all().delete()
    for root, directories, files_ex in os.walk(path, topdown=False):
        for name in files_ex:
            #print(os.path.join(root,name))
            if "." in name:
                """
                print("file =-------------------{}".format(root+"\\"+name))
                print("name=---------------{}".format(name))
                print("size ----------={}".format(os.path.getsize(root+"\\"+name)))
                """
                instance=File.objects.create(file=(root+"\\"+name),name=name,size=os.path.getsize(root+"\\"+name))
                instance.save()
        for name in directories:
            if "." in name:
                instance=File.objects.create(file=(root+"\\"+name),name=name,size=os.path.getsize(root+"\\"+name))
                instance.save()

    return HttpResponse("Done Extracting All Files , Go to List-Data Url to show Extracting Files")
    #return redirect("http://127.0.0.1:8000/api-viewset")

def call_viewset(request):
   return redirect("http://127.0.0.1:8000/api-viewset")
    

# create endpoint for compression & decopression functions
@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'List-Data':reverse("call-viewset",request=request,format=format),
        'Compression-Data':reverse('compression-data',request=request,format=format),
        'DeCompression-Data':reverse('decompression-data',request=request,format=format),
        'Remove-List-Data':reverse('delete-list-data',request=request,format=format),
    })


# delete Compression file && uploading data every day
def Delete_Temporary_After_Every_Day():
    print("-----------initialization Server Directory--------------------")
    from_=datetime.today()
    to_=from_.replace(day=from_.day+1, hour=1, minute=0, second=0, microsecond=0)
    interval=to_- from_

    secs=interval.seconds+1
    #for test work correctly 
    #secs=180 

    def delete():
        print("-----------Removing Temporary Files From Server --------------------")
        path1 = r"E:\python\Django\Django Rest API\Excerices\DataCompression_API\dwonload"
        path2 = r'E:\python\Django\Django Rest API\Excerices\DataCompression_API\media'
        path3 = r'E:\python\Django\Django Rest API\Excerices\DataCompression_API\Extractall_Files'
        # if api no using decompression funtion Extractall_Files not creating, and rasing error when delete it (not effect on API Function)
        try:
            for f in os.listdir(path1):
                os.remove(os.path.join(path1, f))
            for f in os.listdir(path2):
                os.remove(os.path.join(path2, f))
            shutil.rmtree(path3)
        except Exception as identifier:
            pass
        
    t = Timer(secs, delete)
    t.start()

# used it function when decompression file and then upload new files
def Remove_List_Data(request):
    File.objects.all().delete()
    return HttpResponse("Delete All Files in List-data")

"""
# For Test Delete Files
def delete(request):
    #file_code=1
    path1 = r"E:\python\Django\Django Rest API\Excerices\DataCompression_API\dwonload"
    path2 = r'E:\python\Django\Django Rest API\Excerices\DataCompression_API\media'
    path3 = r'E:\python\Django\Django Rest API\Excerices\DataCompression_API\Extractall_Files'
    for f in os.listdir(path1):
        os.remove(os.path.join(path1, f))
    for f in os.listdir(path2):
        os.remove(os.path.join(path2, f))
    shutil.rmtree(path3)
    return HttpResponse('Delete All Temporary Files')
"""

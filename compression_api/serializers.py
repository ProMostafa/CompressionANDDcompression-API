from rest_framework import serializers

from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file','name','size')
        extra_kwargs={'name':{'read_only':True},
        'size':{'read_only':True}
        }

    def create(self,validation_data):
        create_file=File.objects.create(file=validation_data['file'],
        name=validation_data['file'].name,
        size=validation_data['file'].size
        )
        return create_file


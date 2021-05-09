from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from .models import  Apartments,complaint_section, bill,  MyImage, User

class Apartmentserializer(serializers.ModelSerializer):
    class Meta:
        model = Apartments
        fields = '__all__'


class Reportserializer(serializers.ModelSerializer):
    class Meta:
        model = complaint_section
        fields = '__all__'

class Paybillserializer(serializers.ModelSerializer):
    class Meta:
        model = bill
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyImage
        fields = '__all__'


"""class MyImageModelSerializer(serializers.ModelSerializers):
      image=Base64ImageField()
      class meta:
         model=MyImageModel
         fields= ('data','image')
      def create(self, validated_data):
        image=validated_data.pop('image')
        data=validated_data.pop('data')
       return MyImageModel.objects.create(data=data,image=image)"""

def decode_base64_file(data):
    def get_file_extension(file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

    from django.core.files.base import ContentFile
    import base64
    import six
    import uuid

    # Check if this is a base64 string
    if isinstance(data, six.string_types):
        # Check if the base64 string is in the "data:" format
        if 'data:' in data and ';base64,' in data:
            # Break out the header from the base64 content
            header, data = data.split(';base64,')

        # Try to decode the file. Return validation error if it fails.
        try:
            decoded_file = base64.b64decode(data)
        except TypeError:
            TypeError('invalid_image')

        # Generate file name:
        file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
        # Get the file name extension:
        file_extension = get_file_extension(file_name, decoded_file)

        complete_file_name = "%s.%s" % (file_name, file_extension, )

        return ContentFile(decoded_file, name=complete_file_name)
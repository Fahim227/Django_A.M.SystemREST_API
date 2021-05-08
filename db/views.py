from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from . models import User, Apartments, MyImage
from .serializers import Apartmentserializer,Reportserializer, Paybillserializer, imageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
import json, base64
import magic
from django.core.files.base import ContentFile
from rest_framework import serializers


def home(request):
    return render(request, 'ourproject/home.html')

  
# @api_view(['POST'])
def show_flatsInJson(request):
  allapartments=Apartments.objects.all()
  serializer = Apa(allapartments, many=True)
  return JsonResponse(serializer.data, safe=False)
# Add Flat for rent

@api_view(['POST'])
def trial(request):
  res = {}
  """img = request.data.get("img")
  myimage = MyImage(model_pic=decode_base64_file(img))
  myimage.save()"""
  request.data._mutable = True
  request.data["img"] = decode_base64_file(request.data.get("img"))
  request.data._mutable = False
  print(request.data)
  serializer = imageSerializer(data=request.data)
  if serializer.is_valid():
        serializer.save()
        res = {
          'response' : True,
          'message' : "Saved Successfully"
        }
  else:
      print(serializer.errors)
  
  res_json = json.dumps(res)
  return HttpResponse(res_json)

@api_view(['POST'])
def insert_Apartment_info(request):
  print(request.data.get('owner_id'))
  user = User.objects.only('id').get(id = request.data.get('owner_id'))
  id = request.data.get('owner_id')
  apartment_info = Apartments(owner_id=user,flat_number=request.data.get('flat_number'), building_name=request.data.get('building_name'), building_number=request.data.get('building_numb'), building_address=request.data.get('building_address'), flat_size=request.data.get('flat_size'), num_of_beds=request.data.get('num_of_beds'), num_of_toilet=request.data.get('num_of_toilet'), num_of_balcony=request.data.get('num_of_balcony'), map_address=request.data.get('map_address'), location=request.data.get('location'), price=request.data.get('price'),img=decode_base64_file(request.data.get("img")))
    
  apartment_info.save()
  res = {
          'response' : True,
          'message' : "Saved Successfully"
    }
  res_json = json.dumps(res)
  return HttpResponse(res_json)


@api_view(['POST'])
def insert_Report(request):
  print(request.data)
  serializer = Reportserializer(data=request.data)
  res = {}
  if serializer.is_valid():
    serializer.save()
    res = {
          'response' : True,
          'message' : "Saved Successfully"
    }
  else:
    print(serializer.errors)
    res = {
          'response' : False,
          'message' : "not saved"
    }
  res_json = json.dumps(res)
  return HttpResponse(res_json)

@api_view(['POST'])
def getOwnedFlats(request):
    id = request.data.get('id')
    print(id)
    flats= Apartmentserializer(Apartments.objects.filter(owner_id=id), many=True)
    print(len(flats.data))
    return HttpResponse(json.dumps(flats.data))


@api_view(['POST'])
def insert_bill(request):
  print(request.data)
  serializer = Paybillserializer(data=request.data)
  res = {}
  if serializer.is_valid():
    serializer.save()
    res = {
          'response' : True,
          'message' : "Saved Successfully"
    }
  else:
    print(serializer.errors)
    res = {
          'response' : False,
          'message' : "not saved"
    }
  res_json = json.dumps(res)
  return HttpResponse(res_json)

@api_view(['POST', 'GET'])
def show_flats(request):
  if request.method=='POST':
    location=request.data.get('location')
    print(location)
    location_based_apartments =  Apartmentserializer(Apartments.objects.filter(location=location), many=True)
    print(len(location_based_apartments.data))
    return HttpResponse(json.dumps(location_based_apartments.data))
  elif request.method=='GET':
    apartment = Apartmentserializer(Apartments.objects.all(), many=True)
    print(len(apartment.data))
    return HttpResponse(json.dumps(apartment.data))





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

"""
def insert_user_info(request):
  #  AppartmentId=User(request.GET['apartment_id'])
    UserInfo = User(first_name=request.POST.get('FirstName'), last_name=request.POST.get(
        'LastName'), phone_number=request.POST.get('PhoneNumber'), user_type=request.POST.get('UserType'))
    UserInfo.save()

    return HttpResponse("Congratulations!You are successfully registered to Nagorik Seba")




def show_flats(request):
  if request.method=='POST':
      # location_search=request.POST.get('location')
      # ampobj=Apartments.objects.filter(location=request.post.get('location')
      location=Apartments.objects.filter(location=request.POST['location'])
      contxt = { 'Flats' : location } 
      return render(request,'flats_info.html', contxt)
  else:
      flats_info=Apartments.objects.all()
      print=flats_info
      return render(request, "ourproject/flats_info.html", {'Flats': flats_info})




def insert_complaint_section_info(request):
    if request.method == 'POST':
        complaint_sectionInfo=complaint_section(user_id=request.POST.get(UserId'),title=request.POST.get('Title'),description=request.POST.get('Description'),home_address=request.POST.get('HomeAddress'),police_station=request.POST.get('PoliceStation'))
        complaint_sectionInfo.save()
        return HttpResponse("Your complaint has been recieved")
     else:
       return render(request,'OurProject/complaint_section.html')

def insert_user_info(request):
  #  AppartmentId=User(request.GET['apartment_id'])
    UserInfo=User(first_name=request.POST.get('FirstName'),last_name=request.POST.get('LastName'),phone_number=request.POST.get('PhoneNumber'),user_type=request.POST.get('UserType'))
    UserInfo.save()
    return HttpResponse("Congratulations!You are successfully registered to Nagorik Seba")


   
def insert_Apartment_info(request):
     if request.method == 'POST':
       ApartmentInfo=Apartments(flat_number=request.POST.get('FlatNumber'),building_name=request.POST.get('BuildingName'),building_number=request.POST.get('BuildingNumber'),building_address=request.POST.get('BuildingAddress'),flat_size=request.POST.get('FlatSize'),num_of_beds=request.POST.get('NumOfBeds'),num_of_toilet=request.POST.get('NumOfToilet'),num_of_balcony=request.POST.get('NumOfBalcony'),map_address=request.POST.get('MapAddress'),location=request.POST.get('Location'))
       ApartmentInfo.save()
       return HttpResponse("Your Apartment Profile is updated")
     else:
       return render(request,'OurProject/apartment.html')


"""

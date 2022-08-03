from dis import show_code
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialization import CountriesSerializer,StatesSerializer,CititesSerializer
from .models import Countries,States,Cities
import pandas as pd
from django.forms.models import model_to_dict
import json


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category' : '/search'
    }
    
    return Response(api_urls)
# Create your views here.

@api_view(['GET'])
def getCountries(request):
    '''
    country_data = pd.read_csv('countries.csv')
    data = {}
    for index,row in country_data.iterrows():
        data = row.to_dict()
        newData = {
            "country_id": data["id"],
            "name": data["name"],
            "iso3": data["iso3"],
            "iso2": data["iso2"],
            "numeric_code": data["numeric_code"],
            "phone_code": data["phone_code"],
            "capital": data["capital"],
            "currency": data["currency"],
            "currency_name": data["currency_name"],
            "currency_symbol": data["currency_symbol"],
            "tld": data["tld"],
            "native": data["native"],
            "region": data["region"],
            "subregion": data["subregion"],
            "latitude": data["latitude"],
            "longitude": data["longitude"],
            "emoji": data["emoji"],
            "emojiU":data["emojiU"]
        }
        addData = CountriesSerializer(data=newData)
        if addData.is_valid():
            addData.save()
        print(addData)
    return Response("Countries Data Stored in database Successfully")
    '''
    #print(country_data)
    countries = Countries.objects.all()
   
    data = CountriesSerializer(data = countries,many=True)
    data.is_valid()
    return Response(data.data)
    

@api_view(['GET'])
def loadCities(request):
    city_data = pd.read_csv('cities.csv')
    data = {}
    for index,rows in city_data.iterrows():
        data = rows.to_dict()

        newData = {
            "city_id": data["id"],
            "name": data["name"],
            "state_id": data["state_id"],
            "state_code": data["state_code"],
            "state_name": data["state_name"],
            "country_id": data["country_id"],
            "country_code": data["country_code"],
            "country_name": data["country_name"],
            "latitude": data["latitude"],
            "longitude": data["longitude"],
            "wikiDataId": data["wikiDataId"]
        }

        addData = CititesSerializer(data=newData)
        if addData.is_valid():
            addData.save()
        print(newData["city_id"])
    return Response("Cities Data saved successfully in Database")

@api_view(['GET'])
def loadStates(request):
    state_data = pd.read_csv('states.csv')
    data = {}
    for index,rows in state_data.iterrows():
        data = rows.to_dict()

        newData = {
            "state_id": data["id"],
            "name": data["name"],
            "country_id": data["country_id"],
            "country_code": data["country_code"],
            "country_name": data["country_name"],
            "state_code": data["state_code"],
            "latitute": data["latitude"],
            "longitude": data["longitude"],
           
        }

        addData = StatesSerializer(data=newData)
        if addData.is_valid():
            addData.save()
        print(newData["state_id"],index)
    return Response("States Data saved successfully in Database")

@api_view(['GET'])
def getCities(request):
    cities = Cities.objects.all()
    city_data = CititesSerializer(data = cities,many=True)
    city_data.is_valid()

    return Response(city_data.data)

@api_view(['GET'])
def getStates(request):
    states = states.objects.all()
    state_data = StatesSerializer(data = states,many=True)
    state_data.is_valid()

    return Response(state_data.data)

@api_view(['GET'])
def getCityForState(request,state):
    allCities = Cities.objects.filter(state_code = state).order_by('city_id')
    data = CititesSerializer(data = allCities,many=True)
    data.is_valid()

    return Response(data.data)

@api_view(['GET'])
def getStateForCountry(request,country):
    allStates = States.objects.filter(country_code = country).order_by('country_id')
    data = StatesSerializer(data = allStates,many=True)
    data.is_valid()

    return Response(data.data)
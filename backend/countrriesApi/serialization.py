from rest_framework import serializers
from .models import Countries,States,Cities

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ("id","country_id","name","iso3","iso2","numeric_code","phone_code","capital","currency","currency_name","currency_symbol","tld","native","region","subregion","latitude","longitude","emoji","emojiU")

class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ("state_id","name","country_id","country_code","country_name","state_code","latitute","longitude")


class CititesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ("city_id","name","state_id","state_code","state_name","country_id","country_code","country_name","latitude","longitude","wikiDataId")

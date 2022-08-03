from django.urls import path
from yaml import load
from . import views
urlpatterns  = [
    path('',views.ApiOverview,name="home"),

    #--Uploading data from csv to sqlite database --
    path('country/',views.getCountries,name="country"),
    path('loadCities/',views.loadCities,name="loadCities"),
    path('getCities/',views.getCities,name="loadCities"),
    path('loadStates/',views.loadStates,name="loadStates"),
    path('getStates/',views.getStates,name="getStates"),
    #--Uploading data from csv to sqlite database --

    path('city/<str:state>',views.getCityForState,name="getCityForState"),
    path('state/<str:country>',views.getStateForCountry,name="getStateForState"),
]
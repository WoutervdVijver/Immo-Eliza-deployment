import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim




subtypes = [
        'APARTMENT_BLOCK',
        'BUNGALOW',
        'CASTLE',
        'CHALET',
        'COUNTRY_COTTAGE',
        'EXCEPTIONAL_PROPERTY',
        'FARMHOUSE',
        'HOUSE',
        'MANOR_HOUSE',
        'MANSION',
        'MIXED_USE_BUILDING',
        'OTHER_PROPERTY',
        'TOWN_HOUSE',
        'VILLA']

condition_types = [
    'AS_NEW', 
    'GOOD', 
    'JUST_RENOVATED',
    'TO_BE_DONE_UP', 
    'TO_RENOVATE', 
    'TO_RESTORE', 
    'HYPER_EQUIPPED',
]  
kitchen_types = [
       'INSTALLED', 
       'NOT_INSTALLED', 
       'SEMI_EQUIPPED', 
       'USA_HYPER_EQUIPPED',
       'USA_INSTALLED', 
       'USA_SEMI_EQUIPPED', 
       'USA_UNINSTALLED',
 ] 



class Preprocess:
    '''
    Class that performs all the cleaning necessary. It initializes two dictionaries:
    
    :param self.obj: which is the raw data from the website
    :pram self.dict: represent the cleaned data after running clean_all()
    '''

    def __init__(self, obj):
        self.obj = obj
        self.dict = {
            'Surface_log': 0.0,
            'Living_log': 0.0,
            'Number of bedrooms': 0
        }
        for type in subtypes:
            self.dict[type] = 0
        self.dict['Pool'] = 0

        self.dict['latitude'] = 0.0
        self.dict['longitude'] = 0.0
        
        for type in condition_types:
            self.dict[type] = 0
        for type in kitchen_types:
            self.dict[type] = 0
        
        self.dict['Furnished'] = 0
        self.dict['Open fireplace'] = 0
        self.dict['Terrace'] = 0
        self.dict['Garden'] = 0
        


    def clean_all(self):
        '''
        Function that cleans all the the data from self.obj of the Preprocess class
        and puts the cleaned data into a dictionary self.dict


        '''
        self.dict['Living_log'] = [self.clean_log('Living area')]
        self.dict['Surface_log'] = [self.clean_log('Surface land area')]
        self.dict['Number of bedrooms'] = [self.clean_number_of_bedrooms()]

        self.clean_location()

        self.clean_type('Property subtype')
        self.clean_type('Kitchen')
        self.clean_type('Condition')

        self.clean_bool('Pool')   
        self.clean_bool('Furnished')
        self.clean_bool('Open fireplace')
        self.clean_bool('Terrace')
        self.clean_bool('Garden')


    def clean_log(self, col: str) -> float:
        '''
        Function that returns the natural log of the col that has been entered

        :param col: str that represent the column in the dataframe that needs to be transformed
        '''
        value = float(self.obj[col])
        if value>0:
            return np.log(value)
        else:
            raise ValueError()

    def clean_number_of_bedrooms(self) -> float:
        '''
        Function that returns the number of bedrooms from a dictionary
        '''
        value = float(self.obj['Number of bedrooms'])
        return  value

    def clean_bool(self, col:str) -> int:
        '''
        Function that retrieves the wether a certain type is present in col and sets the related value in self.dict to 1.

        :param col: str that represent the column in the dataframe that needs to be transformed
        '''
        value = int(self.obj[col])
        if value == 1:
            self.dict[col] = 1
        
    def clean_location(self):
        '''
        Function that returns the latitude and longitude from the location
        '''
        value = self.obj['Location']
        geolocator = Nominatim(user_agent="my_app")
        location = geolocator.geocode(value + ' Belgique')
        if location:
            self.dict['longitude'] = location.longitude
            self.dict['latitude'] = location.latitude
        else:
            raise ValueError()

    def clean_type(self, col: str):
        '''
        Function that updates one of the columns in the self.dict depending on the subtype
        '''
        value = self.obj[col]
        if value in subtypes+kitchen_types+condition_types:
            self.dict[value] = 1
        else:
            raise ValueError()

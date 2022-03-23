from django.test import SimpleTestCase
from django.test import TestCase, Client
from django.urls import reverse, resolve
from business_game.views import *
from business_game.models import *
from business_game.forms import *
import json



#class Test_Forms(SimpleTestCase): 
#    def test_businessform_valid(self):
#        form = BusinessForm(data={
#            'businessName': "apple",
#            'CEOName': "Tim cook",
#            'productName': "iphone",
#            'startingLocation': "london"
#        })       
#        self.assertTrue(form.is_valid())


class Test_Views(TestCase):
    
    def test_index_GET_request(self):
        client = Client()
        response = client.get(reverse('index'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "business_app/index.html")
        
    def test_business_page_GET_request(self):
        client = Client()
        response = client.get(reverse('business_page'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "business_app/business_page.html")
    
    
    def test_business_creation_page_GET_request(self):
        client = Client()
        response = client.get(reverse('business_creation_page'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "business_app/business_creation_page.html")
    
    def test_location_page_london_GET_request(self):
        client = Client()
        response = client.get(reverse('location_page_london'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "business_app/location_page_london.html")
    
    def test_location_page_glasgow_GET_request(self):
        client = Client()
        response = client.get(reverse('location_page_glasgow'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "business_app/location_page_glasgow.html")
        



class Test_Urls(SimpleTestCase):
    
    def test_index_is_resolved(self):
        url=reverse('index')
        self.assertEquals(resolve(url).func, index)
    
    def test_business_page_is_resolved(self):
        url=reverse('business_page')
        self.assertEquals(resolve(url).func, business_page)
    
    def test_business_creation_page_is_resolved(self):
        url=reverse('business_creation_page')
        self.assertEquals(resolve(url).func, business_creation_page)
    
    def test_location_page_london_is_resolved(self):
        url=reverse('location_page_london')
        self.assertEquals(resolve(url).func, location_page_london)
    
    def test_location_page_glasgow_is_resolved(self):
        url=reverse('location_page_glasgow')
        self.assertEquals(resolve(url).func, location_page_glasgow)
        
   
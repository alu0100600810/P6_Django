from django.http import HttpResponse
from django.shortcuts import render

#from django.shortcuts import render_to_response
 
def home(request): 
  return render(request,'home.html') 


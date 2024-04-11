from django import forms # type:ignore
import requests
from dotenv import load_dotenv # type:ignore
load_dotenv()
import os


class MyForm(forms.Form):
  url=f'http://{os.getenv("BackendHost")}:{os.getenv("BackendPort")}/signUp'
  name = forms.CharField(label="Your Name")
  username=forms.CharField(label="Username")
  email = forms.EmailField(label="Email Address")
  password = forms.CharField(widget=forms.PasswordInput)

  # You can add validation rules here (optional)
  def clean_message(self):
    data = self.cleaned_data['message']
    
    return data
  def signUp(self,data, params=None):
    response = requests.post(self.url,json=data, params=params)
    response.raise_for_status()  # Raise an exception for non-2xx status codes
    return response.json()  # Assuming the response is in JSON format
  
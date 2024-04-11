from django.shortcuts import render, redirect,HttpResponseRedirect # type: ignore
from handleRequests.userRequests.forms.signUp import MyForm

def form_view(request):
    
    return redirect('signUp_view')
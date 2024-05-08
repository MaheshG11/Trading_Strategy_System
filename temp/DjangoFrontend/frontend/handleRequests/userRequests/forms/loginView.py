from django.shortcuts import render, redirect,HttpResponseRedirect # type: ignore
from handleRequests.userRequests.forms.login import MyForm
from django.contrib import messages
from django.contrib.auth import login
def login_view(request):
  if request.method == 'POST':
    form = MyForm(request.POST)
    if form.is_valid():
      # Process the form data here (e.g., save to database, send email)
      email = form.cleaned_data['email']
      password=form.cleaned_data['password']
      data={
        'email':email,
        'password':password
        }
      
      try:
        print(data)
        user=form.login(data=data)
        if(user!=None):
          login(request,user)
        else:
            redirect('signUp_view')
        
      except:
        print("failed\nfailed\nfailed\n")
      # Redirect to a success page or display a confirmation message
      return redirect('login_view')
  else:
    form = MyForm()

  context = {'form': form}
  return render(request, 'form.html', context) 

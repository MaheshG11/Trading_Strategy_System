from django.shortcuts import render, redirect,HttpResponseRedirect # type: ignore
from handleRequests.userRequests.forms.signUp import MyForm
from django.contrib import messages

def signUp_view(request):
  if request.method == 'POST':
    form = MyForm(request.POST)
    if form.is_valid():
      # Process the form data here (e.g., save to database, send email)
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      username = form.cleaned_data['username']
      password=form.cleaned_data['password']
      data={
        'name':name,
        'email':email,
        'username':username,
        'password':password
        }
      
      try:
        print(data)
        res=form.signUp(data=data)
        if(res['success']==0):
          messages.info(request,res['message'])
        
      except:
        print("failed\nfailed\nfailed\n")
      # Redirect to a success page or display a confirmation message
      return redirect('signUp_view')
  else:
    form = MyForm()

  context = {'form': form}
  return render(request, 'form.html', context) 

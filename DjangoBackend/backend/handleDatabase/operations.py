import os
import pymongo # type:ignore
from django.http import HttpResponse   # type:ignore
from dotenv import load_dotenv   # type:ignore
from django.conf import settings   # type:ignore
from rest_framework.decorators import api_view   # type:ignore
from rest_framework.response import Response   # type:ignore
from handleDatabase.operation.userOperations import userOperation
load_dotenv() 


#connect_string = 'mongodb+srv://<username>:<password>@<atlas cluster>/<myFirstDatabase>?retryWrites=true&w=majority'
connect_string=f'mongodb://{os.getenv("DatabaseHost")}:{os.getenv("DatabasePort")}/?directConnection=true'
my_client = pymongo.MongoClient(connect_string)
userdb=my_client["users"]
userscollection=userdb["users"]
print(type(userscollection))
ops=userOperation(db=userscollection)



@api_view(['POST'])
def signUp(request):
  username=request.data['username']
  name=request.data['name']
  password=request.data['password']
  email=request.data['email']
  try:
    data=ops.signUp(username=username,name=name,email=email,password=password)
  except:
    print('the except condition')
 
  return Response(data)


@api_view(["GET"])
def login(request):
  if(request.method=='GET'):
    password=request.data['password']
    email=request.data['email']
    try:
      data=ops.login(email=email,password=password)
    except:
      print('the except condition')
    try:
          return Response(data,content_type="application/json")
    except Exception as e:
          # Handle the exception
          print(f"An error occurred: {e}")
          return Response({"error": str(e)}, status=500,content_type="application/json") 


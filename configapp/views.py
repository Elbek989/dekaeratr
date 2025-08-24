import json
from rest_framework.views import APIView
from rest_framework.views import Response
class HELLO(APIView):
    def get(self,request):
        with open('ggg.json', 'r') as f:
            data = json.load(f)
        return Response(data=data)
    def post(self,request):
        name=request.data["name"]
        context={
            "response":f"salom {name}"
        }
        return Response(data=context)
# Create your views here.

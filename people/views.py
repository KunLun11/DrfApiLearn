from rest_framework import generics
from .models import Women
from .serializers import WomenSerializer


# class WomenAPIView(generics.ListAPIView):
#    queryset = Women.objects.all()
#    serializer_class = WomenSerializer


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()  #Здесь как будто выбираем все записи, но на самом деле будет всего одна
    serializer_class = WomenSerializer


class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

#class WomenAPIView(APIView):
#    def get(self, request):
#        w = Women.objects.all()
#        return Response({"posts": WomenSerializer(w, many=True).data})

#    def post(self, request):
#        serializer = WomenSerializer(data=request.data)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()

#        return Response({"post": serializer.data})

#    def put(self, request, *args, **kwargs):
#        pk = kwargs.get("pk", None)
#        if not pk:
#            return Response({"error": "Method PUT not allowed"})

#        try:
#            instance = Women.objects.get(pk=pk)
#        except:
#            return Response({"error": "Object does not exists"})

#        serializer = WomenSerializer(data=request.data, instance=instance)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response({"post": serializer.data})

#    def delete(self, request, *args, **kwargs):
#        pk = kwargs.get("pk", None)
#        if not pk:
#            return Response({"error": "Method DELETE not allowed"})

#        return Response({"post": "delete post" + str(pk)})




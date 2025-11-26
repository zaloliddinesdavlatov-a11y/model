
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


#class BookListApiView(generics.ListAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
class BookListApiView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data)

#class BookCreateApiView(generics.CreateAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
class BookCreateApiView(APIView):
    def post(self,request):
        try:
            serializer=BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({"status":"Nimadur xatto ketdi"})
        except:
            return Response({"status":"Nimadur xatto ketdi"})

#class BookEditApiView(generics.UpdateAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
class BookEditApiView(APIView):
    def put(self,request,pk):
        books=Book.objects.get(id=pk)
        serializer=BookSerializer(books,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar":"boldi yangilandi","yangilangani":serializer.data})
        else:
            return  Response({"javob":"Edit qilinmadi"})

    def patch(self,request,pk):
        books=Book.objects.get(id=pk)
        serializer=BookSerializer(books,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar":"boldi yangilandi","yangilangani":serializer.data})
        else:
            return  Response({"javob":"Edit qilinmadi"})


#class BookDeleteApiView(generics.DestroyAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
class BookDeleteApiView(APIView):
    def delete(self, request,pk):
        books=Book.objects.get(id=pk)
        books.delete()
        return Response({"xabar":"kitob ochirildi"})



#class BookDetailApiView(generics.RetrieveAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
class BookDetailApiView(APIView):
    def get(self,request,pk):
        try:
            books=Book.objects.get(id=pk)
            serializer=BookSerializer(books)
            return Response(serializer.data)
        except:
            return Response({"xabar":"bunday id-li kitob yuq mavjud emas"})

#class BookMixedApiView(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer

class BookMixedApiView(APIView):
    def get(self,request,pk):
        try:
            books=Book.objects.get(id=pk)
            serializer=BookSerializer(books)
            return Response(serializer.data)
        except:
            return Response({"xabar":"bunday id-li kitob yuq mavjud emas"})

    def put(self,request,pk):
        books=Book.objects.get(id=pk)
        serializer=BookSerializer(books,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar":"boldi yangilandi","yangilangani":serializer.data})
        else:
            return  Response({"javob":"Edit qilinmadi"})

    def patch(self,request,pk):
        books=Book.objects.get(id=pk)
        serializer=BookSerializer(books,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar":"boldi yangilandi","yangilangani":serializer.data})
        else:
            return  Response({"javob":"Edit qilinmadi"})


    def delete(self, request, pk):
        books = Book.objects.get(id=pk)
        books.delete()
        return Response({"xabar": "kitob ochirildi"})
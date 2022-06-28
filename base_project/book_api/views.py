# from pickle import TRUE
# from django.shortcuts import render
# from book_api.models import Book
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from book_api.serielizer import BookSerielizer



# # Create your views here.

# @api_view(['GET'])
# def book_list(request):
#     books = Book.objects.all() # Complex Data
#     serializer = BookSerielizer(books, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def book_create(request):
#     serielizer = BookSerielizer(data=request.data)
#     if serielizer.is_valid():
#         serielizer.save()
#         return Response(serielizer.data)
#     else:
#         return Response(serielizer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def book(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except:
#         return Response({
#             'error': 'Book does not exist'   
#         }, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = BookSerielizer(book)
#         return Response(serializer.data)

#     if request.method == "PUT":
#         serializer = BookSerielizer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == "DELETE":
#         book.delete()
#         return Response (status=status.HTTP_204_NO_CONTENT)
        



from rest_framework.views import APIView
from book_api.models import Book
from book_api.serielizer import BookSerializer
from rest_framework.response import Response
from rest_framework import status

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all() # Complex Data
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class BookCreate(APIView):
    def post(self, request):
        serielizer = BookSerializer(data=request.data)
        if serielizer.is_valid():
            serielizer.save()
            return Response(serielizer.data)
        else:
            return Response(serielizer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    def get_book_by_pk(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Book does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request , pk):
        book = self.get_book_by_pk(pk)
        book.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)



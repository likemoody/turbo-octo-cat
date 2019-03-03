from ..models import Post
from ..serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from toc.utils import QueryObjects


# class PostList(APIView):
#     def get(self, request, format=None):
#         posts = QueryObjects.query_posts(Post)
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             print(serializer.validated_data)
#             print(request.data)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PostSingle(APIView):
#     """
#     Retrieve, update or delete a post instance.
#     """
#
#     def get(self, request, pk, format=None):
#         snippet = QueryObjects.get_object(Post, pk)
#         serializer = PostSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = QueryObjects.get_object(Post, pk)
#         serializer = PostSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = QueryObjects.get_object(Post, pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class PostList(generics.ListCreateAPIView):
    queryset = QueryObjects.query_posts(Post)
    serializer_class = PostSerializer


class PostSingle(generics.RetrieveUpdateDestroyAPIView):
    queryset = QueryObjects.query_posts(Post)
    serializer_class = PostSerializer

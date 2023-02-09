from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from exclusive.models import Exclusive
from exclusive.serializers import ExclusiveDetailSerializer, ExclusiveListSerializer


class ExclusiveListView(APIView):
    """
    List all posts, or create a new post.
    """
    def get(self, request, format=None):
        posts = Exclusive.objects.all()
        serializer = ExclusiveListSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExclusiveListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExclusiveDetailView(APIView):
    """
    Retrieve, update or delete a post instance.
    """
    def get_object(self, pk):
        try:
            return Exclusive.objects.get(pk=pk)
        except Exclusive.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = ExclusiveDetailSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = ExclusiveDetailSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
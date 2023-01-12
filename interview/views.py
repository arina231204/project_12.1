from django.shortcuts import render
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination

from interview.models import Category, QuestionAnswer
from interview.serializers import CategorySerializer, DQuestionAnswerSerializer, QASerializer


class PostPagePagination(PageNumberPagination):
    page_size = 3

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    """
    API для List Category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return super().get_queryset()

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API для создания, удаления, изменения  Category
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    def perform_create(self, serializer):
        serializer.save()

class QuestionListCreateAPIView(generics.ListCreateAPIView):
    """
    API для List Category
    """
    queryset = QuestionAnswer.objects.all().order_by('-importance')
    serializer_class = QASerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['category', 'question']

class QuestionDetailDeleteUpdate(generics.RetrieveUpdateDestroyAPIView):
    """
    API для создания, удаления, изменения  Category
    """
    queryset = QuestionAnswer.objects.all()
    serializer_class = DQuestionAnswerSerializer

# class TweetViewSet(viewsets.ModelViewSet):ModelViewSet
#     """
#     API для List Category
#     """
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     pagination_class = PageNumberPagination
#     filter_backends = [DjangoFilterBackend,]
#     filterset_fields = ['category', ]
#
#     def get_queryset(self):
#         return super().get_queryset()




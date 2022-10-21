from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.


class ArticleView(APIView):

    def get(self, request):
        articles = Article.objects.all()
        articles_data = ArticleSerializer(articles, many=True)
        return Response((articles_data).data, status=status.HTTP_200_OK)

    def post(self, request):
        article = request.data
        article_data = ArticleSerializer(data=article)

        if article_data.is_valid():
            article_data.save()
            return Response({'message': 'Article created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Error in article data, check and try again'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        article_details = request.data
        try:
            article_details['id']
        except:
            # Update through title
            article_title = article_details['title']
            article = Article.objects.filter(title=article_title)
            if article.exists():
                article = article[0]
                serialized_article = ArticleSerializer(
                    article, data=article_details)
                if serialized_article.is_valid():
                    serialized_article.save()
                return Response({'message': 'Article update successfully'}, status=status.HTTP_200_OK)
            return Response({'message': 'Error in article data, check and try again'}, status=status.HTTP_400_BAD_REQUEST)
        # Update through id
        article = Article.objects.filter(id=article_details['id'])
        if article.exists():
            article = article[0]
            serialized_article = ArticleSerializer(
                article, data=article_details, partial=True)
            if serialized_article.is_valid():
                serialized_article.save()
            return Response({'message': 'Article update successfully'}, status=status.HTTP_200_OK)
        return Response({'message': 'Error in article data, check and try again'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        article = request.data
        try:
            article['id']
        except:
            # Update via title
            article_title = article['title']
            articles = Article.objects.filter(title=article_title)
            if articles.exists():
                article = articles[0]
                article.delete()
                return Response({'message': 'Delete successful'}, status=status.HTTP_200_OK)
            return Response({'message': 'No matching title'}, status=status.HTTP_400_BAD_REQUEST)
        # Update via id
        article_id = article['id']
        articles = Article.objects.filter(id=article_id)
        if articles.exists():
            article = articles[0]
            article.delete()
            return Response({'message': 'Delete successful'}, status=status.HTTP_200_OK)
        return Response({'message': 'No matching title'}, status=status.HTTP_400_BAD_REQUEST)

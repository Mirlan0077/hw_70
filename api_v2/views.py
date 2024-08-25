
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Article, Comment

from api_v2.serializers.article import ArticleSerializer

from api_v2.serializers.comment import CommentSerializer


@ensure_csrf_cookie
def get_csrf_token(request):
    if request.method == 'GET':
        return HttpResponse()
    else:
        return HttpResponseNotAllowed(permitted_methods=["GET"])


class ArticleView(APIView):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.order_by('-created_at')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        request_data = request.data.copy()
        request_data["test_id"] = 1  # Если нужно
        serializer = ArticleSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        article_data = ArticleSerializer(article).data
        return Response(article_data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(data=request.data, instance=article)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        article_data = ArticleSerializer(article).data
        return Response(article_data, status=status.HTTP_200_OK)

    def delete(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response({"id": pk}, status=status.HTTP_204_NO_CONTENT)

    def get(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)



class CommentView(APIView):

    def get(self, request, *args, article_id=None, pk=None, **kwargs):
        if pk:
            comment = get_object_or_404(Comment, pk=pk, article_id=article_id)
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            comments = Comment.objects.filter(article_id=article_id).order_by('-created_at')
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, article_id=None, **kwargs):
        request_data = request.data.copy()
        request_data['article_id'] = article_id
        serializer = CommentSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        comment_data = CommentSerializer(comment).data
        return Response(comment_data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, article_id=None, pk=None, **kwargs):
        comment = get_object_or_404(Comment, pk=pk, article_id=article_id)
        serializer = CommentSerializer(data=request.data, instance=comment, partial=True)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        comment_data = CommentSerializer(comment).data
        return Response(comment_data, status=status.HTTP_200_OK)

    def delete(self, request, *args, article_id=None, pk=None, **kwargs):
        comment = get_object_or_404(Comment, pk=pk, article_id=article_id)
        comment.delete()
        return Response({"id": pk}, status=status.HTTP_204_NO_CONTENT)

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from drf_spectacular.utils import extend_schema

from .models import Post
from .serializers import PostSerializer, PostCreateSerializer, PostUpdateSerializer
from .help_script import get_user_by_id, get_post_by_id


def index(request):
    """Show all posts on home page, and add new post"""
    if request.method == 'POST':

        user_id = request.POST.get('user_id')
        title = request.POST.get('title')
        body = request.POST.get('body')
        remote_user = get_user_by_id(user_id=user_id)
        if not remote_user:
            message = f'There are no user with id {user_id}'
            context = {'message': message}
            return render(request, 'contributes/index.html', context=context)

        elif remote_user:
            Post.objects.create(userId=user_id,
                                title=title,
                                body=body)

            return redirect('home')


    posts = Post.objects.all().order_by('userId')
    print(posts)
    context = {'posts': posts}
    return render(request, 'contributes/index.html', context=context)


def update_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        new_title = request.POST.get('new_title', post.title)
        new_body = request.POST.get('new_body', post.body)
        post.title = new_title
        post.body = new_body
        post.save()
        return redirect('home')

    return render(request, 'contributes/update.html')


def delete_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.delete()
        return redirect('home')
    return HttpResponse('Only POST method')


# API part
@extend_schema(responses=PostSerializer, description='Show all posts in local database')
@api_view(['GET'])
def posts_list_api(request):  # change name to "post_api"

    if request.method == 'GET':
        # get all posts from local db

        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


@extend_schema(request=PostCreateSerializer, responses=PostSerializer, description='Add new post if userId exists')
@api_view(['POST'])
def add_post_api(request):
    if request.method == 'POST':
        # add post with id validation
        request_user_id = request.data.get('userId') if request.data.get('userId') else None

        if not request_user_id:
            return Response(status=status.HTTP_404_NOT_FOUND, data='userId not provided')

        remote_user = get_user_by_id(endpoint='users', user_id=request_user_id)
        if remote_user:

            title = request.data.get('title', 'Title not provided')
            body = request.data.get('id', 'Body not provided')
            post, created = Post.objects.get_or_create(userId=request_user_id, defaults={'title': title, 'body': body})

            message = 'Post created successfully' if created else 'Post already exists'
            serializer = PostSerializer(post, many=False)
            context = {'message': message,
                       'post': serializer.data}
            return Response(status=status.HTTP_200_OK, data=context)

        else:
            context = {'message': f'There are no user with id #{request_user_id} /'
                                  f'or check input type, it should be integer.'}
            return Response(status=status.HTTP_404_NOT_FOUND, data=context)


@extend_schema(request=PostUpdateSerializer, responses=PostSerializer, description='Update post by using id')
@api_view(['PUT'])
def update_post_api(request, post_id):

    if request.method == 'PUT':
        post = get_object_or_404(Post, id=post_id)
        new_title = request.data.get('title', post.title)
        new_body = request.data.get('body', post.body)
        post.title = new_title
        post.body = new_body
        serializer = PostUpdateSerializer(post, many=False)
        post.save()
        return Response(status=status.HTTP_202_ACCEPTED, data=serializer.data)


@extend_schema(responses=PostSerializer, description="Detail post view")
@api_view(['GET', 'DELETE'])
def post_detail_api(request, post_id):

    if request.method == 'GET':

        try:
            # if object in local db
            post = Post.objects.get(id=post_id)
            serializer = PostSerializer(post, many=False)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        except ObjectDoesNotExist:
            post = get_post_by_id(post_id=post_id)

            if not post:
                return Response(status=status.HTTP_404_NOT_FOUND, data=f'There are no user id {post_id}')

            else:
                userId, id, title, body = post.values()
                post = Post.objects.create(userId=userId,
                                           id=id,
                                           title=title,
                                           body=body)
                post.save()

                serializer = PostSerializer(post, many=False)
                return Response(status=status.HTTP_201_CREATED, data=serializer.data)

    if request.method == 'DELETE':

        try:
            post = get_object_or_404(Post, id=post_id)
            post.delete()
            serializer = PostSerializer(post, many=False)
            return Response(status=status.HTTP_204_NO_CONTENT, data=f'DELETED: {serializer.data}')

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data=f'There are no post with id: {post_id}.')

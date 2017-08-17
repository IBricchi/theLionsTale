from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from article.models import ArticleInfo
from django.shortcuts import redirect
from django.core.files.base import ContentFile
import pathlib
from django.core.files.storage import default_storage
import os
from django.conf import settings
from django.core.files import File


def index(request):
    if request.user.is_authenticated():
        redirect_url = "./" + str(request.user.author_set.all().first().id)
    else:
        redirect_url = "login"
    return redirect(redirect_url)


def author(request, author_id):
    author = Author.objects.get(id=author_id)
    all_author_articles = author.articleinfo_set.all()
    author_with_rights = request.user.is_staff or author_id == str(request.user.author_set.all().first().id)
    context = {
        'author': author,
        'author_with_rights': author_with_rights,
        'all_author_articles': all_author_articles,
    }
    return render(request, 'author/author.html', context)


def profilePicChange(request):
    current_auth_id = request.POST.get("authorId")
    current_auth = Author.objects.get(id=current_auth_id)
    new_img = request.FILES.get("newProfileImg")

    temp_file_name = new_img.name
    temp_file = ContentFile(new_img.read())
    path = default_storage.save(
        'tmp/temp_' + str(current_auth_id) + pathlib.Path(temp_file_name).suffix, temp_file)
    temp_file = os.path.join(settings.MEDIA_ROOT, path)
    print(temp_file)

    with open(temp_file, 'rb') as f:
        temp_temp_loc = 'upload_' + str(current_auth_id) + pathlib.Path(f.name).suffix
        temp_temp_file = File(f)
        current_auth.profile_pic.save(temp_temp_loc, temp_temp_file, save=False)
    current_auth.save()

    os.remove('tmp/temp_' + str(current_auth_id) + pathlib.Path(temp_file_name).suffix)
    return redirect('authorIndex')


def descChange(request):
    current_auth_id = request.POST.get("authorId")
    current_auth = Author.objects.get(id=current_auth_id)
    new_desc = request.POST.get('newDesc')
    current_auth.description = new_desc
    current_auth.save()
    return redirect('authorIndex')
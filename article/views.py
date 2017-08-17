from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ArticleInfo, ArticleFiles
from author.models import Author
import json
from collections import OrderedDict
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os
from django.core.files import File
import pathlib


def index(request):
    all_authors = Author.objects.all()
    context = {
        'all_authors': all_authors,
    }
    return render(request, 'article/index.html', context)


def article(request, article_id):
    article_info = ArticleInfo.objects.get(id=article_id)
    article_content_json = json.loads(article_info.articlecontent_set.all()[0].content, object_pairs_hook=OrderedDict)
    context = {
        'article_info': article_info,
        'article_content_json': article_content_json,
    }
    return render(request, 'article/article.html', context)


def uploadDisp(request, user_key, stuff = "hello"):
    context = {
        'stuff': stuff,
    }
    return render(request, 'article/upload.html', context)


def upload(request, user_key):
    post_dic = request.POST.dict()
    files_dic = request.FILES.dict()

    out_author = Author.objects.get(name='Ignacio Bricchi')
    out_article_info = out_author.articleinfo_set.create(title=post_dic.get("title"))
    out_article_info.save()

    out_dic = OrderedDict()

    for i in range(0, int(post_dic.get("form_size"))):
        temp_key = str(i) + "_" + str(post_dic.get(str(i) + "_type"))
        temp_val = str(post_dic.get(str(i) + "_out"))

        if "file_image" in temp_key:
            temp_file = files_dic.get(str(i) + "_file")
            print(type(temp_file))

            temp_file_name = temp_file.name
            temp_file = ContentFile(temp_file.read())
            path = default_storage.save('tmp/temp_' + str(ArticleFiles.objects.count() + 1) + pathlib.Path(temp_file_name).suffix, temp_file)
            temp_file = os.path.join(settings.MEDIA_ROOT, path)
            print(temp_file)

            temp_article_file = out_article_info.articlefiles_set.create(description=temp_val)
            with open(temp_file, 'rb') as f:
                temp_temp_loc = 'upload_' + str(ArticleFiles.objects.count() + 1) + pathlib.Path(f.name).suffix
                temp_temp_file = File(f)
                temp_article_file.file.save(temp_temp_loc, temp_temp_file, save=False)
            temp_article_file.save()

            os.remove('tmp/temp_' + str(ArticleFiles.objects.count()) + pathlib.Path(temp_file_name).suffix)

            out_dic[temp_key] = [temp_val, temp_article_file.id]
        elif "link_image" in temp_key:
            out_dic[temp_key] = [temp_val]
        elif "text" in temp_key:
            temp_val_list = temp_val.splitlines()
            out_dic[temp_key] = [temp_val_list]

    out_json = json.dumps(out_dic, ensure_ascii=False)
    out_str = out_json.__str__()

    out_article_description = out_article_info.articlecontent_set.create(content=out_str)
    out_article_description.save()
    return redirect('../../../' + str(out_article_info.id))

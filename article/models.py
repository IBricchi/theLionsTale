from django.db import models

# Create your models here.


class ArticleInfo(models.Model):
    title = models.CharField(max_length=50, default="Title Missing")
    author = models.ForeignKey('author.Author', on_delete=models.CASCADE)

    def article_images_get(self, key):
        return self.articleimages_set.get(id=key)

    def __str__(self):
        return str(self.id) + ": " + self.title


class ArticleContent(models.Model):
    content = models.CharField(max_length=100000, default="Someone forgot to save or submit there work")
    linkedArticle = models.ForeignKey(ArticleInfo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ": " + self.content


class ArticleFiles(models.Model):
    description = models.CharField(max_length=500, default="image")
    file = models.FileField(upload_to="article/static/article/img/uploads/")
    linkedArticle = models.ForeignKey(ArticleInfo, on_delete=models.CASCADE)

    def static_url(self):
        try:
            output = self.file.url[self.file.url.index("static/") + 7:]
        except Exception:
            output = "article/img/fallbacks/no-img.jpg"
        return output

    def __str__(self):
        return str(self.id) + ": " + self.description

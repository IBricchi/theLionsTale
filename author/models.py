from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=30, default="Anonymous")
    description = models.CharField(max_length=1000, default="I'm a boring human with nothing to say about him/herself")
    profile_pic = models.FileField(upload_to="author/static/author/img/profile_pics/", default='author/static/author/img/profile_pics/no-image.jpg')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def static_url(self):
        try:
            output = self.profile_pic.url[self.profile_pic.url.index("static/") + 7:]
        except Exception:
            output = "author/img/profile_pics/no-image.jpg"
        return output

    def __str__(self):
        return self.name

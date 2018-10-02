from django.db import models

# Create your models here.
import datetime as dt

class User(models.Model):
    photo=models.ImageField()
    bio=models.TextField()




class Image(models.Model):
    image=models.ImageField(upload_to='picture/')
    name = models.CharField(max_length=40)
    description=models.TextField()
    user=models.ForeignKey(User, blank=True)
    likes=models.IntegerField(blank=True)



    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    @classmethod
    def delete_image_by_id(cls, id):
        pictures = cls.objects.filter(pk=id)
        pictures.delete()

    @classmethod
    def get_image_by_id(cls, id):
        pictures = cls.objects.get(pk=id)
        return pictures

    @classmethod
    def search_image(cls, search_term):
        pictures = cls.objects.filter(name__icontains=search_term)
        return pictures

    @classmethod
    def update_image(cls, id):
        pictures=cls.objects.filter(id=id).update(id=id)
        return pictures


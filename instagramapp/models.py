from django.db import models
from django.contrib.auth.models import User

# Create your models here.
import datetime as dt

class Profile(models.Model):
    class Meta:
        db_table = 'profile'

    bio = models.TextField(max_length=200, null=True, blank=True, default="bio")
    profilepic = models.ImageField(upload_to='picture/', null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True )
    followers = models.ManyToManyField(User, related_name="followers", blank=True)
    following = models.ManyToManyField(User, related_name="following", blank=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def follow_user(self, follower):
        return self.following.add(follower)

    def unfollow_user(self, to_unfollow):
        return self.following.remove(to_unfollow)

    def is_following(self, checkuser):
        return checkuser in self.following.all()

    def get_number_of_followers(self):
        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    def get_number_of_following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0

    @classmethod
    def search_users(cls, search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term)
        return profiles

    def __str__(self):
        return self.user.username


class Location(models.Model):
    name = models.CharField(max_length=30)


    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_tags(self):
        self.save()

    def delete_tags(self):
        self.delete()


class Image(models.Model):
    image=models.ImageField(upload_to='picture/')
    name = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    description=models.TextField()
    location=models.ForeignKey(Location, null=True)
    tags=models.ManyToManyField(tags, blank=True)
    likes=models.IntegerField(null=True)
    comments= models.TextField(blank=True)

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
    def filter_by_tag(cls, tags):
        pictures = cls.objects.filter(tags=tags)
        return pictures

    @classmethod
    def filter_by_location(cls, location):
        pictures = cls.objects.filter(location=location)
        return pictures

    @classmethod
    def search_image(cls, search_term):
        pictures = cls.objects.filter(name__icontains=search_term)
        return pictures

    @classmethod
    def update_image(cls, id):
        pictures=cls.objects.filter(id=id).update(id=id)
        return pictures

    @classmethod
    def update_description(cls, id):
        pictures = cls.objects.filter(id=id).update(id=id)
        return pictures

class Followers(models.Model):
    '''
    followers
    '''
    user = models.CharField(max_length=20, default="")
    follower = models.CharField(max_length=20, default="")


class Review(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="review")
    comment = models.TextField()

    def save_comment(self):
        self.save()

    def __str__(self):
        return self.comment
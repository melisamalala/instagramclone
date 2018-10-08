from django.test import TestCase

# Create your tests here.
from .models import Location, tags, Image, Review, Followers, User, Profile
from django.core.files.uploadedfile import SimpleUploadedFile


class tagsTestClass(TestCase):

    # Set up method the test for location and instantiating the location object

    def setUp(self):
        self.test_tags = tags(name='funny')
        self.test_tags.save()

        # Testing instance

    def test_instance(self):
        self.assertTrue(isinstance(self.test_tags, tags))

        # Testing Save method

    def test_save_method(self):
        tags = tags.objects.create(name='funny')
        tags = tags.objects.all()
        self.assertTrue(len(tags) > 0)

    # Tear down method
    def tearDown(self):
        tags.objects.all().delete()

        # Testing delete method

    def test_delete_tags(self):
        self.test_tags.delete()
        self.assertEqual(len(tags.objects.all()), 0)


class LocationTestClass(TestCase):

    #Set up method the test for location and instantiating the location object


    def setUp(self):
        self.test_location = Location(name = 'Nairobi')
        self.test_location.save()

    #Testing instance

    def test_instance(self):

        self.assertTrue(isinstance(self.test_location, Location))

    #Testing Save method

    def test_save_method(self):
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    # Tear down method
    def tearDown(self):
        Location.objects.all().delete()

        # Testing delete method

    def test_delete_location(self):
        self.test_location.delete()
        self.assertEqual(len(Location.objects.all()), 0)



class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):


        self.nairobi = Location.objects.create(name="nairobi")
        self.funny= tags.objects.create(name='funny')


        self.test_image = Image.objects.create(image='imagesef',
                                name='cat',
                                description='This is a description',
                                location=self.nairobi,
                                )

        self.test_image.save()

    def test_save_method(self):
        self.test_image.save()
        test_images = Image.objects.all()
        self.assertTrue(len(test_images) > 0)

    # Testing save method
    def test_save_image(self):
        self.assertEqual(len(Image.objects.all()), 1)

    # Tear down method
    def tearDown(self):
        Image.objects.all().delete()

    def test_delete_image(self):
        Image.delete_image_by_id(self.test_image.id)
        self.assertEqual(len(Image.objects.all()), 0)



class Review(TestCase):

    def setUp(self):

        self.melissa = User.objects.create(username="melissa")
        self.picture = Image.objects.create(image='image1',
                                            user=self.melissa)
        self.comment = Review.objects.create(comment = 'nicephoto')

        self.test_review = Review.objects.create(user=self.melissa,
                                                 image=self.picture,
                                                 comment='nice photo')
        self.test_review.save()

    #Testing instance

    def test_instance(self):

        self.assertTrue(isinstance(self.test_reviews, Review))

    #Testing Save method

    def test_save_method(self):
        reviews = Review.objects.all()
        self.assertTrue(len(reviews)>0)

    def test_save_review(self):
        self.assertEqual(len(Review.objects.all()), 1)

    # Tear down method
    def tearDown(self):
        Review.objects.all().delete()

        # Testing delete method

    def test_delete_review(self):
        self.test_review.delete()
        self.assertEqual(len(Review.objects.all()), 0)



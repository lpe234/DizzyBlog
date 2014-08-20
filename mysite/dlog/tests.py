from django.test import TestCase
from models import Tag


class TagTestCase(TestCase):

    def setUp(self):
        Tag.objects.create(name='tag1')
        Tag.objects.create(name='tag2')

    def test_tag_curd(self):
        t1 = Tag.objects.get(pk=1)
        t2 = Tag.objects.get(pk=2)
        t1.created_time
        t2.created_time
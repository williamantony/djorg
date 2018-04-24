from django.test import TestCase
from .models import Bookmark

# Create your tests here.
class BookmarkTestCase(TestCase):
  def setUp(self):
    Bookmark.objects.create(name="Noteless bookmark",
                            url="http://wwww.noteless.com")
    Bookmark.objects.create(name="Notefull bookmark",
                            url="http://wwww.notefull.com",
                            notes="This is a bookmark with notes")
    
  def test_retrieving_valid_bookmark(self):

    noteless_bookmark = Bookmark.objects.get(name="Noteless bookmark")
    self.assertEqual(noteless_bookmark.name, "Noteless bookmark")   
    self.assertEqual(noteless_bookmark.url, "http://wwww.noteless.com")
    self.assertEqual(noteless_bookmark.notes, "")

    notefull_bookmark = Bookmark.objects.get(name="Notefull bookmark")
    self.assertEqual(notefull_bookmark.name, "Notefull bookmark")   
    self.assertEqual(notefull_bookmark.url, "http://wwww.notefull.com")
    self.assertEqual(notefull_bookmark.notes, "This is a bookmark with notes")
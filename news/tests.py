from django.test import TestCase
from .models import Editor, Article,tags

# Create your tests here.
class EditorTestClass(TestCase):

  def setUp(self) -> None:
      self.charles = Editor(first_name = 'Charles', last_name = 'Okunzo', email = 'okunzo.charles@gmail.com')


  #testing instance
  def test_instance(self):
    self.assertTrue(isinstance(self.charles, Editor))


  def test_save_method(self):
    self.charles.save_editor()
    editors = Editor.objects.all()
    self.assertTrue(len(editors)>0)


  def test_delete(self):
    self.charles.delete_editor()
    editors = Editor.objects.all()
    self.assertTrue(len(editors) <1)
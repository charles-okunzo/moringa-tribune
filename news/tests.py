from django.test import TestCase
from .models import Editor, Article,tags
import datetime as dt

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


class ArticleTestClass(TestCase):
  def setUp(self) -> None:
      #creating a new editor and saving it 
      self.charles = Editor(first_name = 'Charles', last_name = 'Okunzo', email = 'okunzo.charles@gmail.com')
      self.charles.save()

      self.new_tag = tags(name = 'testing')
      self.new_tag.save()

      self.new_article = Article(title = 'Test Article', post = 'This is a random test article', editor = self.charles)
      self.new_article.save()

      self.new_article.tags.add(self.new_tag)

  def tearDown(self):
    Editor.objects.all().delete()
    tags.objects.all().delete()
    Article.objects.all().delete()

  def test_get_news_today(self):
    todays_news = Article.today_news()
    self.assertTrue(len(todays_news)>0)

  def test_get_news_by_date(self):
    test_date = '2022-04-26'
    date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
    news_by_date = Article.days_news(date)

    self.assertTrue(len(news_by_date)==0)


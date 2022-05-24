from django.db import models

# Create your models here.
class Editor(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField()


  def __str__(self) -> str:
      return self.first_name


  def save_editor(self):
    self.save()


  def delete_editor(self):
    Editor.objects.filter(id=1).delete()

#ordering data when querying from db
  class Meta:
    ordering = ['first_name']

class tags(models.Model):
  name = models.CharField(max_length=30)


  def __str__(self) -> str:
      return self.name


class Article(models.Model):
  title = models.CharField(max_length=60)
  post = models.TextField()
  editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
  tags = models.ManyToManyField(tags)
  pub_date = models.DateTimeField(auto_now_add=True)
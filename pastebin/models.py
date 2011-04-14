from django.db import models

# Create your models here.
class Paste(models.Model):
    LANGS = (
                ('py', 'Python'),
                ('lisp', 'Lisp'),
                ('js', 'Javascript'),
                ('rb', 'Ruby'),
                ('css', 'CSS'),
                ('html', 'HTML')
            )

    title = models.CharField(max_length=128, default = "untitled")
    lang  = models.CharField(max_length=10, choices = LANGS, default = "python")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

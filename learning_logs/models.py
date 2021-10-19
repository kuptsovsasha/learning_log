from django.db import models

# Create your models here.


class Topic(models.Model):
    """theme which studying user"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return text field in admin"""
        return self.text


class Entry(models.Model):
    """specific information for topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text)>50:
            return f"{self.text[:50]}..."
        else:
            return self.text
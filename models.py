# -*- encoding: utf-8 -*-
from django.db import models

class Author(models.Model):
    Name = models.CharField(max_length=60)
    Age = models.IntegerField()
    Country = models.CharField(max_length=60)
    def __unicode__(self):
        return u'%s' % (self.Name)

class Book(models.Model):
    Title = models.CharField(max_length=100)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length=40)
    PublishDate = models.DateField(blank=True, null=True)
    Price = models.CharField(max_length=60)
    def __unicode__(self):
        return u'%s %s %s %s' % (self.Title, self.Publisher, self.PublishDate, self.Price)
sjkhgrkl

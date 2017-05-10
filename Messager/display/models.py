# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Entry(models.Model):
	recipient = models.CharField(max_length = 25)
	phoneNumber = models.CharField(max_length = 10)
	message = models.TextField()
	sendDate = models.DateTimeField()
	def __unicode__ (self):
		return self.recipient


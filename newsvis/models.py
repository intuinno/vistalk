from django.db import models
from django.core.urlresolvers import reverse
from jsonfield import JSONField
import collections

# Create your models here.

class MovievisState(models.Model):
	title=models.CharField(max_length=255)
	slug=models.SlugField(unique=True,max_length=255)
	description = models.CharField(max_length=255)
	content=models.TextField()
	published=models.BooleanField(default=True)
	created=models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']

	def __unicode__(self):
		return u'%s' % self.title

	def get_absolute_url(self):
		return reverse('blog:post', args=[self.slug])

class MovievisCommentState(models.Model):
    content=models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    vis_state = JSONField()

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.content
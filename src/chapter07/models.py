from django.db import models
from django.core.urlresolvers import reverse


class ImportantDate(models.Model):
    date = models.DateField()
    desc = models.CharField(max_length=100)

    def __str__(self):
        return "{} - {}".format(self.date, self.desc)

    def get_absolute_url(self):
        return reverse('impdate_detail', args=[str(self.pk)])

    class Meta:
        ordering = ('-date',)

from django.db import models


class Photo(models.Model):
    owner = models.ForeignKey('users.User', verbose_name='owner', related_name='photos', on_delete=models.CASCADE)
    description = models.CharField('description', max_length=200, blank=True, null=True)
    photo_url = models.CharField('photo url', blank=True, null=True, max_length=300)
    is_approved = models.BooleanField('is approved', default=False, blank=True, null=True)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)

    def __str__(self):
        return f'{self.photo_url}'

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'

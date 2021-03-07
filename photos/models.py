from django.db import models


class Photo(models.Model):
    owner = models.ForeignKey('users.User', verbose_name='owner', related_name='photos', on_delete=models.CASCADE)
    description = models.CharField('description', max_length=200, blank=True, null=True)
    photo_url = models.CharField('photo url', blank=True, null=True, max_length=300)
    is_approved = models.BooleanField('is approved', default=False, blank=True, null=True)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.photo_url}'

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'


class Like(models.Model):
    user = models.ForeignKey('users.User', verbose_name='user', related_name='likes', on_delete=models.CASCADE)
    photo = models.ForeignKey('photos.Photo', verbose_name='user', related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.photo}'

    class Meta:
        verbose_name = 'like'
        verbose_name_plural = 'likes'

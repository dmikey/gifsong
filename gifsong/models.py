from django.db import models

class SFWManager(models.Manager):
    def get_queryset(self):
        return super(SFWManager, self).get_queryset().filter(sfwness=gifsong.SFW)

class gifsong(models.Model):
    SFW = 1
    NSFW = 2
    UNKNOWN = 3
    STATUS_CHOICES = (
        (SFW, 'SFW'),
        (NSFW, 'NSFW'),
        (UNKNOWN, 'Unknown'),
    )

    image_url = models.CharField(max_length=255)
    audio_url = models.CharField(max_length=255)
    sfwness = models.PositiveIntegerField(choices=STATUS_CHOICES, default=UNKNOWN)

    objects = models.Manager()
    sfw = SFWManager()

    def create(cls, image_url, audio_url):
        gifsong = cls()
        return gifsong

from django.db import models

class gifsong(models.Model):
    image_url = models.CharField(max_length=255)
    audio_url = models.CharField(max_length=255)
    
    def create(cls, image_url, audio_url):
        gifsong = cls()
        return gifsong
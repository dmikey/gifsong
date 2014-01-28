from django.test import TestCase

from gifsong.models import gifsong


class TestModeration(TestCase):

    def setUp(self):
        self.rickroll = gifsong.objects.create(image_url='some_song',
                                               audio_url='some_video')

        self.educational_gif = gifsong.objects.create(image_url='astrophysics_lecture.com',
                                                      audio_url='hawking_dubstep',
                                                      sfwness=gifsong.SFW)

    def test_new_gifsong_status(self):
        self.assertEqual(self.rickroll.sfwness, gifsong.UNKNOWN)

    def test_random_manager(self):
        self.assertEqual(gifsong.sfw.count(), 1)
        self.assertEqual(gifsong.sfw.all()[0].image_url, self.educational_gif.image_url)

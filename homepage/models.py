from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=200)
    album_title= models.CharField(max_length=300)
    genre=models.CharField(max_length=400)
    album_logo=models.CharField(max_length=500)

    def __str__(self):
        return self.album_title+'_'+self.artist

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type= models.CharField(max_length=10)
    song_title=models.CharField(max_length=200)

    def __str__(self):
        return self.song_title

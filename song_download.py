from __future__ import unicode_literals
import youtube_dl


# definition of audio characteristics for the songs to be downloaded
song_liked = {
    'outtmpl': 'like/%(title)s.%(ext)s',
    'format': 'bestaudio[asr=44100]/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
song_disliked = {
    'outtmpl': 'dislike/%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

song_test = {
    'outtmpl': 'test/%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# downloadSong/downloadTestSong: download the songs
# in their corresponding folder, depending on their type
def downloadSong(url, is_liked):
    if is_liked:
        youtube_dl.YoutubeDL(song_liked).download([url])
    else:
        youtube_dl.YoutubeDL(song_disliked).download([url])

def downloadTestSong(url):
    youtube_dl.YoutubeDL(song_test).download([url])

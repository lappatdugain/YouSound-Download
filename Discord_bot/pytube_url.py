from pytube import YouTube
from moviepy.editor import *


def url_youtube_mp3(url):
    os.mkdir('./tmp')
    yt = YouTube(url)
    title = yt.title
    caractere_speciaux = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '&', '=', '?', '%', '『』', '「」']
    for caractereSpecial in caractere_speciaux:
        title = title.replace(caractereSpecial, '_')
    path = './tmp'
    yt.streams.get_audio_only().download(output_path=path, filename=f'{title}.mp4')
    mp3 = os.path.join(path, f'{title}.mp3')
    with AudioFileClip(os.path.join(path, f'{title}.mp4')) as video:
        video.write_audiofile(mp3)
    return mp3



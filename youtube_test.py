from yt_dlp import YoutubeDL

ydl_video_opts = {
    'outtmpl' : '%(id)s'+'_.mp4',
    'format' : 'best',
    'writesubtitles' : True,
    'skip_download' : True
}

with YoutubeDL(ydl_video_opts) as ydl:
    result = ydl.download([
        'https://www.youtube.com/watch?v=j098o7024Ss'
    ])
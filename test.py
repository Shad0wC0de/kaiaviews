import yt_dlp

with yt_dlp.YoutubeDL({'cookiesfrombrowser': ('safari',), 'quiet': False}) as ydl:
    ydl.extract_info("https://www.youtube.com/watch?v=g591O8Y69JI", download=False)
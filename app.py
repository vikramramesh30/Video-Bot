from moviepy.editor import VideoFileClip, vfx, AudioFileClip
from moviepy.video.fx.all import crop
import random


def createbackground():
    video = VideoFileClip("background.mp4")

    audio = AudioFileClip("tts.mp3")
    videolength = int(audio.duration) + 1
    randint = random.randint(0, int(video.duration)-videolength)

    randomizedclip = video.subclip(randint,randint+videolength).fx(vfx.colorx,1.2)
    randomizedclip = randomizedclip.set_audio(audio)


    (w,h) = randomizedclip.size
    resizedclip = crop(randomizedclip, width=600, height=5000, x_center=w/2, y_center=h/2)
    resizedclip.write_videofile("final.mp4", codec="libx264")


    
    #resizedclip.write_videofile("final.mp4", codec='mpeg4', bitrate='3000k', audio_codec="aac")








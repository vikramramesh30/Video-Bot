from moviepy.editor import VideoFileClip, vfx, AudioFileClip, TextClip, CompositeVideoClip, ImageClip, concatenate_audioclips
from moviepy.video.fx.all import crop
import stt, random, tts, textwrap, redditpull




def createbackground():
    video = VideoFileClip("Video_Info/background.mp4")

    #create tts
    tts.createtts("hello", "ttsintro.mp3")
    tts.createtts("hello little brody", "ttsbody.mp3")

    audiointro = AudioFileClip("Video_Info/ttsintro.mp3")
    audiobody = AudioFileClip("Video_Info/ttsbody.mp3")
    finalaudio = concatenate_audioclips([audiointro, audiobody])


    videolength = int(finalaudio.duration) + 1

    if videolength < 60:
        videolength = 60
    

    randint = random.randint(0, int(video.duration)-videolength)

    randomizedclip = video.subclip(randint,randint+videolength).fx(vfx.colorx,1.2)
    randomizedclip = randomizedclip.set_audio(finalaudio)


    (w,h) = randomizedclip.size
    #resizedclip = crop(randomizedclip, width=w, height=h, x_center=w/2, y_center=h/2)
    resizedclip = randomizedclip.resize(height=1920)
    resizedclip = resizedclip.crop(x_center=960, y_center=960, width=1080, height=1920)


    finalclip = CompositeVideoClip([resizedclip, createIntroImage(redditpull.title)])

    CaptionGenerator(finalclip).write_videofile("Video_Info/final.mp4", codec="libx264")



    
    #resizedclip.write_videofile("final.mp4", codec='mpeg4', bitrate='3000k', audio_codec="aac")

def createText(caption, start, duration):

    text = TextClip(caption,font="Obelix-Pro",fontsize=70,color='white', stroke_color='black', stroke_width=1.7).set_duration(duration).set_start(start).set_position(('center'))
    shadowtext = text.fx(vfx.colorx, 0.5)
    #shadow_blurred = shadowtext.crop(x1=6, y1=6, width=shadowtext.w, height=shadowtext.h)

    return [text, shadowtext]


def CaptionGenerator(videoclip):
   
   audiobody = AudioFileClip("Video_Info/ttsintro.mp3")
   duration = audiobody.duration


   text_clips = []
   shadow_clips = []


   words_list = stt.Transcriber("Video_Info/ttsbody.mp3")
   for word in words_list:
       caption = createText(word["word"], duration + word["start"], word["duration"])[0]
       text_clips.append(caption)

   finalclip = CompositeVideoClip([videoclip] + text_clips)


   return finalclip

def createIntroImage(intro: str):

    audiobody = AudioFileClip("Video_Info/ttsintro.mp3")

    text_clips = []
    wrapper = textwrap.TextWrapper(width=32) 
    word_list = wrapper.wrap(text=intro) 
    count = 0
    for word in word_list[:-1]:
        text = TextClip(txt = word, fontsize = 42, color = 'black').set_position((30,190 + 50*count))
        text_clips.append(text)
        count+=1
    text = TextClip(txt = word_list[-1], fontsize = 45, color = 'black').set_position((30,190 + 50*count))
    text_clips.append(text)

    duration = audiobody.duration

    text = TextClip(txt = intro, fontsize = 30, color = 'black').set_position((70,140))
    image = ImageClip("Intro_Template.png")
    finalclip = CompositeVideoClip([image] + text_clips).set_start(0).set_duration(duration).set_position(('center', 'center'))

    #finalclip.save_frame("out.png")
    return finalclip

def main():
    createbackground()

if __name__ == '__main__':
    main()




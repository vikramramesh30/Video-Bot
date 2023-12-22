from faster_whisper import WhisperModel
from moviepy.editor import *




def Transcriber(audio: str):

  wordlevel_info = []

  model = WhisperModel("medium")

  segments, info = model.transcribe(audio, word_timestamps=True)

  segments = list(segments) 

  for segment in segments:
    for word in segment.words:
      duration = word.end - word.start
      wordlevel_info.append({'word':word.word,'start':word.start,'duration':duration})

  return wordlevel_info    

    
def main():
  print(Transcriber("Video_Info/tts.mp3"))

if __name__ == '__main__':
    main()  
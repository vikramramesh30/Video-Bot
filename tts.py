import boto3

polly = boto3.client('polly',
                     region_name = 'us-east-1',
                     aws_access_key_id='',
                     aws_secret_access_key='')



def createtts():
    result = polly.synthesize_speech(Text='Hello World, This is a test Message. In this article we will see how we can add external audio to the video file clip in MoviePy. MoviePy is a Python module for video editing, which can be used for basic operations on videos and GIF’s.',
                                    OutputFormat='mp3',
                                    VoiceId='Joanna')

    audio = result['AudioStream'].read()
    with open("tts.mp3", 'wb') as file:
        file.write(audio)

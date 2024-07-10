import boto3
polly = boto3.client('polly',
                     region_name = 'us-east-1',
                     aws_access_key_id='AKIAQZ6QLBAVT37FZ5PO',
                     aws_secret_access_key='') #hidden for security reasons



def createtts(text: str, output:str):
    new_text = text.replace("AITA", "Am I the A hole").replace("IATA", "I am the A hole")


    result = polly.synthesize_speech(Text=new_text,
                                    OutputFormat='mp3',
                                    VoiceId='Joanna')

    audio = result['AudioStream'].read()

    path = "Video_Info/" + output

    with open(path, 'wb') as file:
        file.write(audio)


def main():
    createtts()

if __name__ == '__main__':
    main()



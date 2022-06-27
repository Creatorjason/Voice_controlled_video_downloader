from googleapiclient.discovery import build
import speech_recognition as sp
import pyttsx3
import pywhatkit
import os
import json
import pytube

# initialize speech recognition and pyttsx3
listener = sp.Recognizer()
processor = pyttsx3.init()

def say(text):
    processor.say(text)
    processor.runAndWait()


def test_command():
    try:
        with sp.Microphone() as source:
            print('Speak please')
            user_voice = listener.listen(source)
            voice_command = listener.recognize_google(user_voice)
            if "Genie" in voice_command:
                voice_command = voice_command.replace('Genie', '')
    except:
        pass
    return voice_command


def run_virtual_assistant():
    if "play" in user_voice_req:
        play_song = user_voice_req.replace('play', '')
        pywhatkit.playonyt(f"Ok, playing now {play_song}")

    elif "download" in user_voice_req:
        user_voice_video_search = user_video.get_highest_resolution()
        user_voice_video_search.download()


user_voice_req = test_command()

api_key = "AIzaSyDsOaKGu0tZlFYvyLiEMIEphj_PU0EvoYs"

youtube_search = build("youtube", "v3", developerKey=api_key)

request = youtube_search.search().list(
    part="id",
    order="relevance",
    type="video",
    q=str(user_voice_req)
)
response = request.execute()
# data = json.loads(response)
# print(json.dumps(data, indent=4))
print(response)
# data = json.loads(str(response))
json.dumps(response, sort_keys=True, indent=4)
data = (response['items'][0]['id']['videoId'])

vid_url = f"https://www.youtube.com/watch?v={data}"
user_video = pytube.YouTube(vid_url)

while True:
    run_virtual_assistant()

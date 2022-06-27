from googleapiclient.discovery import build
import json


api_key= "Insert your own API key here"

youtube_search = build("youtube", "v3", developerKey=api_key)

request = youtube_search.search().list(
    part="id",
    order="relevance",
    type="video",
    q="botty"
)
response = request.execute()
# data = json.loads(response)
# print(json.dumps(data, indent=4))
print(response)
#data = json.loads(str(response))
print(json.dumps(response, sort_keys=True, indent=4))
print(response['items'][0]['id']['videoId'])
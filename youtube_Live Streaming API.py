import urllib.request
import json

#-------↓パラメータ入力↓-------

APIKEY = 'AIzaSyB6j2I-k92CQSBcra0Um65402Wbak4j2tA' #
video_id = 'EoRqjH8zt-U' #ライブ配信中のみ

#-------↑パラメータ入力↑-------

#videoメソッドでactiveLiveChatId取得
param = {
    'part':'liveStreamingDetails',
    'id': video_id,
    'key': APIKEY
}
# target_url = 'https://www.googleapis.com/youtube/v3/videos?'+(urllib.parse.urlencode(param))
target_url = 'https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id=EoRqjH8zt-U&key=AIzaSyB6j2I-k92CQSBcra0Um65402Wbak4j2tA'

req = urllib.request.Request(target_url)

with urllib.request.urlopen(req) as json_ress:
    ress = json.load(json_ress)

    #LiveChatMessagesメソッドでチャットを取得
    param = {
        'part':'id,snippet,authorDetails',
        'liveChatId':ress['items'][0]['liveStreamingDetails']['activeLiveChatId'],
        'key':APIKEY
    }
    target_url = 'https://www.googleapis.com/youtube/v3/liveChat/messages?'+(urllib.parse.urlencode(param))
    req = urllib.request.Request(target_url)
    
    with urllib.request.urlopen(req) as json_ress:
        ress = json.load(json_ress)
        for res in ress['items']:
            print(res['snippet']['publishedAt'] + ' ' + res['authorDetails']['displayName'] + ' ' + res['snippet']['displayMessage'])
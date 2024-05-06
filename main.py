# from Mock.GPIO import GPIO
import vlc
import time
import os

PATH=""
listPlayer = vlc.MediaListPlayer()

def useCommand(command, listPlayer): 
    print(command)
    if(command=="pause"): listPlayer.pause()
    elif(command=="play"): listPlayer.play()
    elif(command=="next"): listPlayer.next()
    elif(command=="back"): listPlayer.previous()
    elif(command=="replay"): 
        listPlayer.previous()
        listPlayer.next()
    elif(command.endswith('.mp3') or command.endswith('.m4a') or command.endswith('.flac') or command.endswith('.m3u')):
        mediaList = vlc.MediaList()
        mediaList.add_media(vlc.Media(os.path.join(PATH,command)))
        listPlayer.set_media_list(mediaList)
        listPlayer.play()
    else: 
        mediaList = vlc.MediaList()
        path = PATH+command
        songs = os.listdir(path)
        for s in songs:
            mediaList.add_media(vlc.Media(os.path.join(path,s)))
        listPlayer.set_media_list(mediaList)
        listPlayer.play()    
while True:
    print("Wat do?")
    useCommand(input(),listPlayer)
    time.sleep(2)

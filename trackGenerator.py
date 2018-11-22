#trackGenerator
import os
import sys
import subprocess

#Creates directory string of Desktop and Soundtracks(if already created)
if sys.platform.startswith('win'):                                      #Var is assigned 'path of Desktop' (code for windows)
    documents = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')        
    if (os.path.isdir( os.path.join(documents,'Soundtracks') )):
        dirStr = os.path.join(documents,'Soundtracks')                     #Var is assigned 'path of the directory: Soundtracks'

elif sys.platform.startswith('linux'):                                  # Code for Linux
    documents = os.path.join(os.path.join(os.path.expanduser('~')), 'Documents')              
    if (os.path.isdir( os.path.join(documents,'Soundtracks') )):
        dirStr = os.path.join(documents,'Soundtracks')



def directoryCreation():
    global dirStr
    if sys.platform.startswith('win'):                                      #Var is assigned 'path of Desktop' (code for windows)        
        dirStr = os.path.join(documents,'Soundtracks')   
    elif sys.platform.startswith('linux'):                                  # Code for Linux
        dirStr = '{}/{}'.format(documents,'Soundtracks')
    try:
        os.mkdir(dirStr)                                                                
    except FileExistsError:
        pass

def fileCreation(trackName,noteString):
    with open('f{trackName}.txt', mode='w') as file:
        file.write(noteString)

def editTrack(trackName:str):
    info = """
############ MUSIC CREATION MODE ###############
### Type out your notes that pyano will play ###
### Symbols:                                 ###
### as = a sharp                             ###
### .. = 1 note delay                        ###
################################################
"""
    path = os.path.join(dirStr,trackName)
    if sys.platform == "win32.py":
        os.startfile(path)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, path])
    
def retTrackNames():              #Returns list of track names in folder: Soundtracks
    return (os.listdir(dirStr))
    


directoryCreation()


#trackGenerator
import os
import sys

#Creates directory string of Desktop and Soundtracks(if already created)
if sys.platform.startswith('win'):                                      #Var is assigned 'path of Desktop' (code for windows)
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')        
    if (os.path.isdir( os.path.join(desktop,'Soundtracks') )):
        dirStr = os.path.join(desktop,'Soundtracks')                     #Var is assigned 'path of the directory: Soundtracks'

elif sys.platform.startswith('linux'):                                  # Code for Linux
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')              
    if (os.path.isdir( os.path.join(desktop,'Soundtracks') )):
        dirStr = os.path.join(desktop,'Soundtracks')



def directoryCreation():
    global dirStr
    if sys.platform.startswith('win'):                                      #Var is assigned 'path of Desktop' (code for windows)        
        dirStr = os.path.join(desktop,'Soundtracks')   
    elif sys.platform.startswith('linux'):                                  # Code for Linux
        dirStr = '{}/{}'.format(desktop,'Soundtracks')
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
    os.startfile(os.path.join(dirStr,trackName))
    
def retTrackNames():              #Returns list of track names in folder: Soundtracks
    return (os.listdir(dirStr))
    


directoryCreation()


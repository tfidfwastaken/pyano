# Plays dem notes
import simpleaudio as sa
import time
import sys
import re
import os
from trackGenerator import dirStr

def cleanerrors(text):
    orig = text
    text = re.sub(r'[^a-gs.. ]|[a-g]{2,}', ' ', text)
    text = re.sub(r'(?<=[a-g]s).', ' ', text)
    text = re.sub(r'\bs*', ' ', text)
    text = re.sub(r'[be]s', ' ', text)
    if orig.split() != text.split():
        print("Your note file had errors. pyanosense tried fixing it, but the notes might not sound like what you intend.")
    return text


def play_notes(notes):
    note_list = notes.split()
    for note in note_list:
        if note == '..':
            time.sleep(0.5)
        else:
            wav_ob = sa.WaveObject.from_wave_file(f'notes/{note}1.wav')
            play_ob = wav_ob.play()
            play_ob.wait_done()

def edit_notes():
    info = """
############ MUSIC CREATION MODE ###############
### Type out your notes that pyano will play ###
### Symbols:                                 ###
### as = a sharp                             ###
### .. = 1 note delay                        ###
### Press CTRL+D to finish editing           ###
################################################
"""
    print(info)
    text = sys.stdin.read()
    text = cleanerrors(text)
    resp = input("Would you like to try again? ")
    if resp == 'y':
        return -1
    else:
        return text
        
def store_notes(note_text):
    filename = input("\nEnter name of file to save notes in: ")
    filename += ".txt"
    filename = os.path.join(dirStr, filename)
    print(f"{filename} written")
    with open(filename, 'w') as notefile:
        notefile.write(note_text)

def main(arg=1):
    if arg==1:
        filename = input("Enter Filename: ")
        filename+=".txt"
        filename = os.path.join(dirStr, filename)
        with open(filename) as f:
            notes=f.read()
            text = cleanerrors(notes)
            print(text)
            play_notes(text)
            
    else:
        while True:
            notes = edit_notes()
            if notes != -1:
                break
        play_notes(notes)
        store_notes(notes)

if __name__ == '__main__':
    main()

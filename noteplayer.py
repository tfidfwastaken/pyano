# Plays dem notes
import simpleaudio as sa
import time

def play_notes(notes):
    note_list = notes.split()
    for note in note_list:
        if note == '..':
            time.sleep(0.5)
        else:
            wav_ob = sa.WaveObject.from_wave_file(f'notes/{note}1.wav')
            play_ob = wav_ob.play()
            play_ob.wait_done()

def main(arg):
    if arg==1:
        filename = input("Enter Filename: ")
        with open(filename):
            notes=filename.read()
            play_notes(notes)
    else:
        notes = input("Enter note sequence: ")
        play_notes(notes)

if __name__ == '__main__':
    main(1)

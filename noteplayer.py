# Plays dem notes
import simpleaudio as sa

def play_notes(notes):
    note_list = notes.split()
    for note in note_list:
        wav_ob = sa.WaveObject.from_wave_file(f'notes/{note}1.wav')
        play_ob = wav_ob.play()
        play_ob.wait_done()

def main():
    notes = input("Enter note sequence: ")
    play_notes(notes)

if __name__ == '__main__':
    main()

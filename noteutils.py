# Loads and saves dem text files
import sys

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
    resp = input("Would you like to try again? ")
    if resp == 'y':
        return -1
    else:
        return text

def store_notes(note_text):
    filename = input("\nEnter name of file to save notes in: ")
    filename += ".txt"
    print(f"{filename} written")
    with open(filename, 'w') as notefile:
        notefile.write(note_text)

def main():
    while True:
        notes = edit_notes()
        if notes != -1:
            break
    store_notes(notes)

if __name__ == '__main__':
    main()

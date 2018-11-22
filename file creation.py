import os
documents = os.path.join(os.path.join(os.environ['HOME']), 'Documents')        
dirStr = os.path.join(documents,'Soundtracks')

noteString = 'c d e f .. g a b c'
for i in range (10):
    with open(os.path.join(dirStr,f'{i}.txt'), mode='w') as file:
        file.write(noteString)
    

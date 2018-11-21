import os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')        
dirStr = os.path.join(desktop,'Soundtracks')

noteString = 'c d e f .. g a b c'
for i in range (10):
    with open(os.path.join(dirStr,f'{i}.txt'), mode='w') as file:
        file.write(noteString)
    

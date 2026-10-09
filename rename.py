''' Rename selig files based on the first row '''
import os

# check for selig files
files = [x for x in os.listdir() if x.startswith('selig')]

# rename files based on the first row
for file in files :
    with open(file, 'r') as f :
        name = f.readline().strip()

    os.rename(file, name+".txt")
    print(f'Renamed {file} to {name}')

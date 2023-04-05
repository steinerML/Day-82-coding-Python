filename = 'File Reading/append.txt'

#Write my first line
with open (filename, 'a') as f:
    f.write('This is my first appending exercise.\n')

# Write multiple lines
with open (filename, 'a') as f:
    f.write('This is my second appending exercise.\n')
    f.write('This is my third appending exercise.\n')
    f.write('This is my fourth appending exercise.\n')

# Note that 
with open (filename, 'a') as f:
    f.write('This is also appended everything.\n')
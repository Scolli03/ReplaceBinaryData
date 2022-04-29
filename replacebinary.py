someVar = 'ShainC_MV170_RevL'
header = bytearray(someVar, 'utf8')
filler = bytearray('\x00'*(80-len(header)),'utf8')
header.extend(filler)
print(len(header))
with open('make_characters_fast_with_the_skin_modifier.stl','r+b') as file:
    data = file.read()
    file.seek(0)
    file.write(header)
    file.close()


import re

f = open("D:/Mensaje.txt", "r")

lengths = f.readline().strip()
instruction1 = f.readline().strip()
instruction2 = f.readline().strip()
message = f.readline().strip()

message = re.sub(r'(.)\1+', r'\1', message)

f = open("D:/Mensaje-result.txt", "w")
f.write("%s\n%s" %(("Si" if instruction1 in message else "No"), ("Si" if instruction2 in message else "No")))
f.close()
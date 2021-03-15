import re

f = open("D:/Mensaje.txt", "r")

lengths = f.readline().strip()
instruction1 = f.readline().strip()
instruction2 = f.readline().strip()
message = f.readline().strip()

message = re.sub(r'(.)\1+', r'\1', '12233322155552')
print(message)
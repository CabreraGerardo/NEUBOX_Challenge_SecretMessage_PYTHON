
f = open("D:/Mensaje.txt", "r")

lengths = f.readline().strip()
instruction1 = f.readline().strip()
instruction2 = f.readline().strip()
message = f.readline().strip()

print(instruction1, instruction2, message)
import re
from tkinter.filedialog import askopenfilename
from tkinter import filedialog

filename = askopenfilename()
if(filename != "" or filename != null):
    f = open(filename, "r")

    lengths = f.readline().strip()
    instruction1 = f.readline().strip()
    instruction2 = f.readline().strip()
    message = f.readline().strip()

    message = re.sub(r'(.)\1+', r'\1', message)

    directory = filedialog.askdirectory()
    if(directory != "" or directory != null):
        f = open(directory + "/Mensaje-result.txt", "w")
        f.write("%s\n%s" %(("Si" if instruction1 in message else "No"), ("Si" if instruction2 in message else "No")))
        f.close()
    else:
        print("No path selection")
else:
    print("No selection")
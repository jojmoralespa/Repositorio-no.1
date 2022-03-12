# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

texto = fh.read()

print(texto.upper().rstrip())
    

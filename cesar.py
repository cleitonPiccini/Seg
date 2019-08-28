#python3

#Trabalho, cripitar e descriptar utilizando a cicra de César
k = 10

def openArq (file):

	fileOpen = open(file, "r")
	line = fileOpen.read()
	return line

def cipher (text):

	fileCipher = ""

	#Lê e criptografa.
	for i in text :
		fileCipher = fileCipher + (chr((int(ord(i)) + k) % 256))
		
	return fileCipher

def decipher (text):

	fileDecipher = ""
	
	#Lê e decriptografa.
	for i in text :
		fileDecipher = fileDecipher + (chr((int(ord(i)) - k) % 256))
		
	return fileDecipher	

##___main___##

arquivo = "teste.txt"
testo = openArq (arquivo)
cifra = cipher (testo)
print (cifra)
print (decipher(cifra))


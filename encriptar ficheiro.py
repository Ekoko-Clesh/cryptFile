import platform,os
from time import sleep

#funcao que limpa tela do Terminal
def clear():
	"""
	verifica se a plataforma é windows
	de modo a rodar o comando adequado 
	"""
	if platform=="win32":
		os.system("cls")
		
	#sistema Baseado em Linux
	else:
		os.system("clear")
		
"""
funcao para encriptar o arquivo,recebe como primeiro parâmetro o caminho do arquivo e o segundo parâmetro é a chave da cifra ou rotação
"""
def encriptar(path,chave):
	file=""
	list=[]
	#abertura do ficheiro no modo leitura
	try:
		file=open(f"{path}","r")
		#iteracao para pegar strings do arquivo
		for x in file.readlines():
			#iteracao para pegar caracter por caracter da string armazenada em X e encriptando
			for y in range(0,len(x)):
				if ord(x[y])>=65 and ord(x[y])<=90:
					list.append(chr(ord(x[y])+chave))
				elif ord(x[y])>=97 and ord(x[y])<=122:
					list.append(chr(ord(x[y])+chave))
				elif x[y]=="\n":
					list.append(x[y])
				else:
					list.append(chr(ord(x[y])+chave))
		#fechamento do ficheiro
		file.close()
		file=""
	except (FileNotFoundError):
		print("Erro o tentar abrir o ficheiro\nOu ficheiro inexistente\n")	
		exit(1)
	#abertura do ficheiro no modo escrita de forma a escrever nele o conteudo encriptado
	file=open(f"{path}","w")
	for x  in list:
	      file.write(x)
	print("\nficheiro encriptado\n")
	file.close()
	sleep(2)


"""
funcao para desencriptar o arquivo, recebe como primeiro parâmetro o caminho do arquivo e o segundo parâmetro a chave da cifra ou rotação
"""
def desencriptar(path,chave):
	file=""
	list=[]
	#abertura do ficheiro no modo leitura
	try:
		file=open(f"{path}","r")
		#iteracao para pegar strings do arquivo
		for x in file.readlines():
			#iteracao para pegar caracter por caracter da string armazenada em X e desencriptando
			for y in range(0,len(x)):
				if ord(x[y])>=65 and ord(x[y])<=90:
					list.append(chr(ord(x[y])-chave))
				elif ord(x[y])>=97 and ord(x[y])<=122:
					list.append(chr(ord(x[y])-chave))
				elif x[y]=="\n":
					list.append(x[y])
				else:
					list.append(chr(ord(x[y])-chave))
		#fechamento do ficheiro
		file.close()
		file=""
	except (FileNotFoundError):
		print("Erro o tentar abrir o ficheiro\nOu ficheiro inexistente\n")	
		exit(1)
	
	#abertura do ficheiro no modo escrita de forma a escrever nele o conteudo encriptado
	file=open(f"{path}","w")
	for x  in list:
	      file.write(x)
	print("\nficheiro Desencriptado\n")
	file.close()
	sleep(2)

#funcao que cria Menu	
def menu():
	print("*"*35)
	print("# \033[31m[1]-> Criptografar arquivo\033[m      #\n\n# \033[31m[2]->Descriptografar arquivo\033[m    #\n\n# \033[31m[3]-> Sair\033[m                      #\n")
	print("*"*35)

#inicio do programa principal
while True:
	try:
		clear()
		menu()
		op=int(input("Opção: "))
		if op>3 or op<1:
			print("Opção inválida\n")
			continue
		elif op == 1:
			path=str(input("\nCaminho do arquivo (ex /home/teste/arquivo.txt): "))
			chave=int(input("\nchave de Encriptação: "))
			encriptar(path,chave)
		elif op == 2:
			path=str(input("\nCaminho do arquivo (ex /home/teste/arquivo.txt): "))
			chave=int(input("\nchave de Encriptação: "))
			desencriptar(path,chave)
		elif op == 3:
			break
	except (ValueError):
		print("ERRO!\ninforme valores inteiros somente")
		exit(1)
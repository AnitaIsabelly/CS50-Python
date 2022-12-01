#docs.python.org/library/functions.html#print
#Ask user for their name
name = input("What's your name? ").strip().title() #Declarei uma variavel que recebe um valor de input

# Split the user name into first and last name
# first, last = name.split(" ")

'''
Remove whitespace from str
name = name.strip()

#Primeira letra fica maiuscula
name = name.capitalize()

#Primeira letra de qualquer palavra fica maiuscula
name = name.title()

'''

#Say hello to user
'''
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
sep -> adiciona um separador da string para a variavel
end -> adiciona no final do print 
'''
print("Hello,", name, sep="???")

'''
print("Hello,", name) -> adiciona um espaço da string para a variavel automaticamente
print("Hello, " + name) -> concatena uma ou mais strings
print("Hello, \"name\"") -> meio de adicionar aspas na string
print(f"Hello,", {name}) -> string de formato ou Fstring, criando variavel dentro de uma string
'''


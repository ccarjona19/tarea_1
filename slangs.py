import sqlite3 # LIBRERIA DE SQLITE

def insercion(palabra, significado):
    cur.execute("INSERT INTO slangs (palabra, significado) VALUES (?, ?)", (palabra, significado))
    bd.commit()

def editar(palabra, significado, value):
    try:
        cur.execute("UPDATE slangs SET palabra=?, significado=? WHERE id=?", (palabra, significado, int(value)))
        bd.commit()
    except:
        print("ERR:: El valor que buscas no existe")

def borrar(value):
    try:
        cur.execute("DELETE FROM slangs WHERE id=?", (int(value),))
        bd.commit()
    except:
        print("ERR:: El valor que buscas no existe")

def visualizar():
    cur.execute("SELECT * FROM slangs")
    resultado = cur.fetchall()
    for columnas in resultado:
        print(columnas)

def significado(palabra):
    cur.execute("SELECT significado FROM slangs WHERE palabra=?", (palabra,))
    resultado = cur.fetchone()
    return resultado[0] if resultado else None

bd = sqlite3.connect("slangs.db")
cur = bd.cursor()
    
cur.execute('''
    CREATE TABLE IF NOT EXISTS slangs(
    id INTEGER PRIMARY KEY,
    palabra TEXT,
    significado TEXT )''')

diccionario = {
        1:{"palabra": "tongo", "significado": "policia"},
        2:{"palabra": "gringo", "significado": "persona de origen anglo no habla espaniol"},
        3:{"palabra": "mopri", "significado": "primo"},
        4:{"palabra": "llesca", "significado": "calle"},
        5:{"palabra": "compa", "significado": "compadre"}
    }

for slang in diccionario.values():
    cur.execute("SELECT * FROM slangs WHERE palabra=?", (slang["palabra"],))
    if cur.fetchone() is None: 
       cur.execute("INSERT INTO slangs (palabra, significado) VALUES (?, ?)", (slang["palabra"], slang["significado"]))
bd.commit()

menu = True
while menu:
    print("*****MENU******"
           "\na. Agregar nueva palabra"
           "\nb. Editar palabra existente"
           "\nc. Eliminar palabra existente "
           "\nd. Ver listado de palabras "
           "\ne. Buscar significado de palabra "
           "\nf. Salir ")

    desicion = input("Que deseas hacer?: ")
    if desicion == 'a':
        word = input("Ingresa tu palabra: ")
        text = input('Ingresa el significado: ')
        insercion(palabra=word, significado=text)

    elif desicion == 'b':
        value = input("Ingresa el ID de la palabra que quieres editar: ")
        word = input("Ingresa tu nueva palabra: ")
        text = input('Ingresa el nuevo significado: ')
        editar(palabra=word, significado=text, value=value)

    elif desicion == 'c':
        value = input("Ingresa el ID de la palabra que quieres borrar: ")
        borrar(value=value)
        
    elif desicion == 'd':
        visualizar()

    elif desicion == 'e':
        word = input("Ingresa tu palabra: ")
        print(f'el resultado es:\n{significado(palabra=word)}')

    elif desicion == 'f':
        print("Gracias por usar el programa")
        break

    else: 
        print("**ERROR, informacion no disponible**")
        

# Dao =  Data Access Object
from config.database import get_connection #Importamos la función que hace la conexión a BD 
from models.user_model import User #Importamos el módelo User

class UserDAO:
    @staticmethod
    def get_user_by_username(username):
        conn = get_connection() #Abre la conexión
        if not conn:
            return None #Si no hay conexión no devolvemos nada

        cursor = conn.cursor(dictionary=True) 
        #El cursor nos deja ejecutar queries para la bd
        #dictionary=True, hace que cada fila se vuelva como un diccionario {"id":1,"username":"test"}

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        # Ejecutamos un SELECT buscando al usuario con ese username.
        # %s se reemplaza de manera segura con el valor, evitando SQL Injection.

        row = cursor.fetchone()  # Obtenemos la primera fila encontrada
        cursor.close() # Cerramos cursor
        conn.close() # Cerramos conexión

        if row:
            #Si encontró algo, cremaos el obj User con los datos de la fila
            return User(row["id"], row["username"], row["password"], row["role"])
        return None 
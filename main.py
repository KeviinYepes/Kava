#Desde la carpeta CONFIG el archivo DATABASE importo la FUNCIÓN de la CONEXIÓN
from config.database import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

conn.close()
import psycopg2,os
from dotenv import load_dotenv

load_dotenv()

# Obtener la URL de la base de datos desde una variable de entorno
DATABASE_URL = os.environ.get('POSTGRES_URL')

if not DATABASE_URL:
    raise ValueError("La variable de entorno DATABASE_URL no está configurada")

def connect_db():
    try:
        # Conectar a la base de datos
        conn = psycopg2.connect(DATABASE_URL)
        print("Conexión exitosa a la base de datos.")
        
        # Crear un cursor para ejecutar comandos SQL
        cur = conn.cursor()
        
        # Ejecutar una consulta de prueba
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
        
        # Obtener el resultado de la consulta
        db_version = cur.fetchall()
        print(f"Versión de la base de datos: {db_version}")
        
        # Cerrar el cursor y la conexión
        cur.close()
        conn.close()
        print("Conexión cerrada.")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

if __name__ == "__main__":
    connect_db()

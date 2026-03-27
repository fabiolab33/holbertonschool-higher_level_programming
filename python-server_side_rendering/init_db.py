import sqlite3

def create_database():
    # Esto creará el archivo si no existe y abrirá la conexión
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Borramos la tabla si existe para empezar de cero y evitar conflictos
    cursor.execute('DROP TABLE IF EXISTS Products')
    
    # Creamos la tabla con la estructura exacta
    cursor.execute('''
        CREATE TABLE Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Insertamos los datos de prueba
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    
    conn.commit()
    conn.close()
    print("Database 'products.db' created and populated successfully!")

if __name__ == '__main__':
    create_database()

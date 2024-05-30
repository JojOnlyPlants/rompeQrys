#!/bin/bash

# Solicitar al usuario las credenciales de MySQL
read -p "Ingrese el nombre de usuario de MySQL: " USERNAME
read -sp "Ingrese la contraseña de MySQL: " PASSWORD
echo # Nueva línea para separar la entrada del usuario

# Solicitar al usuario el nombre de la base de datos existente
read -p "Ingrese el nombre de la base de datos existente: " HIPOLOKO

# Conectar a MySQL y crear tablas con filas específicas
mysql -u $USERNAME -p$PASSWORD $DATABASE << EOF
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    apellidoPaterno VARCHAR(50) NOT NULL,
    apellidoMaterno VARCHAR(50),
    email VARCHAR(100) NOT NULL,
    gender VARCHAR(100) NOT NULL,
    admin boolean,
    birthDate Date
);



# Puedes agregar más tablas y definiciones de columnas según sea necesario

EOF

echo "Tablas creadas exitosamente en la base de datos $DATABASE."

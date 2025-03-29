## Instalar entorno vitual
python -m pip install virtualenv
python -m venv venv

## Activar entorno vitual
venv\Scripts\activate

## instalar dependencias despues de clonar##
python -m pip install -r requirements.txt

## DataBase
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status ENUM('pending', 'completed') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
CREATE TABLE blacklisted_tokens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    token TEXT NOT NULL,
    blacklisted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

## Ejecutar el progrma
python -m app.run

## JWT

Authorization Bearer token


## New User
{
    "username": "SACM",
    "email": "SACM@example.com",
    "password": "12345*"
}

## new task

{
    "title": "Revisar informes",
    "description": "Revisar los informes semanales y enviar feedback.",
    "due_date": "2025-04-01",
    "priority": "Alta",
    "status": "pending",
    "assigned_to": 3
}

## PUT task
{
    "status": "completed"
}

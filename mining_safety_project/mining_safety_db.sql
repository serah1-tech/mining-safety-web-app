CREATE DATABASE mining_safety_db;
CREATE TABLE safety_lesson (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,          -- Aligning with 'title' field in Django model
    content TEXT,                         -- Aligning with 'content' field in Django model
    video_url VARCHAR(200),               -- Aligning with 'video_url' field (URLField is stored as VARCHAR in MySQL)
    duration INT,                         -- This field may still be relevant for your data
    start_date DATE,                      -- You can include 'start_date' if it's needed
    end_date DATE,                        -- You can include 'end_date' if it's needed
    description TEXT                      -- 'description' field in MySQL (content in Django model)
);


CREATE TABLE hazards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(255) NOT NULL,  -- Corresponds to 'location' in Django model
    hazard_description TEXT,  -- Corresponds to 'description' in Django model
    risk_level ENUM('Low', 'Medium', 'High') NOT NULL,  -- Corresponds to 'risk_level' in Django model
    timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP  -- Corresponds to 'timestamp' in Django model
);


CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,  -- Corresponds to 'username' in Django
    email VARCHAR(255) UNIQUE NOT NULL,  -- Corresponds to 'email' in Django
    password_hash VARCHAR(255) NOT NULL,  -- Corresponds to 'password' in Django (may need to change name to 'password' if you wish)
    full_name VARCHAR(255),  -- Corresponds to 'full_name' in Django
    role ENUM('Admin', 'Employee', 'Manager') NOT NULL,  -- Corresponds to 'role' in Django
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Corresponds to 'date_joined' in Django
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Optional, for 'last_login' in Django (this will update automatically on login)
);


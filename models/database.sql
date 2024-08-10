CREATE TABLE roles (
    id SERIAL,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE user (
    id SERIAL,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    rol VARCHAR(50) DEFAULT 'patient', -- patient,doctor,nurse,administrator,pharmacyOwner
    token_header VARCHAR(60) NOT NULL,
    token_access VARCHAR(30) NOT NULL,
    a2f BOOLEAN DEFAULT FALSE
);


CREATE TABLE hospitals (
    id SERIAL,
    name VARCHAR(255) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    contact_number VARCHAR(20),
    postal_code VARCHAR(10),
    city VARCHAR(100),
    state VARCHAR(100),
    type VARCHAR(100)
);

CREATE TABLE pharmacies (
    id SERIAL,
    name VARCHAR(255) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    contact_number VARCHAR(20),
    postal_code VARCHAR(10),
    city VARCHAR(100),
    state VARCHAR(100),
    opening_hours VARCHAR(100)
);

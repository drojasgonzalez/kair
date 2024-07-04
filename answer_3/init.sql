CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    name VARCHAR,
    username VARCHAR,
    email VARCHAR,
    address TEXT,
    phone VARCHAR,
    website VARCHAR,
    company VARCHAR
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    post_id INTEGER,
    title VARCHAR,
    body TEXT
);
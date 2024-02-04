CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    first_name TEXT,
    profile_picture_url TEXT
);

CREATE TABLE museums (
    id SERIAL PRIMARY KEY,
    museum_name TEXT
);

CREATE TABLE exhibitions (
    id SERIAL PRIMARY KEY,
    exhibition_name TEXT,
    museum_id INT REFERENCES museums(id),
    description TEXT,
    start_date DATE,
    end_date DATE
);

CREATE TABLE users_exhibitions (
    user_id INT REFERENCES users(id),
    exhibition_id INT REFERENCES exhibitions(id),
)

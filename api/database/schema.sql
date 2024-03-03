CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    first_name TEXT,
    profile_picture_url TEXT
);

CREATE TABLE IF NOT EXISTS museums (
    id SERIAL PRIMARY KEY,
    museum_name TEXT
);

CREATE TABLE IF NOT EXISTS exhibitions (
    id SERIAL PRIMARY KEY,
    exhibition_name TEXT,
    museum_id INT REFERENCES museums(id),
    description TEXT,
    start_date DATE,
    end_date DATE
);

CREATE TABLE IF NOT EXISTS users_exhibitions (
    user_id INT REFERENCES users(id),
    exhibition_id INT REFERENCES exhibitions(id)
);

CREATE TABLE IF NOT EXISTS groups (
    id SERIAL PRIMARY KEY,
    group_name TEXT,
    group_description TEXT
);

CREATE TABLE IF NOT EXISTS groups_users (
    group_id INT REFERENCES groups(id),
    user_id INT REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS groups_exhibitions (
    group_id INT REFERENCES groups(id),
    exhibition_id INT REFERENCES exhibitions(id)
);

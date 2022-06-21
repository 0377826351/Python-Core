CREATE DATABASE big02db IF NOT EXISTS;

CREATE TABLE IF NOT EXISTS Student(
    code_ST VARCHAR(6) NOT NULL PRIMARY KEY, 
    fullName VARCHAR(30) NOT NULL, 
    birthDay date NOT NULL, 
    sex int NOT NULL,
    address VARCHAR(30) NOT NULL,
    phone VARCHAR(10) unique key,
    email VARCHAR(250) unique key
);
CREATE TABLE IF NOT EXISTS Subject(
    code_SB VARCHAR(6) NOT NULL PRIMARY KEY, 
    name_SB VARCHAR(20) unique key NOT NULL 
);
CREATE TABLE IF NOT EXISTS Score(
    code_ST VARCHAR(6) NOT NULL reference Student(code_ST) ON DELETE CASCADE ON UPDATE CASCADE,
    code_SB VARCHAR(6) NOT NULL reference Subject(code_SB) ON DELETE CASCADE ON UPDATE CASCADE, 
    processPoint FLOAT unsigned NOT NULL, 
    endPoint FLOAT unsigned NOT NULL,
    PRIMARY KEY (code_ST, code_SB)
);
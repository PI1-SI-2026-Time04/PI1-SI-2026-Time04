CREATE DATABASE scsc_db;
USE scsc_db;

CREATE TABLE solicitantes (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    celular VARCHAR(20) NOT NULL
);

CREATE TABLE solicitacoes (
    id_solicitacao INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    descricao TEXT NOT NULL,
    urgencia INT NOT NULL CHECK (urgencia BETWEEN 1 AND 3),
    impacto INT NOT NULL CHECK (impacto BETWEEN 1 AND 3),
    prioridade VARCHAR(20) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'Aberta',
    data_abertura DATETIME DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES solicitantes(id_usuario)
        ON DELETE CASCADE
);
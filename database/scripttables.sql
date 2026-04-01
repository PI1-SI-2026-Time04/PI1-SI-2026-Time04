CREATE DATABASE scsc;
USE scsc;

CREATE TABLE solicitante (
    id_usuario INT AUTO_INCREMENT NOT NULL, 
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    PRIMARY KEY (id_usuario)
);

CREATE TABLE solicitacao (
    id_solicitacao INT AUTO_INCREMENT NOT NULL,
    id_usuario INT NOT NULL,  
    categoria VARCHAR(50) NOT NULL,   
    descricao VARCHAR(100) NOT NULL,  
    urgencia INT NOT NULL,
    impacto INT NOT NULL,
    prioridade VARCHAR(20) NOT NULL,  
    `status` VARCHAR(20) NOT NULL,  
    data_abertura DATE NOT NULL,
    PRIMARY KEY (id_solicitacao)
);


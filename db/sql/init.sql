DROP DATABASE IF EXISTS produtos;
CREATE DATABASE produtos;

-- USE produtos;

CREATE TABLE estoque (
    id integer not null auto_increment,
    categoria varchar(100),
    produto varchar(100),
    PRIMARY KEY (id)
);
SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO estoque (categoria, produto) VALUES ('Eletronicos','MacBook Pro');
INSERT INTO estoque (categoria, produto) VALUES ('Futebol','Camisa III Vasco da Gama');
INSERT INTO estoque (categoria, produto) VALUES ('Digital','1 Mês de GloboPlay + Canais');
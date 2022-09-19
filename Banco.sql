CREATE TABLE PALAVRAS(
    ID INT PRIMARY KEY AUTO_INCREMENT,
    COREANO VARCHAR(255) NOT NULL,
    PORTUGUÊS VARCHAR(255) NOT NULL
);

CREATE TABLE FRASES(
    ID INT PRIMARY KEY AUTO_INCREMENT,
    COREANO VARCHAR(255) NOT NULL,
    PORTUGUÊS VARCHAR(255) NOT NULL
);

CREATE TABLE RESULTADOS(
    ID INT PRIMARY KEY AUTO_INCREMENT,
    IDIOMA VARCHAR(255) NOT NULL,
    FRASE_PALAVRA VARCHAR(255) NOT NULL,
    TIPO_EXERCICIO VARCHAR(255) NOT NULL,
    COREANO VARCHAR(255) NOT NULL,
    PORTUGUÊS VARCHAR(255) NOT NULL,
    RESPOSTA VARCHAR(255) NOT NULL,
    RESULTADO VARCHAR(255) NOT NULL
);
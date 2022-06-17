SELECT
    *
FROM
    cidades;

INSERT INTO
	prefeitos(nome, cidade_id)
VALUES
	('Rodrigo Neves', 2),
	('Raquel Lira', 3),
	('Zenaldo Coutinho', null);

INSERT INTO
	prefeitos(nome, cidade_id)
VALUES
	('Rafael Greca', null);

-- Error Code: 1062. Duplicate entry '3' for key 'prefeitos.cidade_id'
INSERT INTO
	prefeitos(nome, cidade_id)
VALUES
	('Rodrigo Pinheiro', 3);

SELECT
    *
FROM
    prefeitos;
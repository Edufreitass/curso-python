-- Error Code: 1264. Out of range value for column 'cnpj' at row 1
INSERT INTO empresas
	(nome, cnpj)
VALUES
    ('Bradesco', 45929608000133),
    ('Vale', 63776400000103),
    ('Cielo', 23679313000113);

ALTER TABLE empresas MODIFY cnpj VARCHAR(14);

-- 3 row(s) affected Records: 3  Duplicates: 0  Warnings: 0
INSERT INTO empresas
	(nome, cnpj)
VALUES
    ('Bradesco', 45929608000133),
    ('Vale', 63776400000103),
    ('Cielo', 23679313000113);

DESC empresas;
DESC prefeitos;

SELECT
    *
FROM
    empresas;

SELECT
    *
FROM
    cidades;

INSERT INTO empresas_unidades
	(empresa_id, cidade_id, sede)
VALUES
	(1, 1, 1),
    (1, 2, 0),
    (2, 1, 0),
    (2, 2, 1);
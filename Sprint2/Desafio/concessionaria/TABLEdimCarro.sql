CREATE TABLE FatoLocacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    idVendedor INT,
    idCombustivel INT,
    dataLocacao DATE,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL,
    valorTotal DECIMAL(10,2),
    FOREIGN KEY (idCliente) REFERENCES dimCliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES dimCarro(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES dimVendedor(idVendedor),
    FOREIGN KEY (idCombustivel) REFERENCES dimCombustivel(idCombustivel)
);

INSERT INTO FatoLocacao (idLocacao, idCliente, idCarro, idVendedor, idCombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, valorTotal)
SELECT 
    idLocacao, 
    idCliente, 
    idCarro, 
    idVendedor, 
    idCombustivel, 
    dataLocacao, 
    horaLocacao, 
    qtdDiaria, 
    vlrDiaria, 
    (qtdDiaria * vlrDiaria) AS valorTotal
FROM Locacao;

CREATE VIEW FatoLocacaoView AS
SELECT idLocacao, idCliente, idCarro, idVendedor, idCombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, valorTotal
FROM FatoLocacao;


CREATE TABLE dimCliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(50),
    estadoCliente VARCHAR(2),
    paisCliente VARCHAR(50)
);

INSERT OR IGNORE INTO dimCliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM Cliente;

CREATE VIEW dimClienteView AS
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM dimCliente;

CREATE TABLE dimCarro (
    idCarro INT PRIMARY KEY,
    kmCarro INT,
    classiCarro VARCHAR(50), 
    marcaCarro VARCHAR(50),
    modeloCarro VARCHAR(50),
    anoCarro INT,
    idCombustivel INT
    
);

INSERT OR IGNORE INTO dimCarro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT DISTINCT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel
FROM Carro;

CREATE VIEW dimCarroView AS
SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel
FROM dimCarro;

CREATE TABLE dimCombustivel (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
);

INSERT OR IGNORE INTO dimCombustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM Combustivel;

CREATE VIEW dimCombustivelView AS
SELECT idCombustivel, tipoCombustivel
FROM dimCombustivel;

CREATE TABLE dimVendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(100),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(50)
);

INSERT INTO dimVendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM Vendedor;

CREATE VIEW dimVendedorView AS
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM dimVendedor;


create table dipendenti
(
    ID int primary key AUTO_INCREMENT,
    nome varchar(20) not null,
    cognome varchar(20) not null,
    posizione_lavorativa varchar(20) not null,
    data_assunzione date not null,
    stipendio int(5) not null
);

CREATE table zone_di_lavoro 
(
    IDZ int PRIMARY KEY AUTO_INCREMENT ,
   	nome_zona varchar(20) not null,
    n_clienti int not null,
    Piano int not null,
);

INSERT INTO dipendenti(`ID`,nome,cognome,posizione_lavorativa,data_assunzione,stipendio) VALUES(0,'Nicola','Di Vietri','Capo','2023-09-27',1000);

INSERT INTO zone_di_lavoro(nome_zona,n_clienti,Piano) VALUES('Ovest',3,4);
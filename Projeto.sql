create database surdezTI14TPython;
use surdezTI14TPython;

create table pessoa(
	codigo int not null primary key auto_increment,
    nome varchar(120) not null,
    telefone varchar(15) not null,
    endereco varchar(120) not null,
    email varchar(120) not null,
    CID varchar(10) not null,
    salario varchar(120) not null,
    dataDeNascimento date not null
    ) engine = InnoDB;
    
    drop table pessoa;
    
    select* from pessoa
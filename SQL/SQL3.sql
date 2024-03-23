use db_uninter;

create table funcionario(
	matricula int primary key auto_increment,
    nome varchar(100) not null,
    data_ncto date not null,
    salario numeric(6,2) not null,
    cargo varchar(100) not null
);

select * from funcionario;

/* Operadores Aritméticos */
select nome, salario * 1.1 from funcionario;

/* Cabeçalho das Colunas */
select nome, salario, salario * 0.1 as 'Gratificação Total' from funcionario;

/* Manipulação de Datas */
select data_ncto from funcionario;
select day(data_ncto) from funcionario; 
select nome, data_ncto from funcionario where month(data_ncto) = 3;

/* Modificar o formato da data no MySQL */
select date_format(data_ncto, '%d/%m/%y') from funcionario;

/* Comando para selecionar a data do Sistema Operacional da máquina */
select curdate();
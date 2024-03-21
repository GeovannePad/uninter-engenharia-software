use db_uninter;

create table funcionario (
	matricula int primary key auto_increment,
    nome varchar(100) not null,
    data_ncto date not null,
    salario numeric(6,2)
);

/* Comandos de manipulação de dados */

/* Insert - insere dados na tabela */
insert funcionario (nome, data_ncto, salario)
values ('José da Silva', '20010317', 1000);

/* Delete - apaga dados da tabela */
delete from funcionario where matricula = 1;

/* Update - altera dados da tabela */
update funcionario set nome='Beatriz Alexia Ricci'
where matricula = 2;

/* Para permitir exclusão e alteração sem where - 0; Para não permitir - 1 */
set sql_safe_updates = 0;

/* Select - seleciona dados da tabela */
select * from funcionario;
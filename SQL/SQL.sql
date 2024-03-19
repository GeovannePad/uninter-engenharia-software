create user 'geovannepad'@'localhost' identified by '486219@Gp';

/* Atribuindo permissões */
grant all privileges on db.tabela to 'usuario'@'localhost';

/*
CREATE - permite criar novas tabelas ou bases de dados
DROP - permite deletar tabelas ou bases de dados
DELETE - permite deletar linhas das tabelas
INSERT - permite inserir linhas nas tabelas
SELECT - permite utilizar o comando Selet para ler bases de dados
UPDATE - permite atualizar linhas das tabelas
GRANT OPTION - permite conceder ou revogar privilégios de outros usuários
*/

/* Revogando permissões */
revoke insert on *.* from 'usuario'@'localhost';
revoke all privileges, grant option from 'usuario'@'localhost';

/* Database
create database [if not exists] nome_banco_dados
[character set nome_charset]
[collate nome_collation]
[encryption] [=] {'y' | 'n'};
*/

create database db_uninter character set utf8mb4 collate utf8mb4_unicode_ci;

/* Apagar um database */
drop database db_uninter;

/* Selecionando um database
use nome_banco_dados;
 */
use db_uninter;

/* Tabelas */
create table aluno (
	matricula int primary key auto_increment,
	nome varchar(100) not null,
	data_ncto date not null
);

/* Controles */
alter table aluno add unique(nome);
alter table aluno drop index nome;

/* Primary key */
alter table aluno drop primary key;
alter table aluno add primary key(matricula);

/* Atribuindo permissões */
grant all privileges on aluno to 'geovannepad'@'localhost';
/* Conversão de dados */
select cast(nome as char(10)) from funcionario;
select cast(salario as unsigned int) from funcionario;

select format(salario,2) from funcionario;

/* Funções agrupadoras - count, sum, avg, max e min */
select cargo, count(*) as "Número total de funcionários" from funcionario group by cargo;
select sum(salario) as "Total salário dos funcionários" from funcionario;
select avg(salario) as "Média salário dos funcionários" from funcionario;
select max(salario) as "Maior salário dos funcionários" from funcionario;
select min(salario) as "Menor salário dos funcionários" from funcionario;

/* Condições de pesquisa */
select * from funcionario where salario = 5000;
select * from funcionario where nome like "M%";
select * from funcionario where cargo is null;

/* Ordenando valores */
select * from funcionario order by nome;
select * from funcionario order by nome desc;

INSERT INTO LOCAL(NFANTASIA, AREA, LOTACAO, ALUGUEL, ENDERECO, TELEFONE, NPROPRIETARIO)
    VALUES('Buffet Andramar', 400, 300, 20.000, 'Avenida Brasil, RJ, 1100', '(11)40028922', 'Antonio Nunes');

INSERT INTO LOCAL(NFANTASIA, AREA, LOTACAO, ALUGUEL, ENDERECO, TELEFONE, NPROPRIETARIO)
    VALUES('Buffet Demácia', 300, 200, 15.000, 'Rua das flores, SP, 140', '(11)32244000', 'Leonardo Teemo');

------------------------------------------------------------------------------------------------------

INSERT INTO EVENTO(NRO, TEMA, DATA, DESCRICAO, LOCAL, TIPO)
    VALUES(1, 'Classico', to_date('2018/01/29 20:00:00', 'yyyy/mm/dd hh24:mi:ss'), 'Casamento clássico', 'Buffet Andramar', 'Casamento');

INSERT INTO EVENTO(NRO, TEMA, DATA, DESCRICAO, LOCAL, TIPO)
    VALUES(2, 'Anos 80', to_date('2019/02/20 19:00:00', 'yyyy/mm/dd hh24:mi:ss'), 'Formatura oitentista', 'Buffet Demácia', 'Formatura');

------------------------------------------------------------------------------------------------------

INSERT INTO CERIMONIA(NRO, RELIGIAO, MESTRE)
    VALUES(0010, 'Catolica', 'Padre Brisola');

INSERT INTO CERIMONIA(NRO, RELIGIAO, MESTRE)
    VALUES(0097, NULL, NULL);

------------------------------------------------------------------------------------------------------

INSERT INTO COLACAO(NRO)
    VALUES(0097);

------------------------------------------------------------------------------------------------------

INSERT INTO COMISSAO(NOME, TELEFONE, EMAIL)
    VALUES('Comissão BCC 016', '(11)99999-8787', 'comissaobcc@usp.br');

------------------------------------------------------------------------------------------------------

INSERT INTO PESSOA(CPF, NOME, TIPO)
    VALUES('444.333.000-55', 'Joao Pedro', 'Noivo');

INSERT INTO PESSOA(CPF, NOME, TIPO)
    VALUES('999.555.777-22', 'Pedro Santos', 'Formando');

INSERT INTO PESSOA(CPF, NOME, TIPO)
    VALUES('111.222.333-45', 'Monica Sanches', 'Funcionario');

------------------------------------------------------------------------------------------------------

INSERT INTO NOIVO(CPF, TELEFONE)
    VALUES('444.333.000-55', '(11)998987676');

------------------------------------------------------------------------------------------------------

INSERT INTO FORMANDO(CPF, CURSO, INSTITUICAO)
    VALUES('999.555.777-22', 'BCC', 'USP');

------------------------------------------------------------------------------------------------------

INSERT INTO SERVICO(ORDEM_SERVICO, PRECO, TIPO)
    VALUES(050, 2000.00, 'Estilizacao');

INSERT INTO SERVICO(ORDEM_SERVICO, PRECO, TIPO)
    VALUES(040, 2500.00, 'Decoracao');

INSERT INTO SERVICO(ORDEM_SERVICO, PRECO, TIPO)
    VALUES(030, 1000.00, 'Florista');

INSERT INTO SERVICO(ORDEM_SERVICO, PRECO, TIPO)
    VALUES(020, 800.00, 'Seguranca');

INSERT INTO SERVICO(ORDEM_SERVICO, PRECO, TIPO)
    VALUES(010, 4000.00, 'Buffet');

------------------------------------------------------------------------------------------------------

INSERT INTO ESTILIZACAO(ORDEM_SERVICO, PACOTE, MODELO, QUANTIDADE)
    VALUES(050, 'Completo', 'Camiseta', 100);

------------------------------------------------------------------------------------------------------

INSERT INTO FLORISTA(ORDEM_SERVICO)
    VALUES(030);

------------------------------------------------------------------------------------------------------

INSERT INTO ARRANJO(ORDEM_SERVICO, NRO_ARRANJO)
    VALUES(030, 05);

------------------------------------------------------------------------------------------------------

INSERT INTO ESPECIES(ORDEM_SERVICO, NOME_ESPECIE)
    VALUES(030, 'Rosa');

INSERT INTO ESPECIES(ORDEM_SERVICO, NOME_ESPECIE)
    VALUES(030, 'Orquidea');

------------------------------------------------------------------------------------------------------

INSERT INTO SEGURANCA(ORDEM_SERVICO, NIVEL)
    VALUES(020, 'Sofisticado');

------------------------------------------------------------------------------------------------------

INSERT INTO DECORACAO(ORDEM_SERVICO, TEMA)
    VALUES(040, 'Classico');

------------------------------------------------------------------------------------------------------

INSERT INTO OBJETO(ORDEM_SERVICO, NOME, QUANTIDADE)
    VALUES(040, 'Mesa', 80);

INSERT INTO OBJETO(ORDEM_SERVICO, NOME, QUANTIDADE)
    VALUES(040, 'Cortinas', 30);

------------------------------------------------------------------------------------------------------

INSERT INTO BUFFET(ORDEM_SERVICO)
    VALUES(010);

------------------------------------------------------------------------------------------------------

INSERT INTO CARDAPIO(ORDEM_SERVICO, NOME, INGREDIENTES, QUANTIDADE)
    VALUES(010, 'Mini Salada', 'Alface, tomate, molho balsâmico', 300);

INSERT INTO CARDAPIO(ORDEM_SERVICO, NOME, INGREDIENTES, QUANTIDADE)
    VALUES(010, 'Canapé de salmão', 'Massa, salmão', 300);

------------------------------------------------------------------------------------------------------

INSERT INTO BEBIDA(ORDEM_SERVICO, NOME, QUANTIDADE)
    VALUES(010, 'Refrigerante', 500);

INSERT INTO BEBIDA(ORDEM_SERVICO, NOME, QUANTIDADE)
    VALUES(010, 'Cerveja', 500);

------------------------------------------------------------------------------------------------------

INSERT INTO FUNCIONARIO(CPF, CARGO, ENDERECO, CT, SALARIO, ORDEM_SERVICO)
    VALUES('111.222.333-45', 'Chefe de cozinha', 'Alameda A, 35', '222.22222.22-2', 30000.00, 010);

------------------------------------------------------------------------------------------------------

INSERT INTO FESTA_CASAMENTO(NRO, FLORISTA)
    VALUES(0010, 030);

------------------------------------------------------------------------------------------------------

INSERT INTO FESTA_FORMATURA(NRO, ESTILIZACAO)
    VALUES(0097, 050);

------------------------------------------------------------------------------------------------------

INSERT INTO FORMATURA(COMISSAO, FESTA, COLACAO)
    VALUES('Comissão BCC 016', 0097, 0097);

------------------------------------------------------------------------------------------------------

INSERT INTO CASAMENTO(NOIVO, FESTA, CERIMONIA)
    VALUES('444.333.000-55', 0010, 0010);

------------------------------------------------------------------------------------------------------

INSERT INTO FORMA(FORMANDO, COMISSAO)
    VALUES('999.555.777-22', 'Comissão BCC 016');

/* 
    Mudança aluguel não é mais chave secundária
    LOCAL = {NFANTASIA, AREA, LOTACAO, ALUGUEL, ENDEREÇO, TELEFONE, PROPRIETARIO}
*/
CREATE TABLE LOCAL (
    NFANTASIA VARCHAR2(20) NOT NULL,
    AREA NUMBER NOT NULL,
    LOTACAO NUMBER,
    ALUGUEL NUMBER NOT NULL,
    ENDERECO VARCHAR2(30) NOT NULL,
    TELEFONE CHAR(12),
    NPROPRIETARIO VARCHAR2(20) NOT NULL,
    CONSTRAINT PK_LOCAL PRIMARY KEY(NFANTASIA)
);

/* 
    Mudança de dia/horario para Data e local agora Not Null
    EVENTO = {NRO, TEMA, DATA, DESC, LOCAL} 
*/
CREATE TABLE EVENTO (
    NRO NUMBER NOT NULL,
    TEMA VARCHAR2(20) NOT NULL,
    DATA DATE NOT NULL,
    DESCRICAO VARCHAR2(20),
    LOCAL VARCHAR2(20) NOT NULL,
    TIPO VARCHAR2(14) NOT NULL,
    CONSTRAINT PK_EVENTO PRIMARY KEY(NRO),
    CONSTRAINT FK_EVENTO FOREIGN KEY(LOCAL) REFERENCES LOCAL(NFANTASIA) ON DELETE CASCADE
);

/*

*/
CREATE TABLE CERIMONIA (
    NRO NUMBER NOT NULL,
    RELIGIAO VARCHAR2(20),
    MESTRE VARCHAR2(20),
    CONSTRAINT PK_CERIMONIA PRIMARY KEY(NRO),
    CONSTRAINT FK_CERIMONIA FOREIGN KEY(NRO) REFERENCES EVENTO(NRO) ON DELETE CASCADE
);

CREATE TABLE COLACAO (
    NRO NUMBER NOT NULL,
    CONSTRAINT PK_COLACAO PRIMARY KEY(NRO),
    CONSTRAINT FK_COLACAO FOREIGN KEY(NRO) REFERENCES EVENTO(NRO) ON DELETE CASCADE
);

CREATE TABLE FESTA_CASAMENTO (
    NRO NUMBER NOT NULL,
    FLORISTA NUMBER,
    CONSTRAINT PK_FESTA_CASAMENTO PRIMARY KEY(NRO),
    CONSTRAINT FK_FESTA_CASAMENTO FOREIGN KEY(NRO) REFERENCES EVENTO(NRO) ON DELETE CASCADE,
    CONSTRAINT FK_FLORISTA FOREIGN KEY(FLORISTA) REFERENCES FLORISTA(ORDEM_SERVICO) ON DELETE CASCADE
);

CREATE TABLE FESTA_FORMATURA (
    NRO NUMBER NOT NULL,
    ESTILIZACAO NUMBER,
    CONSTRAINT PK_FESTA_FORMATURA PRIMARY KEY(NRO),
    CONSTRAINT FK_FESTA_FORMATURA FOREIGN KEY(NRO) REFERENCES EVENTO(NRO) ON DELETE CASCADE,
    CONSTRAINT FK_ESTILIZACAO FOREIGN KEY(ESTILIZACAO) REFERENCES ESTILIZACAO(ORDEM_SERVICO) ON DELETE CASCADE
);

CREATE TABLE COMISSAO (
    NOME VARCHAR2(20) NOT NULL,
    TELEFONE CHAR(12),
    EMAIL VARCHAR2(30),
    CONSTRAINT PK_COMISSAO PRIMARY KEY(NOME)
);

CREATE TABLE FORMATURA (
    COMISSAO VARCHAR2(20) NOT NULL,
    FESTA NUMBER NOT NULL,
    COLACAO NUMBER,
    CONSTRAINT PK_FORMATURA PRIMARY KEY(COMISSAO, FESTA),
    CONSTRAINT FK_COMISSAO FOREIGN KEY(COMISSAO) REFERENCES COMISSAO(NOME) ON DELETE CASCADE,
    CONSTRAINT FK_FFORMATURA FOREIGN KEY(FESTA) REFERENCES FESTA_FORMATURA(NRO) ON DELETE CASCADE,
    CONSTRAINT FK_CFORMATURA FOREIGN KEY(COLACAO) REFERENCES COLACAO(NRO) ON DELETE CASCADE
);

/*
    lINKAR COM O VITOR DEPOIS
*/
CREATE TABLE CASAMENTO (
    NOIVX CHAR(11) NOT NULL,
    FESTA NUMBER(10) NOT NULL,
    CERIMONIA NUMBER,
    CONSTRAINT PK_CASAMENTO PRIMARY KEY(NOIVX, FESTA),
    CONSTRAINT FK_NOIVX FOREIGN KEY(NOIVX) REFERENCES NOIVX(CPF) ON DELETE CASCADE,
    CONSTRAINT FK_FCASAMENTO FOREIGN KEY(FESTA) REFERENCES FESTA_CASAMENTO(NRO) ON DELETE CASCADE,
    CONSTRAINT FK_CCASAMENTO FOREIGN KEY(CERIMONIA) REFERENCES CERIMONIA(NRO) ON DELETE CASCADE
);

/* ================ TABELAS RELACIONADAS A PESSOAS ================ */
CREATE TABLE PESSOA (
    CPF   CHAR(14) NOT NULL,
    NOME  VARCHAR(30) NOT NULL,
    --TIPO  VARCHAR() NOT NULL,
    
    CONSTRAINT PK_PESSOA PRIMARY KEY (CPF)
    --CONSTRAINT CK_PESSOA_TIPO CHECK () 
);

CREATE TABLE NOIVO (
    CPF   CHAR(14) NOT NULL,
    TELEFONE NUMBER,  -- NOT NULL ??
    
    CONSTRAINT PK_NOIVO PRIMARY KEY (CPF),
    CONSTRAINT FK_NOIVO FOREIGN KEY (CPF)
        REFERENCES PESSOA (CPF) 
        ON DELETE CASCADE
);

CREATE TABLE FORMANDO (
    CPF   CHAR(14) NOT NULL,
    CURSO  VARCHAR(30),
    INSTITUICAO VARCHAR(30),
    
    CONSTRAINT PK_FORMANDO PRIMARY KEY (CPF),
    CONSTRAINT FK_FORMANDO FOREIGN KEY (CPF)
        REFERENCES PESSOA (CPF) 
        ON DELETE CASCADE
);

CREATE TABLE FUNCIONARIO (
    CPF   CHAR(14) NOT NULL,
    CARGO VARCHAR(30),
    ENDERECO VARCHAR(30),
    NROCT CHAR(13) NOT NULL, -- CATEIRA DE TRABALHO (XX.XXXXX.XX-X)
    SALARIO NUMBER,
    --SERVICO 
    
    CONSTRAINT PK_FUNCIONARIO PRIMARY KEY (CPF),
    CONSTRAINT FK1_FUNCIONARIO FOREIGN KEY (CPF)
        REFERENCES PESSOA (CPF) 
        ON DELETE CASCADE,
    --CONSTRAINT FK2_FUNCIONARIO FOREIGN KEY (SERVICO)
    --    REFERENCES PESSOA (ORDEMSERVICO) 
    --    ON DELETE CASCADE,
    CONSTRAINT UK_FUNCIONARIO UNIQUE(NROCT)   
);

CREATE TABLE FUNCIONARIO{
	CPF CHAR(14) NOT NULL, -- xxx.xxx.xxx-xx
	CARGO CHAR(13),
	ENDERECO VARCHAR2(20),
	CT CHAR(14),
	SALARIO FLOAT(7,2),
	ORDEM_SERVICO NUMBER,

	CONSTRAINT PK_FUNCIONARIO PRIMARY KEY(CPF),
	CONSTRAINT FK_CPF_FUNCIONARIO FOREIGN KEY(CPF) REFERENCES PESSOA(CPF) ON DELETE CASCADE,
	CONSTRAINT FK_ORDEM_SERVICO_FUNCIONARIO FOREIGN KEY(ORDEM_SERVICO) REFERENCES SERVICO(ORDEM_SERVICO) ON DELETE CASCADE, -- NAO FAZ MUITO SENTIDO SER ON DELETE CASCADE
	CONSTRAINT CK_CT CHECK(REGEXP_LIKE(CPF, '[0-9]{3}\.[0-9]{5}\.[0-9]{2}\-[0-9]{1}'),
	CONSTRAINT CK_CPF CHECK(REGEXP_LIKE(CPF, '[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}')
};

CREATE TABLE SERVICO(
	ORDEM_SERVICO NUMBER,
	PRECO NUMBER(7,2),
	TIPO VARCHAR2(14), 

	CONSTRAINT PK_SERVICO PRIMARY KEY(ORDEM_SERVICO),
	CONSTRAINT CK_TIPO CHECK(TIPO IN ('ESTILIZACAO', 'FLORISTA', 'SEGURANCA', 'DECORACAO', 'BUFFET'))
);
------------------------------------------------------------------------------------

CREATE TABLE ESTILIZACAO(
	ORDEM_SERVICO NUMBER,
	PACOTE CHAR(8),
	MODELO VARCHAR2(20),
	QUANTIDADE NUMBER(4), -- MAXIMO DE 9999 CAMISETAS
    

	CONSTRAINT PK_ESTILIZACAO PRIMARY KEY(ORDEM_SERVICO),
	CONSTRAINT FK_ORDEM_SERVICO_ESTILIZACAO FOREIGN KEY(ORDEM_SERVICO) REFERENCES SERVICO(ORDEM_SERVICO) ON DELETE CASCADE,
	CONSTRAINT CK_PACOTE CHECK(PACOTE IN ('BASICO', 'COMPLETO'))
);

---------------------------------FLORISTA-------------------------------------------

CREATE TABLE FLORISTA(
	ORDEM_SERVICO NUMBER,

	CONSTRAINT PK_FLORISTA PRIMARY KEY(ORDEM_SERVICO),
	CONSTRAINT FK_ORDEM_SERVICO_FLORISTA FOREIGN KEY(ORDEM_SERVICO) REFERENCES SERVICO(ORDEM_SERVICO) ON DELETE CASCADE
);

CREATE TABLE ARRANJO(
	ORDEM_SERVICO NUMBER,
	NRO_ARRANJO NUMBER,

	CONSTRAINT PK_ARRANJO PRIMARY KEY(ORDEM_SERVICO, NRO_ARRANJO),
	CONSTRAINT FK_ORDEM_SERVICO_ARRANJO FOREIGN KEY(ORDEM_SERVICO) REFERENCES FLORISTA(ORDEM_SERVICO) ON DELETE CASCADE
);

CREATE TABLE ESPECIES(
	ORDEM_SERVICO NUMBER,
	NOME_ESPECIE VARCHAR2(20),

	CONSTRAINT PK_ESPECIES PRIMARY KEY(ORDEM_SERVICO, NOME_ESPECIE),
	CONSTRAINT FK_ORDEM_SERVICO_ESPECIES FOREIGN KEY(ORDEM_SERVICO) REFERENCES FLORISTA(ORDEM_SERVICO) ON DELETE CASCADE
);

-------------------------------------------------------------------------------------

CREATE TABLE SEGURANCA(
	ORDEM_SERVICO NUMBER,
	NIVEL CHAR(11),

	CONSTRAINT PK_SEGURANCA PRIMARY KEY(ORDEM_SERVICO),
	CONSTRAINT FK_ORDEM_SERVICO_SEGURANCA FOREIGN KEY(ORDEM_SERVICO) REFERENCES SERVICO(ORDEM_SERVICO) ON DELETE CASCADE,
	CONSTRAINT CK_NIVEL CHECK(NIVEL IN ('BASICO', 'SOFISTICADO'))
);

---------------------------------DECORACAO-------------------------------------------

CREATE TABLE DECORACAO(
	ORDEM_SERVICO NUMBER,
	TEMA VARCHAR2(20),

	CONSTRAINT PK_DECORACAO PRIMARY KEY(ORDEM_SERVICO),
	CONSTRAINT FK_ORDEM_SERVICO_DECORACAO FOREIGN KEY(ORDEM_SERVICO) REFERENCES SERVICO(ORDEM_SERVICO) ON DELETE CASCADE
);

CREATE TABLE OBJETO(
	ORDEM_SERVICO NUMBER,
	NOME VARCHAR2(20),
	QUANTIDADE NUMBER,

	CONSTRAINT PK_OBJETO PRIMARY KEY(ORDEM_SERVICO, NOME),
	CONSTRAINT FK_ORDEM_SERVICO_OBJETO FOREIGN KEY(ORDEM_SERVICO) REFERENCES DECORACAO(ORDEM_SERVICO) ON DELETE CASCADE
);

---------------------------------BUFFET-------------------------------------------

CREATE TABLE BUFFET(
	ORDEM_SERVICO NUMBER

	CONSTRAINT PK_BUFFET PRIMARY KEY(ORDEM_SERVICO),
	CONSTRAINT FK_ORDEM_SERVICO_BUFFET FOREIGN KEY(ORDEM_SERVICO) REFERENCES SERVICO(ORDEM_SERVICO) ON DELETE CASCADE
);

CREATE TABLE CARDAPIO(
	ORDEM_SERVICO NUMBER,
	NOME VARCHAR2(20),
	INGREDIENTES VARCHAR2(20),
	QUANTIDADE NUMBER,

	CONSTRAINT PK_CARDAPIO PRIMARY KEY(ORDEM_SERVICO, NOME),
	CONSTRAINT FK_ORDEM_SERVICO_CARDAPIO FOREIGN KEY(ORDEM_SERVICO) REFERENCES BUFFET(ORDEM_SERVICO) ON DELETE CASCADE
);

CREATE TABLE BEBIDA(
	ORDEM_SERVICO NUMBER,
	NOME VARCHAR2(20),
	QUANTIDADE NUMBER,

	CONSTRAINT PK_BEBIDA PRIMARY KEY(ORDEM_SERVICO, NOME),
	CONSTRAINT FK_ORDEM_SERVICO_BEBIDA FOREIGN KEY(ORDEM_SERVICO) REFERENCES BUFFET(ORDEM_SERVICO) ON DELETE CASCADE
);
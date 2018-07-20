CREATE DATABASE lagoux;
USE lagoux;

DROP TABLE IF EXISTS technologys;
CREATE TABLE technologys (
    lagoux_id             INT primary key auto_increment,
    data_company          varchar(255)    NOT NULL,
    data_positionname     varchar(255)    NOT NULL,
    adds                  varchar(255)    NOT NULL,
    salary                varchar(255)    NOT NULL,
    experience            varchar(255)    NOT NULL,
    industry              varchar(255)    NOT NULL,
    birthday              DATE            NOT NULL
);

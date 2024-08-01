/* Create the database */
CREATE DATABASE  IF NOT EXISTS sentimentanalysis;

/* Switch to the classicmodels database */
USE sentimentanalysis;

/* Drop existing tables  */
DROP TABLE IF EXISTS result;

/* Create the tables */
CREATE TABLE result (
  resultID int,
  contents varchar(50) NOT NULL
);
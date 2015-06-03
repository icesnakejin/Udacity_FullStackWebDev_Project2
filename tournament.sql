-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- DROP old Tables
-- DROP VIEW IF EXISTS OMW;



DROP DATABASE IF EXISTS tournament;
DROP VIEW IF EXISTS Standings;
DROP View IF EXISTS Count;
DROP VIEW IF EXISTS Wins;
DROP TABLE IF EXISTS Matches;
DROP TABLE IF EXISTS Players;

-- Create Database
CREATE DATABASE tournament;
\c tournament;

-- Players Table
CREATE TABLE Players (
id SERIAL primary key,
name varchar(255)
);

-- Matches Table
CREATE TABLE Matches (
id SERIAL primary key,
player int references Players(id),
opponent int references Players(id)
);

-- Wins View shows number of wins for each Player
CREATE VIEW Wins AS
SELECT Players.id, COUNT(Matches.player) AS n
FROM Players
LEFT JOIN Matches
ON Players.id = Matches.player
GROUP BY Players.id;

-- Count View shows number of matches for each Player
CREATE VIEW Count AS
SELECT Players.id, Count(Matches.player)AS n
FROM Players
LEFT JOIN Matches
ON (Players.id = Matches.opponent OR Players.id = Matches.player)
GROUP BY Players.id;

-- Standings View shows the matches and wins of a player
CREATE VIEW Standings AS
SELECT Players.id,Players.name,Wins.n as wins,Count.n as matches
FROM Players,Count,Wins
WHERE Players.id = Wins.id and Wins.id = Count.id
ORDER BY wins DESC;




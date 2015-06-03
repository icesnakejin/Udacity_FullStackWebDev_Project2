#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

#connect to databse
def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

#delete all rows in Match table
def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM Matches;");
    conn.commit()
    conn.close()

#delete all rows in Player table
def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM Players;");
    conn.commit()
    conn.close()


#count the number of players
def countPlayers():
    conn = connect();
    c = conn.cursor();
    c.execute("SELECT count(*) as n FROM Players;");
    
    rows = c.fetchall();
    conn.close();
    
    return rows[0][0]
    """Returns the number of players currently registered."""

# register players into database
def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect();
    c = conn.cursor();
    c.execute("INSERT INTO Players (name) VALUES (%s);",(name,));
    conn.commit();
    conn.close();

# get current standing players and matches and wins
def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect();
    c = conn.cursor();
    c.execute("SELECT * FROM Standings;");
    rows = c.fetchall();
    conn.close();
    return rows;

# register math record
def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect();
    c = conn.cursor();
    c.execute("INSERT INTO Matches (player, opponent) VALUES (%s, %s);", (winner, loser,));
    conn.commit();
    conn.close();
 
# By Compating adjacent players in the standing view, we choose the players with closest match wins.
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn = connect();
    c = conn.cursor();
    c.execute("SELECT id, name, wins, matches FROM Standings ORDER BY wins DESC;");
    rows = c.fetchall();
    conn.close();
    i = 0;
    pairings = [];
    while i < len(rows):
        id1 = rows[i][0];
        name1 = rows[i][1];
        id2 = rows[i + 1][0];
        name2 = rows[i + 1][1];
        pairings.append([id1, name1, id2, name2]);
        i = i + 2;
    return pairings





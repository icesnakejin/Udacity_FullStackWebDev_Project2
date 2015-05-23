# Udacity_Fullstack_Project2
Udacity_Fullstack_Project2 : Tournament Result

# Files
```bash
tournament.py -- python api for database tournament
tournament.sql -- aql schema for databse tournament
tournament_test.py -- testcases for database tournament
```

# How to Use
```bash
Go to your vagrant folder, then turn on vagrant VM:
Yankuns-MacBook-Pro:vagrant yankunjin$ vagrant up

Connect to your VM using SSH:
Yankuns-MacBook-Pro:vagrant yankunjin$ vagrant ssh

go to tournament folder: 
vagrant@vagrant-ubuntu-trusty-32:/vagrant$ cd /vagrant/tournament/

Using psql to run the sql schema
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ psql
vagrant=> \i tournament.sql

Run tournament_test.py;
tournament=> \q
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py
```

Result:
```bash
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py 
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!
```



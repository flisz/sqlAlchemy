This is where i get started with SQL Alchemy
============================================

Howto get started with this repo
--------------------------------

1) startup PostgreSQL with Vagrant

```
vagrant up
```

this will startup a virtual machine based on ubuntu/trusty64, update it
and set up the latest PostgreSQL based on PostgreSQL-s [Vagrantfile](https://wiki.postgresql.org/wiki/PostgreSQL_For_Development_With_Vagrant#Vagrant)

The output of vagrant up (--provision) will print you how to access the
database from CLI, in the python code this has been already set up.

2) put the database under version control

```
python manage.py version_control
```

this will initialize version control over the schema (migrate_version
table)

2) test the change script

```
python manage.py test
```

3) upgrade to the latest version

```
python manage.py upgrade
0 -> 1...
done
```


WTF is here?!?
--------------

This repo only contains a set of python scripts that i experiment with
while getting started with sqlAlchemy and db Schema versioning with
PostgreSQL.

- The __Vagrantfile__ is the PostgreSQL provided virtualized
PostgreSQL setup for development.
- __sql_alchemy__ folder is the db schema versioning rumblings stuff
- __sqlalchemy_*.py__ scripts are simple sample scripts playing with the
  declarative system, nothing to do with the sql_alchemy repo

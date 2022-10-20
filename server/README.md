

### Setting Up Local DB
1. Install requirements.txt
```
$ pip install -r requirements.txt
```
2. Make sure that you have the [Postgres Application](https://www.postgresql.org/download/) *installed* and *running* on your computer.
3. Create a new database through terminal.
```
$ psql
# create DATABASE tutor_local;
CREATE DATABASE
# \q
```
This should create a new database that you can see in your Postgress Application called *tutor_local*.
4. Create a .env file in /server/ folder.
5. Run the following command in terminal:
```
$ export LOCAL_DATABASE_URL="postgresql://postgres:postgress@localhost/tutor_local"
```
6. Then add the following to the .env file.
```
LOCAL_DATABASE_URL=postgresql://postgres:postgress@localhost/tutor_local
```
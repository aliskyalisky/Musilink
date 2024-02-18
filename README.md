# Musilink
Online forum connecting musicians

For
- Bands/Artists searching for Musicians and Sound Engineers
- Musicians and Sound Engineers searching for Bands/Artists
- Songwriters searching for co-write sessions
- Beginners and Professionals searching for like-minded individuals

In short Musilink is a forum built for easy connection of supply and demand in any music industry related scenario. 

FORUM
Search keywords from existing threads to join the conversation or create your own

PROFILE
Let people know who you are and what you are looking for and/or providing

### Install

1. Clone repository and move to the rootfolder
2. Create .env file and fill in the location of your local database and your secret key: <br>
DATABASE_URL=< local-database-location > <br>
SECRET_KEY=< secret-key >
3. Activate virtual environment and install dependencies:
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt
```
4. Set the database schema with:
```
$ psql < schema.sql
```
5. Ready to go! Run the application with:
```
$ flask run
```

### 18.2
Sovellus ei ole testattavissa Fly.iossa.
Sovelluksen perustoiminnot toimivat paikallisesti.
Perustoimintoja ovat:
- Käyttäjätunnuksen luominen
- Kirjautuminen
- Uuden keskustelun luonti
- Keskustelujen avaaminen ja kommentointi

Työn alla:
- Admin toiminnot (Keskustelujen ja viestien poisto)
- Admineille eventlog-sivu, jossa näkyy viimeisimmät tapahtumat (uudet viestit, kirjautumiset yms)
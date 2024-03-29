# Exhibition Wishlist


_I have a group of friends who try to meet every week to visit interesting museums and galleries. We find it hard to track which exhibitions are ending next and therefore should be prioritized, and we would like to plan better who is interested in joining which exhibition._

## 🎨 App

Exhibition Wishlist is a web-based app for organizing museum and gallery visits with friends. 
It allows users to register, log in, join different groups and create lists for them, 
add interesting exhibitions, and track which exhibitions each user is interested in. 
The app also displays exhibition end dates approaching, 
and sorts exhibitions in chronological order based on their end dates.

## 🚀 Test Deployment
https://exhibition-wishlist.fly.dev/

## 🚧 [Changelog ->](docs/Changelog.md)

## 🔧 Installation for Local testing

Clone this repository to your computer and navigate to its root folder.
Create an `.env `file in the folder and specify its contents as follows:

```
FLASK_APP=api.app
DATABASE_URL=<your-local-database-address>
SECRET_KEY=<generate-some-secret-key>
```

Next, activate the virtual environment and install the application dependencies:

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt
```
You will need to have a local PostgreSQL server installed on your computer.
You can get it from 🔗 [here](https://www.postgresql.org/) .

Once you have PostgreSQL running:

Create a new database

```
$ psql
user=# CREATE DATABASE <your-database-name>;`
```
then configure the database schema with:

`$ psql -d <your-database-name> -f < api/database/schema.sql`

And start the application:

`$ flask run`

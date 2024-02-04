# Exhibition Wishlist


_I have a group of friends who try to meet every week to visit interesting museums and galleries. We find it hard to track which exhibitions are ending next and therefore should be prioritized, and we would like to plan better who is interested in joining which exhibition._

## 🎨 App

Exhibition Wishlist is a web-based app for organizing museum and gallery visits with friends. It allows users to register, log in, add interesting exhibitions, and track which exhibitions each user is interested in. The app also reminds as exhibition end dates approach, and sorts exhibitions in chronological order based on their end dates.

## 🚀 Test Deployment
https://exhibition-wishlist.fly.dev/ [4-2-2024 deployment down]

## 🚧 [Changelog](docs/Changelog.md)

## 🔧 Installation for Local testing

Clone this repository to your computer and navigate to its root folder.
Create an `.env `file in the folder and specify its contents as follows:

```
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

Once you have PostgreSQL running, configure the database schema with:

`$ psql < schema.sql`

And start the application:

`$ flask run`

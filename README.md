# Shows and Actors API

- Clone project from github
- In the directory you cloned this project, run the command in the terminal "pipenv install"
- After running the install, you will need to initialize the database with the following steps:
  - pipenv shell
  - python (this will open the python interpretor in your terminal)
  - from app import db
  - db.create_all()
  - exit() or ctrl + D to exit python interpretor
  - python app.py (this will start up the server for the API)
  - Open Postman application

## Routes

- Start by adding a new entry to the API <br />

### POST (Add New)

- In postman use the following route to add a new entry
  > localhost:5000/shows-and-actors
- Have method set to POST
- Fill in JSON data (example below)

```json
{
    "actor_name": "",
    "character_name": "",
    "show": "",
    "year_released": 0
}

{
    "actor_name": "Robert Downy Jr.",
    "character_name": "Tony Stark",
    "show": "Iron Man",
    "year_released": 2008
}
```

### PUT (Update)

- Use the following route for updating
  > localhost:5000/update-show-and-actor/ID
- For this route you will need to make sure to specify which entry ID you are trying to modify
- Have method set to PUT

```json
{
    "actor_name": "Robert Downy Jr.",
    "character_name": "Tony Stark",
    "show": "Iron Man",
    "year_released": 2008
}

{
    "actor_name": "Robert Downy Jr.",
    "character_name": "Tony Stark",
    "show": "Avengers, Inifity War",
    "year_released": 2018
}
```

### GET (all entries or single entry)

- There are 2 separate routes for the GET route
- GET All entries
  > localhost:5000/view-all-shows-and-actors
- GET Single entry
  > localhost:5000/view-single-show-and-actor/ID
- You will need to specify which entry ID you want to view

### DELETE (remove a single entry)

- Use the following to delete an entry
  > localhost:5000/delete-show-and-actor/ID
- You will need to specify which entry ID you want to delete

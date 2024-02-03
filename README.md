# Museum visit planner

## Project Objective

I have a group of friends who try to meet every week to visit interesting museums and galleries. We find it hard to track which exhibitions are ending next and therefore should be prioritized, and we would like to plan better who is interested in joining which exhibition.

## App

The solution would be this web-based app for organizing museum and gallery visits with friends. It allows users to register, log in, add interesting exhibitions, and track which exhibitions each user is interested in. The app also reminds as exhibition end dates approach, and sorts exhibitions in chronological order based on their end dates.


## Features

* **Registration/Login:** Users can create an account and log in
* **Adding exhibitions:** Users can add new exhibitions to the database
* **Viewing exhibition information:** Users can view details about exhibitions, like description, location and end dates

* **Tracking Attendance:** Users can mark which exhibitions they plan to attend

* **Ending soon -tag:** The application reminds about upcoming exhibitions that are about to end soon (eg within two weeks)
* **Sorting Exhibitions:** Exhibitions can be organized chronologically to see which ones are ending soon

* **Mark visited:** User can mark if they have already visited the exhibition

### Bonus:
* **Openings:** an extra section for approaching opening or other events?
* **Further development:** finding or writing an open API with a list of all the current exhibitions around Helsinki area (eg. [museot.fi](https://museot.fi/nayttelykalenteri/), [myhelsinki.fi](https://www.myhelsinki.fi/fi/search?tags=n%C3%A4yttelyt&category=events)


## Database tables (initial plan)

* **Users:** user information like username, password, name, profile picture
* **Exhibitions:** details such as name, location, description, start and end dates, (ending soon -tag?)
* **Users per exhibitions:** tracking which users plan to attend which exhibitions, or if the users have already visited them (or should those be separate tables)
* **Reminders:** approaching exhibition end dates
* ( **Events:** a separate table for openings and other events)

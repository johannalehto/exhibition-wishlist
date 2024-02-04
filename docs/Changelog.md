# Changelog


## 🚀 4-2-2024

☑️ **User registration:** Users can create an account | 🔴 no tests

☑️ **User login:** Users can log in, validation for existing account and matching password | 🔴 no tests

☑️ **Adding exhibitions:** Users can add new exhibitions to the database | 🔴 no tests

☑️ **Viewing exhibition information:** Users can view a list of added exhibitions, with the exhibition name, in which venue it is held at, start and end dates | 🔴 no tests


## 🚧 TODO

🔲 **Tracking Attendance:** Users can mark which exhibitions they plan to attend

🔲 **Ending soon -tag:** The application reminds about upcoming exhibitions that are about to end soon (eg within two weeks)

🔲 **Sorting Exhibitions:** Exhibitions can be organized chronologically to see which ones are ending soon

🔲 **Mark visited:** User can mark if they have already visited the exhibition

### Bonus:
🔲 **Openings:** an extra section for approaching opening or other events?

🔲**Further development:** finding or writing an open API with a list of all the current exhibitions around Helsinki area (eg. [museot.fi](https://museot.fi/nayttelykalenteri/), [myhelsinki.fi](https://www.myhelsinki.fi/fi/search?tags=n%C3%A4yttelyt&category=events))


## Database tables 

☑️ **Users:** user information like username, password, name, profile picture

☑️ **Museums:** museum information, 

☑️ **Exhibitions:** details such as name, location, description, start and end dates, (ending soon -tag?)

☑️ **Users per exhibitions:** tracking which users plan to attend which exhibitions, or if the users have already visited them (or should those be separate tables)

🔲 **Reminders:** approaching exhibition end dates

🔲 **Events:** a separate table for openings and other events
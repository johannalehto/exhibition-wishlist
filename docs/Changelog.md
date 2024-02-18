# Changelog


## 🚀 18-2-2024

✅ **Museum suggestions:** User can choose a museum from a list of existing museums when adding a new exhibition

✅ **Check required fields** Empty fields not allowed, responses with error messages

✅ **Tracking Attendance:** Users can mark which exhibitions they plan to attend, see others attending, and leave if not interested

✅ **Exhibition closing in N days:** Users can see in how many days exhibition is closing.


✅ Exception and error handling for existing features


## 🚀 4-2-2024

✅ **User registration:** Users can create an account | 🔴 no tests

✅ **User login:** Users can log in, validation for existing account and matching password | 🔴 no tests

✅ **Adding exhibitions:** Users can add new exhibitions to the database | 🔴 no tests

✅ **Viewing exhibition information:** Users can view a list of added exhibitions, with the exhibition name, in which venue it is held at, start and end dates | 🔴 no tests


## 🚧 TODO

🔲 Frontend not done at all: CSS styling coming up. 

🔲 Tests for existing features

🔲 Application refactoring. Currently including stupid hacks, magic numbers in tuples and temporary dictionaries. 




### Features


🔲 **Ending soon -tag:** The application reminds about upcoming exhibitions that are about to end soon (eg within two weeks)

🔲 **Sorting Exhibitions:** Exhibitions can be organized chronologically to see which ones are ending soon

🔲 **Delete exhibitions:** User can delete exhibition should they have admin rights

🔲 **Mark visited:** User can mark if they have already visited the exhibition

🔲 **Create a group of friends:** User can create new group which can start their own list

🔲 **Join existing group of friends:** User can create new group which can start their own list

🔲 **Past exhibitions:** User can see exhibitions that already ended


### Bonus:
🔲 **Openings:** an extra section for approaching opening or other events?

🔲**Further development:** finding or writing an open API with a list of all the current exhibitions around Helsinki area (eg. [museot.fi](https://museot.fi/nayttelykalenteri/), [myhelsinki.fi](https://www.myhelsinki.fi/fi/search?tags=n%C3%A4yttelyt&category=events))


## Database tables

✅ **Users:** user information like username, password, name, profile picture

✅ **Museums:** museum information,

✅ **Exhibitions:** details such as name, location, description, start and end dates, (ending soon -tag?)

✅ **Users per exhibitions:** tracking which users plan to attend which exhibitions

✅ **Groups:** User can create new group which can start their own wishlist

✅ **Users per groups:** which users belong to a group

✅ **Exhibitions per group:** which exhibitions belongs to a group

🔲 **Events:** a separate table for openings and other events

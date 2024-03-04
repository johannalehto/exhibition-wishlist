# Changelog

## 🚀 3-3-2024

✅ **Create a group of friends:** User can create new group which can start their own list

✅ **Join existing group of friends:** User can view a list of existing groups and join those

✅ **View exhibition lists per group:** User can see exhibitions that belong to each group, add exhibitions and mark if interested

✅ some CSS styling added



## 🚀 18-2-2024

✅ **Museum suggestions:** User can choose a museum from a list of existing museums when adding a new exhibition 

✅ **Check required fields** Empty fields not allowed, responses with error messages 

✅ **Tracking Attendance:** Users can mark which exhibitions they plan to attend, see others attending, and leave if not interested 

✅ **Exhibition closing in N days:** Users can see in how many days exhibition is closing. 

✅ Exception and error handling for existing features

✅ **Exhibitions sorted:** Exhibitions listed according to ones ending soonest

✅ **Past exhibitions:** User can see exhibitions that already ended 


## 🚀 4-2-2024

✅ **User registration:** Users can create an account 

✅ **User login:** Users can log in, validation for existing account and matching password 

✅ **Adding exhibitions:** Users can add new exhibitions to the database

✅ **Viewing exhibition information:** Users can view a list of added exhibitions, with the exhibition name, in which venue it is held at, start and end dates


## 🚧 TODO


🔲 Tests for existing features

🔲 Application refactoring. Currently including stupid hacks, magic numbers in tuples and temporary dictionaries.



### Upcoming Features


🔲 **Sorting Exhibitions:** Exhibitions can be organized chronologically to see which ones are ending soon

🔲 **Delete exhibitions:** User can delete exhibition should they have admin rights

🔲 **Ending soon -tag:** The application reminds about upcoming exhibitions that are about to end soon (eg within two weeks)

🔲 **Mark visited:** User can mark if they have already visited the exhibition



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


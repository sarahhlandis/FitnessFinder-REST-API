# FitnessFinder: A RESTful API

### [gitHub Repository](https://github.com/sarahhlandis/FitnessFinder-REST-API)

### [Source Control](https://github.com/sarahhlandis/FitnessFinder-REST-API/commits/main)

### [Project Management](https://trello.com/b/L4tvjr7Q/t1a3-terminal-application)

## Purpose:
The FitnessFinder API is an application that intends to mitigate and ease the process of finding a fitness center. Often, when searching for a new gym or studio, one must travel to the prospective facilities to check what amenities they have, hours, and just to gain general info. This application aims to make this process easier for people by having this info all in one place, thus making it easier to compare facilities and find one that better suits their needs.

## Resolution:
This problems needs to be solved because with the evergrowing population of fitness centers, gyms, pilates studios, etc. it can be overwhelming finding something that suits all your needs. This application congregates all the relevant data into one place making it much easier to do preliminary research when starting this process. Upgrades of this app may include a user portal in which users can review and rate facilities making it even easier to see which gyms may be suitable for the prospective gym-goer's needs. 

## Database System:
This API uses postgres

## ORM Basics:
### Functionalities:
### Benefits:

## Endpoints:

## Entity Relationship Diagram:
![erd](/docs/prelim_erd.png)

## Third Party Services:

## Models:

## Database Relations:
The FitnessFinder API intends to implement its database relations based off the project's preliminary entity relationship diagram. 

The relations can be elaborated as follows:

*Facilities* can be only one ```facility_type```. They can also run 0 to multiple promotions (optional). A facility can have many *amenities* as shown thru the join table (```facility_amenities```). A facility can have only one address.

*Facility_types* can be attributed to 0 or many *facilities*. Facility types has the option to have 0 facilities as this is a prepopulated attribute in the database, in which is not required to have any facilities linked to at time of seeding.

*Promotions* can be run at one facility (if the facility is independent) however if the facility is a chain, the promotion can be held across their locations.

*Amenities* has a many-to-many relationship with *facilities*, meaning many amenities can be present at many facilities - this relationship is noted thru the join table ```facility_amenities```.

*Addresses* has a one-to-one relationship with ```facilities``` as only one address can be attributed to one facility location. ```Addresses``` has a one relationship with ```post_codes``` as an address can only have one ```post_code```.

*Post_codes* has an atleast-one to one relationship with ```addresses```. A postcode can have multiple addresses within that post_code, and an address must only have one ```post_code```. The relationship is atleast-one because there will always be atleast one address with that specific post_code if the address is entered into the database.

## Project Management:
![project_start](/docs/trello_board1.png)
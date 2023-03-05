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
![erd](/docs/final_erd.png)

## Third Party Services:

## Models:

## Database Relations:
The FitnessFinder API intends to implement its database relations based off the project's preliminary entity relationship diagram. 

The relations can be elaborated as follows:

*Facilities* can be only one ```facility_type```. They can also run 0 to multiple promotions (optional). A facility can have many *amenities* as shown thru the join table ```facility_amenities```. A facility can have only one address.

*Facility_types* can be attributed to 0 or many ```facilities```. Facility types has the option to have 0 facilities as this is a prepopulated attribute in the database, in which is not required to have any facilities linked to at time of seeding.

*Promotions* can be run at one facility (if the facility is independent) however if the facility is a chain, the promotion can be held across their multiple locations.

*Amenities* has a many-to-many relationship with *facilities*, meaning many amenities can be present at many facilities - this relationship is noted thru the join table ```facility_amenities```.

*Addresses* has a one-to-one relationship with ```facilities``` as only one address can be attributed to one facility location. ```Addresses``` has a one-to-one relationship with ```post_codes``` as an address can only have one ```post_code```.

*Post_codes* has an atleast-one-to-one relationship with ```addresses```. A postcode can have multiple addresses within that post_code, and an address must only have one ```post_code```. The relationship is atleast-one from post_codes because there will always be atleast one address with that specific post_code if the address is entered into the database.

## Project Management
### Development
When building an api that intends to store data thru a connected database, it's important to build logically. The first step I did was create the entity relationship diagram (ERD) so that I could better understand the relationships between all the desired tracked entities. In doing so, I would be better poised to begin coding the relevant models, schemas, routes etc once I knew the exact relations I wanted to build.

I started out with the below entity relationship diagram:
>
![original_ERD](/docs/og_erd.png)
>
but once I realized that I wanted a bit more complexity to show facilities and their related promotions, I needed to bulk out the original ERD, below.
>
![second_ERD](/docs/second_erd.png)
>
Upon further dissection of what I wanted to achieve and in order to ensure an adequate level of data normalization (third normal form), the *final* ERD evolved to the below:
>
![final_ERD](/docs/final_erd.png)
>
Between the second ERD and the final ERD, there was duplication with post_codes as a foreign key in the ```facilities``` table - there waas also an entity relation to match however this was removed prior to the image capture. 
>
The ```addresses``` table was also filled out appropriately with relevant attributes to ensure more specificity upon data entries which in turn allows for more precise filtering options.
>
Lastly, a space for ```owners``` to input their mobile number in case of a 2-factor authentication being released in future api updates.
>
### Planning
To better assist me in my project planning, I chose to use **Trello** to manage my tasks. The below is the beginning trello board that I started with.
>
![project_start](/docs/trello_board1.png)
>
I chose to lay out my tasks with *preliminary* referring to environment and app structure setup, and *tasks* referring to coding actions. I labelled them with colors to signify the difficulty/time I estimated it would take, with green being quick and relatively easy, orange taking incrementally more time and requiring a little more thinking, and lastly red to symbolize tasks that required some hours. I then accordingly assigned due dates for all of them to keep on track. 

![cli_checklist](/docs/trello_cli.png)
![controller_checklist](/docs/trello_controller.png)
![models_checklist](/docs/trello_models.png)


![project_start](/docs/trello_board2.png)
Progress as of March 5


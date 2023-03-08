# FitnessFinder: A RESTful API

### [gitHub Repository](https://github.com/sarahhlandis/FitnessFinder-REST-API)

### [Source Control](https://github.com/sarahhlandis/FitnessFinder-REST-API/commits/main)

### [Project Management](https://trello.com/b/L4tvjr7Q/t1a3-terminal-application)

## Purpose:
The FitnessFinder API is an application that intends to mitigate and ease the process of finding a fitness center. Often, when searching for a new gym or studio, one must travel to the prospective facilities to check what amenities they have, hours, and just to gain general info. This application aims to make this process easier for people by having this info all in one place, thus making it easier to compare facilities and find one that better suits their needs.

## Resolution:
This problems needs to be solved because with the evergrowing population of fitness centers, gyms, pilates studios, etc. it can be overwhelming finding something that suits all your needs. This application congregates all the relevant data into one place making it much easier to do preliminary research when starting this process. Upgrades of this app may include a user portal in which users can review and rate facilities making it even easier to see which gyms may be suitable for the prospective gym-goer's needs. 

## Database System:
I have chosen to use postgreSQL as my relational database management system.
With Flask applications, a developer will often need to utilize a database management system (DBMS) to handle and store the data to later interact with the application and integrate properly with the Flask framework. PostgreSQL as a DBMS has many **benefits**.

1. *PostgreSQL is open sourced* - 
Meaning it's free to use, modify, and implement as per required for your business. This is a pro because access to the database management system will never expire or add to total costs.
>
2. *Large, active community support* - 
"...Users themselves can develop modules and propose the module to the community. The development possibility is superiorly high with collecting opinions from its own global community organized with all different kinds of people. Collective Intelligence, as some might call it, facilitates transmission of indigenous knowledge greatly within the communities."[^7] This aspect is beneficial because it demonstrates that it is widely used and accepted as well as any troubleshooting will be made easier thru highly-frequented and involved forums.
>
3. *PostgreSQL is an object-relational database* - 
"PostgreSQL supports geographic objects so you can use it for location-based services and geographic information systems...[as well as for storing geospatial data]."[^8] This is a plus because other database management systems may not offer support for this making it a highly competitive option for any businesses who wish to store or track anything location related about their users.
>
4. *Robust language support* - 
PostgreSQL can support many languages including Python, Java, PHP, C, C++, etc. Having a database management systems that interacts easily with a multitude of industry-accepted languages is a huge benefit especially if the company ever wants to move the data over from one language to another.
>
5. *ACID* - 
"A PostgreSQL transaction is atomic, consistent, isolated, and durable. These properties are often referred to as ACID:

    >*Atomicity* guarantees that the transaction completes in an all-or-nothing manner.
    >
    >*Consistency* ensures the change to data written to the database must be valid and follow predefined rules.
    >
    >*Isolation* determines how transaction integrity is visible to other transactions.
    >
    > *Durability* makes sure that transactions that have been committed will be stored in the database permanently.[^9]

    This also includes PostgreSQL's WAL (write-ahead logging) making the DBMS highly fault tolerant and virtually immune to errors, power failures, and other mishaps as all modifications are written to a log prior to being applied. In practice, this means the developer has the ability to undo actions from the most recent commit and discard them, thus preserving the most recent data store.[^9]
    >
    Having a database management system that preserves where you left of and has the ability to backtrack is important for data integrity as well as accountability.
>
6. *Flexible indexing* - 
"Full-text search is available when searching for strings with execution of vector operation and string search."[^7] Not all database management systems allow for full-text queries which can prove useful when attempting to comb through copious amounts of data for something or filtration.
>
7. PostgreSQL is *scalable and allows for repetition (cascading)* - 
PostgreSQL implements a cascading delete command which aims to maintain data integrity throughout the system. This is vital in case the programmer deletes something that is linked to a foreign key in another table, that entry in that table will also be deleted as is it not relevant anymore, thus maintaining integrity.
>
8. *Security features* - 
"It provides parameter security, as well as app security. In terms of the parameter security, if you want to lock down your database system it provides the configurations at the OS level that you can configure to lock down the environment around your database. In terms of the app security, it provides security on the basis of user privilege by separating the accounts as read-only, read/write or other actions depending upon the category. Besides just granting permission to a specific user to access something you can also create permission on something to be able to have it ongoing."[^10] 
    >
    This component is a major plus as maintaining data security is integral to any functioning business where user data is stored. PostgreSQL has built-in features that allow a developer to control privileges which is a major part in maintaining information security.

Although there are many pros to using PostgreSQL, there are some **drawbacks** as well that need to be considered prior to setting up your data with this DBMS:
>
1. *Performance* - 
PostgreSQL is inherently slower than similar Database Management Systems like MySQL due to the way it reads. "When finding a query, Postgres due to its relational database structure has to begin with the first row and then read through the entire table to find the relevant data. Therefore, it performs slower especially when there is a large number of data stored in the rows and columns of a table containing many fields of additional information to compare."[^10] This is a drawback if you plan to store very large amounts of data as time is money.
>
2. *PostgreSQL is open sourced* - 
This was also listed as a benefit, but the drawback to this is that in the past, it had a tougher time gaining a reputation and therefore may not be supported by many open-sourced apps which prefer MySQL.[^8]

When choosing a database management system, it's important to deduce the main priorites, the size of the data, and the purpose of storing, budget, along with the level of security required, etc.


## ORM Basics:
### Functionalities:
### Benefits:

## Endpoints:
### Owner endpoints -
blueprint: ```owners = Blueprint('owners', __name__, url_prefix='/owners')```
blueprint: ```auth = Blueprint('auth', __name__, url_prefix="/login")```
- authenticate an existing owner 
```@auth.route("/login", methods=["POST"])```
- register a new owner
```@owners.route('/register', methods=['POST'])```
- retrieve details of a logged-in owner
```@owners.route('/<int:owner_id>', methods=['GET'])```
- update details of a logged-in owner
```@owners.route('/<int:owner_id>', methods=['PUT'])```
- delete account of logged-in owner
```@owners.route('/<int:owner_id>', methods=['DELETE'])```


### Facility endpoints - 
blueprint: ```facilities = Blueprint('facilities', __name__, url_prefix="/facilities")```
- Retrieving all owned facilities of a specific owner ```(GET /owners/<owner_id>/facilities)```
- Retrieving a specific owned facility of a specific owner ```(GET /owners/<owner_id>/facilities/<facility_id>)```
- Creating a new owned facility for a specific owner ```(POST /owners/<owner_id>/facilities)```
- Updating an owned facility for a specific owner ```(PUT /owners/<owner_id>/facilities/<facility_id>)```
- Deleting an owned facility for a specific owner ```(DELETE /owners/<owner_id>/facilities/<facility_id>)```

### Amenities endpoints - 
- Update an owned facility's amenities as a logged-in owner ```@facilities.route('/<int:facility_id>/amenities', methods=['PUT'])```




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





![project_endpts](/docs/trello_endpoints.png)

![project_endpts2](/docs/trello_endpoints2.png)

![project_pub_endpts](/docs/trello_public_endps.png)


Progress as of March 8
![project_mid](/docs/trello_board3.png)

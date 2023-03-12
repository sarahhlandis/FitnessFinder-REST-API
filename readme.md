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
"...Users themselves can develop modules and propose the module to the community. The development possibility is superiorly high with collecting opinions from its own global community organized with all different kinds of people. Collective Intelligence, as some might call it, facilitates transmission of indigenous knowledge greatly within the communities."[^2] This aspect is beneficial because it demonstrates that it is widely used and accepted as well as any troubleshooting will be made easier thru highly-frequented and involved forums.
>
3. *PostgreSQL is an object-relational database* - 
"PostgreSQL supports geographic objects so you can use it for location-based services and geographic information systems...[as well as for storing geospatial data]."[^3] This is a plus because other database management systems may not offer support for this making it a highly competitive option for any businesses who wish to store or track anything location related about their users.
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
    > *Durability* makes sure that transactions that have been committed will be stored in the database permanently.[^4]

    This also includes PostgreSQL's WAL (write-ahead logging) making the DBMS highly fault tolerant and virtually immune to errors, power failures, and other mishaps as all modifications are written to a log prior to being applied. In practice, this means the developer has the ability to undo actions from the most recent commit and discard them, thus preserving the most recent data store.[^4]
    >
    Having a database management system that preserves where you left of and has the ability to backtrack is important for data integrity as well as accountability.
>
6. *Flexible indexing* - 
"Full-text search is available when searching for strings with execution of vector operation and string search."[^2] Not all database management systems allow for full-text queries which can prove useful when attempting to comb through copious amounts of data for something or filtration.
>
7. PostgreSQL is *scalable and allows for repetition (cascading)* - 
PostgreSQL implements a cascading delete command which aims to maintain data integrity throughout the system. This is vital in case the programmer deletes something that is linked to a foreign key in another table, that entry in that table will also be deleted as is it not relevant anymore, thus maintaining integrity.
>
8. *Security features* - 
"It provides parameter security, as well as app security. In terms of the parameter security, if you want to lock down your database system it provides the configurations at the OS level that you can configure to lock down the environment around your database. In terms of the app security, it provides security on the basis of user privilege by separating the accounts as read-only, read/write or other actions depending upon the category. Besides just granting permission to a specific user to access something you can also create permission on something to be able to have it ongoing."[^5] 
    >
    This component is a major plus as maintaining data security is integral to any functioning business where user data is stored. PostgreSQL has built-in features that allow a developer to control privileges which is a major part in maintaining information security.

Although there are many pros to using PostgreSQL, there are some **drawbacks** as well that need to be considered prior to setting up your data with this DBMS:
>
1. *Performance* - 
PostgreSQL is inherently slower than similar Database Management Systems like MySQL due to the way it reads. "When finding a query, Postgres due to its relational database structure has to begin with the first row and then read through the entire table to find the relevant data. Therefore, it performs slower especially when there is a large number of data stored in the rows and columns of a table containing many fields of additional information to compare."[^5] This is a drawback if you plan to store very large amounts of data as time is money.
>
2. *PostgreSQL is open sourced* - 
This was also listed as a benefit, but the drawback to this is that in the past, it had a tougher time gaining a reputation and therefore may not be supported by many open-sourced apps which prefer MySQL.[^3]

When choosing a database management system, it's important to deduce the main priorites, the size of the data, and the purpose of storing, budget, along with the level of security required, etc.
>
I chose postgreSQL as my database management system for my flask API because it is an object-relational database (ORD) meaning it allows for the capability to use object-relational mapping (ORM) platforms such as Marshmallow. This makes it significantly easier to handle input and output data as the ORM is built to work in conjunction with the default formatting of an ORD.
>
Additionally, hosting an api that will eventually require data cleaning as facilities will close or move or just wish for their information not to be stored anymore, requires the ability to be scalable. PostgreSQL has built-in functionality that aims to maintain data integrity, such as the ```cascading delete``` command. At this stage the database will not be global or house international facilities, so the speed of the querying capacity was not a major determining factor in using postgreSQL. 
>
Being that this is a searchable database with different parameters a user may want to query, it was important to choose a database that allowed for flexible and complex querying. These were the main components I considered when choosing a database and felt that postgreSQL was most suited to this API's needs regarding data storage, maintaining integrity, and querying capabilities.

## ORM Basics:
"ORM stands for object-relational mapping, where objects are used to connect the programming language on to the database systems, with the facility to work SQL and object-oriented programming concepts."[^1] There are many different ORMs which link better to specific object-oriented programming languages and frameworks such as SQLAlchemy and Flask, or Django ORM and Django (language).
>
### Functionalities:
> ORMs generate objects which map to tables in the database virtually. Once these objects are up, then coders can easily work to retrieve, manipulate or delete any field from the table without paying much attention to language specifically. It supports writing complex long SQL queries in a simpler way. It uses libraries to comprehend the code we are writing in the form of objects and then map it onto the database.[^1]
>
### Benefits:

## API Endpoints:
> 
### Secure endpoints: 
### Owner endpoints -
blueprint: 
    ```owners = Blueprint('owners', __name__, url_prefix='/owners')```
>
blueprint: 
    ```auth = Blueprint('auth', __name__, url_prefix="/login")```
- authenticate an existing owner 
    ```@auth.route("/login/secure", methods=["POST"])```
- register (create) a new owner
    ```@owners.route('/register/secure', methods=['POST'])```
- retrieve details of a logged-in owner
    ```@owners.route('/<int:owner_id>/secure', methods=['GET'])```
- update details of a logged-in owner
    ```@owners.route('/<int:owner_id>/secure', methods=['PUT'])```
- delete account of logged-in owner
    ```@owners.route('/account/secure', methods=['DELETE'])```
** In regards to the deletion of an owner account, this will also delete all associated facilities, as the API does not allow for unowned facilities (without attribution to a specific owner).

### Facility endpoints - 
blueprint: 
    ```facilities = Blueprint('facilities', __name__, url_prefix="/facilities")```
- Create a new facility for logged-in owner (with or without existing owned facility)
    ```@facilities.route('/secure', methods=['POST'])```
- Retrieve a list of all facilities owned by a logged-in owner          
    ```@facilities.route('/secure', methods=["GET"])```
- Retrieve a specific facility of a logged-in owner
    ```@facilities.route('/<int:facility_id>/secure', methods=['GET'])```
- Update a specific facility of a logged-in owner
    ```@facilities.route('/<int:facility_id>/secure', methods=['PUT'])```
- Deletion of specific facility unless owner only has 1 facility, in which case, must delete account (and facility)
    ```@facilities.route('/<int:facility_id>/secure', methods=['DELETE'])```
- Retrieve a list of all facility types and their id assignments (facility_type_id is required as a ```fkey``` in the facilities entity, so must be included at time of facility creation)
    ```@facilities.route('/facility_types', methods=['GET'])```

### Amenities endpoints - 
blueprint: 
    ```facility_amenities = Blueprint('facility_amenities', __name__, url_prefix='/facilities_amenities')```
- Retrieve all amenities for a specified facility by a logged-in owner
    ```@facility_amenities.route('/<int:facility_id>/amenities/secure', methods=['GET'])```
- Update only amenities respective to owned facility for logged-in owner
    ```@facility_amenities.route('/<int:facility_id>/amenities/secure', methods=['PUT'])```
- Remove (delete) selected amenities from a specific facility by a logged-in owner
    ```@facility_amenities.route('/<int:facility_id>/amenities/secure', methods=['DELETE'])```
** An owner cannot create new amenities therefore there is no functionality for a route that allows this. The amenities are prepopulated at time of database initialization - once they are created, they are not created again. 
    >
    I chose to include amenities in this way so that owners could not say "swim_spa" as an amenity, rather either "pool" or "spa". If every owner could create amenities with no naming convention, there would more than likely be many of the same amenities, however named differently. This would render querying by amenities useless and disorganized.

### Promotions endpoints - 
blueprint: ```promotions = Blueprint('promotions', __name__, url_prefix='/promotions')```
- Create a new promotion
    ```@promotions.route('/<int:facility_id>/secure', methods=['POST'])```
- Update a promotion for a specific facility of a logged-in owner
    ```@promotions.route('/<int:facility_id>/<int:promotion_id>/secure', methods=['PUT'])```
- Delete a single promotion for a selected facility by a logged-in owner
    ```@promotions.route('/<int:promotion_id>/secure', methods=['DELETE'])```

** I chose not to create a specific endpoint to retrieve just the promotion of a specific facility as this capability is covered in the retrieval of an entire facility's details.

### Addresses endpoints - 
blueprint: 
    ```addresses = Blueprint('addresses', __name__, url_prefix='/addresses')```
- Retrieve a single address for a specified facility by a logged-in owner
    ```@addresses.route('/<int:facility_id>/secure', methods=['GET'])```
- Update an address for a singular facility by a logged-in owner
    ```@addresses.route('/<int:facility_id>/secure', methods=['PUT'])```

** Specific to addresses, there is no functionality to create a new address since an address must be registered with a facility at the time of facility creation (i.e. an address cannot be created for a facility retrospectively). Additionally, there is no functionality to delete an address as an address is required for every facility and a deletion of an address would compromise the data's integrity.
>
Regarding this API's endpoints, some require verification and related authentication as its important to grant privileges to only those who require it, in this case - owners.
>
The endpoints with verification are specified in the routes with a ```/secure``` tag attached to the endpoint url. The public routes accessible to any user (untracked), do not have this ```/secure``` tag. This is in part to deter accidental routing to this part of the API by someone unintended, as well as to signify to those who are at that endpoint, that it is a secure route.
>
> ### Public endpoints: 



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

*Amenities* has a many-to-many relationship with *facilities*, meaning many amenities can be present at many facilities - this relationship is defined thru the join table ```facility_amenities```.

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

As I started building out the endpoints, I realized there were going to be many so would be best to lay them out. I added them to my trello board so it was easier to tick off when complete, making sure I didn't skip any required functionality.
Secure endpoints:
![project_endpts](/docs/trello_endpoints.png)
![project_endpts2](/docs/trello_endpoints2.png)
>
Public endpoints:
![project_pub_endpts](/docs/trello_public_endps.png)

Progress as of March 8
![project_mid](/docs/trello_board3.png)
>
Progress as of March 10
![project_mid](/docs/trello_board4.png)
>


## Sources
[^2]: Bitnine.net. (2023). [online] Available at: https://bitnine.net/blog-postgresql/advantages-of-postgresql/?ckattempt=1 [Accessed 27 Jan. 2023].


[^3]: Sharda, A. (2021, April 28). What is PostgreSQL? Introduction, Advantages & Disadvantages [Review of What is PostgreSQL? Introduction, Advantages & Disadvantages]. LinkedIn Pulse. https://www.linkedin.com/pulse/what-postgresql-introduction-advantages-disadvantages-ankita-sharda


[^4]: Anon, (n.d.). PostgreSQL Transaction. [online] Available at: https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-transaction/#:~:text=A%20PostgreSQL%20transaction%20is%20atomic [Accessed 27 Jan. 2023].


[^5]: Dhruv, S. (2019, May 15). PostgreSQL Advantages and Disadvantages [Review of PostgreSQL Advantages and Disadvantages]. https://www.aalpha.net/blog/pros-and-cons-of-using-postgresql-for-application-development/

[^1]: 
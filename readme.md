# FitnessFinder: A RESTful API

### [gitHub Repository](https://github.com/sarahhlandis/FitnessFinder-REST-API)

### [Source Control](https://github.com/sarahhlandis/FitnessFinder-REST-API/commits/main)

### [Project Management](https://trello.com/b/L4tvjr7Q/t1a3-terminal-application)

## Help Documentation:
Please ensure your local machine is fit with both Postgres and psycopg prior to engaging the following configuration steps.

1. Database Configuration
    - Check Postgres is running on its default port, 5432. If it is running on a different port, please modify the below statement to located in the ```.env``` file to suit your requirements (the numbers following "localhost:").
        >
        ```DATABASE_URL='postgresql+psycopg2://admin:adm1n@localhost:5432/fitnessfinder_db'```
    >
    - Run ```psql``` in your command line, followed by ```CREATE DATABASE fitnessfinder_db;``` to create the relational database.
    >
2. Database User and Privileges
    - Run ```CREATE USER admin WITH PASSWORD 'adm1n';``` to create the user to access the database.
        >
        ** If you wish to change the user name or the database name, modify the *DATABASE_URL* statement in the ```.env``` file accordingly. Change this part ```admin:adm1n``` according to your desired user:password and this part ```fitnessfinder_db``` to your desired database.
        >
    - Run ```GRANT ALL PRIVILEGES ON DATABASE fitnessfinder_db TO admin;``` (alter if you've modified from the previous steps).
>
3. Setting up the Stack Environment
    - Using your command line interface, move into your local copy of the ```SarahLandis_T2A2``` directory.
    - Move into the ```src``` folder.
    - Run ```python3 -m .venv venv``` on your command line to create a virtual environment for the application.
    - Run ```source .venv/bin/activate``` on your command line to activate the virtual environment.
>
4. Install Application Dependencies
    - Run ```pip install -r requirements.txt``` from your command line.
>
5. Database Seeding
    - Run ```flask db create``` on your command line to create the tables of the relational database.
    - Run ```flask db init``` on your command line to populate the tables with designated default values.
    - Run ```flask db seed``` on your command line to seed the tables in the relational database.
    - If you need to, run ```flask db drop``` on your command line to drop all of the tables in the relational database.
>
6. Server Informatiom
    - This flask application is set up to run on the default local host server port (5000). If your local host runs on another port, please change the following in the ```.flaskenv``` file:
    ```FLASK_RUN_PORT=5000```
>
7. This application's main file is called ```app.py``` and is set up accordingly to run with the command ```flask run``` from the command line. 
    >
    ** To better assist you in navigating the api, please see the below endpoints.

## API Endpoints:
> 
### Secure endpoints: 
Regarding this API's endpoints, some require verification and related authentication as its important to grant privileges to only those who require it, in this case - owners.
>
The endpoints with *authentication (JWT) and verification required* are denoted in the routes by a ```/secure``` tag attached to the endpoint url. The public routes accessible to any user (untracked), do not have this ```/secure``` tag. This is in part to deter accidental routing to this part of the API by someone unintended, as well as to signify to those who are at that endpoint, that it is a secure route.
>
Attached to each URL are payload requests in which you can view sample data -
### Owner endpoints -
registered blueprints: 
```owners = Blueprint('owners', __name__, url_prefix='/owners')```

```auth = Blueprint('auth', __name__, url_prefix="/login")```
>
- POST ```/login/secure```
    - *Functionality*: authenticate an existing owner 
    - *Route*: ```@auth.route("/login/secure", methods=["POST"])```
    - *JSON Request Parameters*: email, password
    - *Expected Response*: 
    ![loginroute](/docs/authroute.png)
>
- POST ```/register/secure```
    - *Functionality*: register (create) a new owner
    - *Route*: ```@owners.route('/register/secure', methods=['POST'])```
    - *JSON Request Parameters*: {name, email, mobile, password}
    - *Expected Response*:
    ![owner_detailsroute](/docs/ownerroute2.png)
    ![owner_detailsroute](/docs/ownerroute2a.png)
>
- GET ```/<int:owner_id>/secure```
    - *Functionality*: retrieve details of a logged-in owner
    - *Route*: ```@owners.route('/<int:owner_id>/secure', methods=['GET'])```
    - *JSON Request Parameters*: None
    - *Expected Response*:
    ![owner_detailsroute](/docs/ownerroute3.png)
>
- PUT ```/<int:owner_id>/secure```
    - *Functionality*: update details of a logged-in owner
    - *Route*: ```@owners.route('/<int:owner_id>/secure', methods=['PUT'])```
    - *JSON Request Parameters*: Any owner_fields owner wishes to change
    - *Expected Response*: 
    ![owner_updateroute](/docs/ownerroute4.png)
    ![owner_updateroute](/docs/ownerroute4a.png)
>
- DELETE ```/account/secure```
    - *Functionality*: delete account of logged-in owner
    - *Route*: ```@owners.route('/account/secure', methods=['DELETE'])```
    - *JSON Request Parameters*: None
    - *Expected Response*:
    ![owner_deleteroute](/docs/ownerroute5.png)
    >
    ** In regards to the deletion of an owner account, this will also delete all associated facilities, as the API does not allow for unowned facilities (without attribution to a specific owner).

### Facility endpoints - 
registered blueprint: 
    ```facilities = Blueprint('facilities', __name__, url_prefix="/facilities")```
- POST ```/secure```
    - *Functionality*: Create a new facility for logged-in owner (with or without existing owned facility)
    - *Route*: ```@facilities.route('/secure', methods=['POST'])```
    - *JSON Request Parameters*: 
    - *Expected Response*:
>
- GET ```/secure```
    - *Functionality*: Retrieve a list of all facilities owned by a logged-in owner         
    - *Route*: ```@facilities.route('/secure', methods=["GET"])```
    - *JSON Request Parameters*: None
    - *Expected Response*:
    ![allfacility_route](/docs/facilitiesroute1.png)
    ![allfacility_route](/docs/facilitiesroute1a.png)
>
- GET ```/<int:facility_id>/secure```
    - *Functionality*: Retrieve a specific facility of a logged-in owner
    - *Route*: ```@facilities.route('/<int:facility_id>/secure', methods=['GET'])```
    - *JSON Request Parameters*: None
    - *Expected Response*:
    ![specificfacility_route](/docs/facilitiesroute2.png)
    ![specificfacility_route](/docs/facilitiesroute2a.png)
>
- PUT ```/<int:facility_id>/secure```
    - *Functionality*: Update a specific facility of a logged-in owner
    - *Route*: ```@facilities.route('/<int:facility_id>/secure', methods=['PUT'])```
    - *JSON Request Parameters*: any facility_fields the owner wishes to update
    - *Expected Response*:
    ![updatefacility_route](/docs/facilitiesroute5.png)
    ![updatefacility_route](/docs/facilitiesroute5a.png)
>
- DELETE ```/<int:facility_id>/secure```
    - *Functionality*: Deletion of specific facility unless owner only has 1 facility, in which case, must delete account (and facility)
    - *Route*: ```@facilities.route('/<int:facility_id>/secure', methods=['DELETE'])```
    - *JSON Request Parameters*: None
    - *Expected Response*:
    ![deletefacility_route](/docs/facilitiesroute4.png)
    ![deletefacility_route](/docs/facilitiesroute4a.png)
>

### Amenities endpoints - 
registered blueprint: 
    ```facility_amens = Blueprint('facility_amenities', __name__, url_prefix='/facility_amens')```
>
- GET ```/<int:facility_id>/amenities/secure```
    - *Functionality*: Retrieve all amenities for a specified facility by a logged-in owner
    - *Route*: ```@facility_amenities.route('/<int:facility_id>/amenities/secure', methods=['GET'])```
    - *JSON Request Parameters*: None
    - *Expected Response*:
    ![amensretrieve](/docs/amensroute1.png)
>
- PUT / DELETE ```/<int:facility_id>/amenities/secure```
    - *Functionality*: Update only amenities respective to owned facility for logged-in owner
    - *Route*: ```@facility_amenities.route('/<int:facility_id>/amenities/secure', methods=['PUT'])```
    - *JSON Request Parameters*: specific amenity_names owner wishes to add/remove
    - *Expected Response*: 
    ![amensupdate](/docs/amensroute2.png)
    ![amensupdate](/docs/amensroute2a.png)
    >
    ** An owner cannot create new amenities therefore there is no functionality for a route that allows this. The amenities are prepopulated at time of database initialization - once they are created, they are not created again. 
    >
    I chose to include amenities in this way so that owners could not say "swim_spa" as an amenity, rather either "pool" or "spa". If every owner could create amenities with no naming convention, there would more than likely be many of the same amenities, however named differently. This would render querying by amenities useless, disorganized, and redundant.

### Promotions endpoints - 
blueprint: ```promotions = Blueprint('promotions', __name__, url_prefix='/promotions')```
- POST ```/<int:facility_id>/secure```
    - *Functionality*: Create a new promotion
    - *Route*: ```@promotions.route('/<int:facility_id>/secure', methods=['POST'])```
    - *JSON Request Parameters*: name, start_date, end_date, discount_percent
    - *Expected Response*:
    ![createpromos_route1](/docs/promosroute1.png)
    ![createpromos_route1](/docs/promosroute1a.png)
>
- PUT ```/<int:facility_id>/<int:promotion_id>/secure```
    - *Functionality*: Update a promotion for a specific facility of a logged-in owner
    - *Route*: ```@promotions.route('/<int:facility_id>/<int:promotion_id>/secure', methods=['PUT'])```
    - *JSON Request Parameters*: any promotions_fields owner wishes to change
    - *Expected Response*:
    ![updatepromos_route2](/docs/promosroute2.png)
    ![updatepromos_route2](/docs/promosroute2a.png)
>
- DELETE ```/<int:promotion_id>/secure```
    - *Functionality*: Delete a single promotion for a selected facility by a logged-in owner
    - *Route*: ```@promotions.route('/<int:promotion_id>/secure', methods=['DELETE'])```
    - *JSON Request Parameters*: None
    - *Expected Response*:
    ![promosdelete](/docs/promosroute3.png)
    >
    ** I chose not to create a specific endpoint to retrieve just the promotion of a specific facility as this capability is covered in the retrieval of an entire facility's details.

### Addresses endpoints - 
registered blueprint: 
    ```addresses = Blueprint('addresses', __name__, url_prefix='/addresses')```
>
- GET ```/<int:facility_id>/secure```
    - *Functionality*: Retrieve a single address for a specified facility by a logged-in owner
    - *Route*: ```@addresses.route('/<int:facility_id>/secure', methods=['GET'])```
    - *JSON Request Parameters*: None
    - *Expected Response*:
    ![address_detailsroute](/docs/addressroute2.png)
>
- PUT ```/<int:facility_id>/secure```
    - *Functionality*: Update an address for a singular facility by a logged-in owner
    - *Route*: ```@addresses.route('/<int:facility_id>/secure', methods=['PUT'])```
    - *JSON Request Parameters*: any address_fields owner wishes to update
    - *Expected Response*:
    ![address_updateroute](/docs/addressroute1.png)
    >
    ** Specific to addresses, there is no functionality to create a new address since an address must be registered with a facility at the time of facility creation (i.e. an address cannot be created for a facility retrospectively). Additionally, there is no functionality to delete an address as an address is required for every facility and a deletion of an address would compromise the data's integrity.
>
I also wanted any untracked user to be able to retrieve data from the API so I created the below public endpoints.
>
### Public endpoints: 
registered blueprint:
    ```public = Blueprint('public', __name__, url_prefix='/public')```
>
- GET ```/facilities/postcode/<string:post_code>```
    - *Functionality*: Query facilities based on post_code
    - *Route*: ```@public.route('/facilities/postcode/<string:post_code>', methods=['GET'])```
    - *JSON Request Parameters*: None
    - *Expected Response*:
    ![publicroute_1](/docs/pubroute1.png)
>
- GET ```/facilities/promotions/current```
    - *Functionality*: Query facilities based on promotion end date 
    - *Route*: ```@public.route('/facilities/promotions/current', methods=['GET'])```
    - *JSON Request Parameters*: None
    - *Expected Response*: 
    ![publicroute_2](/docs/pubroute2.png)
    ![publicroute_2](/docs/pubroute2a.png)
>
- GET ```/facilities/type/<string:facility_type>```
    - *Functionality*: Query facilities based on facility_type
    - *Route*: ```@public.route('/facilities/type/<string:facility_type>', methods=['GET'])```
    - *JSON Request Parameters*: None
    - *Expected Response*: 
    ![publicroute_3](/docs/pubroute3.png)
>
- GET ```/amenities/<string:amenity_ids>```
    - *Functionality*: Query facilities based on an amenity list
    - *Route*: ```@public.route('/amenities/<string:amenity_ids>', methods=['GET'])```
    - *JSON Request Parameters*: None
    - *Expected Response*: 
    ![publicroute_4](/docs/pubroute4.png)
    ![publicroute_4](/docs/pubroute4a.png)
>
- GET ```/facilities/hours/<string:opening_time>/<string:closing_time>```
    - *Functionality*: Query all facilities that are open for certain hours
    - *Route*: ```@public.route('/facilities/hours/<string:opening_time>/<string:closing_time>', methods=['GET'])```
    - *JSON Request Parameters*: None
    - *Expected Response*: 
    ![publicroute_5](/docs/pubroute5.png)
    ![publicroute_5](/docs/pubroute5a.png)
>
- GET ```/facilities/<string:facility_type>/hours/<string:opening_time>/<string:closing_time>```
    - *Functionality*: Query all facilities of a specific type that are also open for certain hours
    - *Route*: ```@public.route('/facilities/<string:facility_type>/hours/<string:opening_time>/<string:closing_time>', methods=['GET'])```
    - *JSON Request Parameters*: None
    - *Expected Response*:
    ![publicroute_6](/docs/pubroute6.png)
>
- GET ```/facilities/postcode/<string:post_code>/amenities/<string:amenity_ids>```
    - *Functionality*: Query all facilities in a specified post_code that have the specified amenities
    returns all facilities within post_code and also have desired amenities
    - *Route*: ```@public.route('/facilities/postcode/<string:post_code>/amenities/<string:amenity_ids>', methods=['GET'])```
    - *JSON Request Parameters*: None
    - *Expected Response*:
    ![publicroute_7](/docs/pubroute7.png)
    ![publicroute_7](/docs/pubroute7a.png)
>
- GET ```/facilities/postcode/<string:post_code>/promotions```
    - *Functionality*: Query all facilities that are running promotions in a specified post_code
    returns all facilities within post_code that are also running promotions
    - *Route*: ```@public.route('/facilities/postcode/<string:post_code>/promotions', methods=['GET'])```
    - *JSON Request Parameters*: None
    - *Expected Response*:
    ![publicroute_7](/docs/pubroute8.png)
>
- GET ```/facility_types```
    - *Functionality*: Retrieve a list of all facility types and their id assignments (facility_type_id is required as a ```fkey``` in the facilities entity, so must be included at time of facility creation)
    - *Route*: ```@facility_types.route('/', methods=['GET'])```
    - *JSON Request Parameters*: None
    - *Expected Response*:
    ![facility_types_all](/docs/facility_typesroute1.png)
>
- GET ```/all_amenities```
    - *Functionality*: Retrieve all amenities and their ids
    - *Route*: ```@amenities.route('/all_amenities', methods=['GET'])```
    - *JSON Request Parameters*: None
    - *Expected Response*:
    ![amens_route4](/docs/amensroute4.png)
>

## 1. Purpose:
The FitnessFinder API is an application that intends to mitigate and ease the process of finding a new fitness center. Often, when searching for a new gym or studio, one must travel to the prospective facilities to check what amenities they have, call up to find out the hours, and just to gain general info. This application aims to make this process more streamlined for people by having this info all in one place, thus making it easier to compare facilities and find one that best suits their needs. 
>
The API also has the capability for owners to have their accounts in which they manage their facility information - this is a lot better than going thru the neverending chains of Google to get your information displayed. With the facility owner having more control over their own facility details, clients will have an easier time making accurate decisions.

## 2. Resolution:
This problem needs to be solved because with the evergrowing population of fitness centers, gyms, pilates studios, etc. it can be overwhelming finding something that suits all your needs. This application congregates all the relevant data into one place making it much easier to do preliminary research when taking the first step towards regaining physical fitness. Upgrades of this app may include a user portal in which users can review and rate facilities making it even easier to see which gyms may be suitable for the prospective gym-goer's needs. At this stage, the api only has capabilities to allow owners to login and manage their facility's details however this is ideal for a preliminary api as people will be able to use it freely without making yet another account for something they may only use once. 

## 3. Database System:
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

## 4. ORM Basics:
"ORM stands for object-relational mapping, where objects are used to connect the programming language on to the database systems, with the facility to work SQL and object-oriented programming concepts."[^1] There are many different ORMs which link better to specific object-oriented programming languages and frameworks such as SQLAlchemy and Flask, or Django ORM and Django (language).
>
### Functionalities:
> Object-relational mapping (ORM) is a technique that creates a layer between the language and the database, helping programmers work with data without the OOP paradigm...An object-relational mapper provides an object-oriented layer between relational databases and object-oriented programming languages without having to write SQL queries. It standardizes interfaces reducing boilerplate and speeding development time... 
>
> ORMs translate this data and create a structured map to help developers understand the underlying database structure. The mapping explains how objects are related to different tables. ORMs use this information to convert data between tables and generate the SQL code for a relational database to insert, update, create and delete data in response to changes the application makes to the data object. Once written, the ORM mapping will manage the application’s data needs and you will not need to write any more low-level code.
[^7]

> An ORM will convert the result of a database query into a class within our application. The selected columns will map to the class properties. On the other hand, if you push data towards the database, an ORM will map the properties of a class into columns of a table. When people say ORM, they refer to a framework that implements this technique. Some of the most frequently used ORM frameworks:  Entity Framework, Hibernate, Sequelize, and SQLAlchemy.[^6]

### Benefits:
- Productivity:
"Using a tool like an ORM that automatically generates the data-access code saves tremendous development time that does not add value to the application. In some cases, the ORM can write 100 percent of the data-access code for the application. The ORM can also help you keep track of database changes making it easier to debug and change the application in the future."[^7] 
    > 
    Essentially, by forgoing having to write out all the SQL queries in SQL language, developers can save time and focus more on the functionality of their code rather than SQL's syntactic requirements. 
    >
    "[Using an ORM] makes the application independent of the database management system being used in the backend, and so you can write a generic query. In case of migrating to another database, it becomes fairly a good deal to have ORM implemented in the project."[^1]
- Application Design:
" If you use an ORM to manage the data interface, you do not need to create the perfect database schema in advance. You will be able to change the existing interface easily. Separating the database table from the programming code also allows you to switch out data for different applications."[^7] Once the Models are written, that's it - there's no need to rewrite it in any other locations, making it easier to maintain as its DRY. Models also use Object-Oriented Programming (OOP) so using an ORM is effectively extending and inheriting from the Models. Essentially, ORMS can be used for any O-O language.
- "Reduced Testing:
Since the code generated by the ORM is well-tested, you do not need to spend as much time testing the data-access code. Instead, you can focus on testing the business logic and code."[^7]
- SQL language:
In using an ORM like SQLAlchemy, the developer does not need to know SQL language. "Queries via ORM can be written irrespective of whatever database one is using in the back end. This provides a lot of flexibility to the coder. This is one of the biggest advantages offered by ORMs."[^1] Additionally, "If you take the time to learn SQL queries and the theory behind sql, there is nothing a Model cannot do. You can write very complex queries which have the same performance if you were to write them directly in sql, however not all developers take the time to learn SQL."[^8]
- Flexible relationships:
ORMS typically allow for flexible entity relations, and tend to work coherently if the database requires "relations like 1: m, n: m and lesser 1:1"[^1]. 
- Security:
When using an ORM, a developer can better and more adequately protect the queries via sanitization. This makes certain breaches such as SQL injection a lot less likely therefore providing more built-in security to a developer's application. 
>
Overall using an ORM can seamlessly integrate the database with the application codebase allowing for easy changes to queries without having to have a vast knowledge of SQL. An ORM also allows for changing up the entire application without having to duplicate access code via a dynamic-link library. ORMs such as SQLAlchemy allow the developer to define production or development mode in which case there is a built-in debugger that is available for use upon correct configuration. All of these features make it easier for programmers to build out applications in a language they're familiar with, without getting to stuck on SQL queries themselves. Development can in turn focus more on business logic rather than SQL syntax further bolstering the application as functional in all ways.
>

## 6. Entity Relationship Diagram:
![erd](/docs/final_erd.png)

## 7. Third Party Services:
- Flask: 
    "Flask is a lightweight Python web framework that provides useful tools and features for creating web applications in the Python Language."[^9]
>
- SQLAlchemy: 
    
    "SQLAlchemy is an SQL toolkit that provides efficient and high-performing database access for relational databases...It gives you access to the database’s SQL functionalities. It also gives you an Object Relational Mapper (ORM), which allows you to make queries and handle data using simple Python objects and methods."[^9] 
    > 
    "...Instead of hiding away SQL and object relational details behind a wall of automation, all processes are fully exposed within a series of composable, transparent tools. The library takes on the job of automating redundant tasks while the developer remains in control of how the database is organized and how SQL is constructed."[^10]
>
- Flask-SQLAlchemy: 
    "Flask-SQLAlchemy is a Flask extension that makes using SQLAlchemy with Flask easier, providing you tools and methods to interact with your database in your Flask applications through SQLAlchemy."[^9] Flask-SQLAlchemy is used in this application to effectively merge both flask and sqlalchemy - by importing this module into the application, flask is enabled to use the full range of functionality from SQLAlchemy and access the database using simplistic and familiar object-oriented code (python). It provides an interface for interacting with the database using SQLAlchemy, which is an Object Relational Mapper (ORM) for Python.
>
    Using Flask-SQLAlchemy, this api was able to define its database as Python classes, known as Models. The models are a representation of the tables in the database. SQLAlchemy allows for querying and CRUD functionality (create, read, update, delete) using methods such as ```db.session.add()```, ```db.session.commit()```, and ```db.session.query()```. Another thing the library is able to handle, is database migration meaning it allows for easy changes - once the schema is changed, the database evolves with it.
>
- Flask-Bcrypt: 
    "Flask bcrypt is defined as a flask extension that enables users with utilities related to bcrypt hashing...The bcrypt is an adaptive function which can be deliberately made slower so that application is resistant to brute force attacks."[^11] 
    >
    This api uses Flask-Bcrypt as a package import in order to hash passwords securely and compare them with stored hashes. This can be seen in the ```/login``` endpoint where an owner must enter their password. The ```bcrypt.check_password_hash``` is a significant helper function in doing so, which is imported with the Flask-Bcrypt package.
>
- Flask-JWT-Extended: 
    Flask-JWT-Extended is a Flask extension that provides JWT-based authentication for your Flask API. It allows you to create and verify JWT tokens, which can be used to protect your API endpoints and authenticate users.  This can be seen being used on all the ```/secure``` endpoints in which an owner must be authenticated prior to any information being released. 
    >
    Functions such as ```create_access_token``` are an integral part of authenticating owners - this generates a JSON Web Token (JWT) access token for a given identity (owner) and sets an expiration time for the token. The token can then be used in the payload request data to access certain information and routes, furthering adding a protective layer to the api.
>
- Flask-marshmallow: 
    "Flask-Marshmallow is a thin integration layer for Flask (a Python web framework) and marshmallow (an object serialization/deserialization library) that adds additional features to marshmallow."[^12]
    ![flask-marshmallow](/docs/flask-marshmallow.png)[^13]
    >
    For example, upon app configuration, this api involves the flask-marshmallow package in order to access the Schema class. This is especially important and useful in serializing and deserializing the data - ensuring that the data is in the correct format, that its not missing any required fields, etc. The Schema allows the programmer to define the structure of the data.
>
- Marshmallow-sqlalchemy:
    Marshmallow-sqlalchemy is a package that provides integration between Marshmallow and SQLAlchemy, making it easy to serialize SQLAlchemy models to and from JSON format. This is especially used upon returning data from the database in a way that Flask can read.
    >
    This package also allows for easier handling of serialization and deserialization of the app's models. 
    >
    ** Note: To fully enable SQLALchemy integration, both Flask-SQLAlchemy and Marshmallow-sqlalchemy must be imported. Additionally, Flask-SQLAlchemy must be initialized before Flask-Marshmallow.
>
- Psycopg2: 
    "Psycopg is the most popular PostgreSQL adapter used in  Python.  Its works on the principle of the whole implementation of Python DB API 2.0 along with the thread safety (the same connection is shared by multiple threads). It is designed to perform heavily multi-threaded applications that usually create and destroy lots of cursors and make a large number of simultaneous INSERTS or UPDATES."[^14]
    >
    This package allows an application to connect to a PostgreSQL database and perform SQL queries and commands, and retrieve results. 

## 8. Models:
Models are used as a way for the database to understand how to build itself. It's important that programmers use models according to how they want all their entities to relate and interact with each other. Foreign keys are used to establish relations between two tables in a relational database - the foreign key constraint ensures that the values in the foreign key column(s) of a table always match the values in the corresponding primary key or unique key column(s) of the referenced table. Foreign keys help maintain data integrity and consistency.

In this api, I have a model for all of my database tables (except in the instance where I used a join table between facilities and amenities instead):
- addresses model
    - The addresses model was required to relate to the ```facilities``` and the ``post_codes`` model. However, in order to achieve this, it was only necessary to associate the ```post_codes``` directly to the addresses via foreign key (as addresses is related to facilities, via its own fkey).
    >
    - To define the foreign key in the addresses table to link ```post_codes```, this piece of code is used. 
        >
        ```post_code_id = db.Column(db.Integer, db.ForeignKey("post_codes.id"), nullable=False)```
        >
        This lets the ```addresses``` model know that there needs to be a column (id) in the addresses table that is populated from the ```post_codes``` table. The column has the constraint ```nullable=False``` meaning it cannot be empty.
        >
    - To achieve any sort of querying between the two tables, a relationship needs to be defined:
        >
        ```post_code = db.relationship('PostCode', backref='post_code_addresses')```
        >
        This piece of code creates the one-to-many relationship between post codes and addresses. A ```PostCode``` can have multiple associated ```Facility``` addresses, but each ```Facility``` address can only belong to one ```PostCode```. 
        >
        The backref to ```post_code_addresses``` provides a way to access all ```Facility``` addresses that are associated with a particular ```PostCode```.
>
- amenities model
    - The ```amenities``` model does not have any direct relations to any other tables.
- facilities model
    - The ```facilities``` model is the main table which houses the information of some connecting information of some of the other tables. It has three foreign keys:
    >
    ```python
    facility_type = db.Column(db.Integer, db.ForeignKey("facility_types.id"), nullable=False)
    ```
    ```python
    owner_id = db.Column(db.Integer, db.ForeignKey("owners.id"), nullable=False)
    ```
    ```python
    address_id = db.Column(db.Integer, db.ForeignKey("addresses.id"), nullable=False)
    ```
    - These key definitions establish a link between the ```facilities``` table and the ```facility_types```, ```owners```, and ```addresses``` table via their unique identifiers. 
    >
    - Just as in the ```addresses``` table, the foreign key relationships defined above specify the constraints and point to where exactly the foreign key is being pulled from. All three definitions are pulling the unique id from their respective table and populating as a foreign key in the ```facilities``` table. This is to establish a proper and recognized link between the tables for querying purposes in the database.
    >
    - The facility model also needs to signify to the database what sort of relationship a ```Facility``` object has with the other objects (```Promotion```,```Address```, ```Owner```, ```Amenity```).
    >
    ```python
    # Add the relationships directions to other models
    promotions = db.relationship('Promotion', backref='facility_promotions', lazy=True, cascade="all, delete-orphan")
    ```
        This line sets up a one-to-many relationship between the ```Facility``` model and the ```Promotion``` model, using the "promotions" attribute in the ```Facility``` model to access all associated ```Promotion``` objects. It backreferences the "facility_promotions" attribute in the ```Promotion``` model to access the Facility object that the Promotion belongs to.
    >
    ```python
    address = db.relationship('Address', backref='facility')
    ```
    - The above line sets up a one-to-one relationship between the ```Facility``` model and the ```Address``` model, using the "address" attribute in the ```Facility``` model to access the associated ```Address``` object, and the "facility" attribute in the ```Address``` model to access the Facility object that the Address belongs to.
    >

    ```python
    owner = db.relationship('Owner', backref="owner_facilities", cascade="all, delete-orphan", single_parent=True)
    ```
    - This above line sets up the one-to-many relationship between the ```Owner``` model and the ```Facility``` model. The backreference parameter creates an ```owner_facilities``` attribute on the ```Owner``` model that allows us to access all facilities associated with a particular owner. 
        >
        Additionally, the cascade and single-parent parameter assist in the deletion order (cascade meaning when an owner is deleted, all its associated facilities will also be deleted) and general integrity maintenance (single-parent meaning a facility can only have one owner, ensuring that the db does not have multiple owners associated with the same facility).
    >
    ```python
    amenities = db.relationship('Amenity', secondary=facility_amenities, lazy='subquery', backref=db.backref('facilities', lazy='dynamic'))
    ```
    - This line defines a many-to-many relationship between the ```Facility``` model and the ```Amenity``` model using the ```facility_amenities``` association table. It allows for access to all facilities associated with a particular amenity.
        >
        The backref denotes that the developer can access all amenities associated with a particular facility. the ```lazy='subquery'``` specifies that related objects should be loaded using a subquery statement, which can improve performance compared to the default lazy loading strategy. 
        >
        The second ```lazy='dynamic'``` specifies that the query should return a dynamic object instead of the default list object. This means that instead of returning a list of amenities, a query object is returned that can be further refined with filters, orderings, etc. 
>
- facility_types model
    - The facility_types model only needed to be linked to specific facilities. This line:  
    ```facilities = db.relationship('Facility', backref='facility_types', lazy=True)```
    defines a one-one relationship between the ```FacilityType``` model and the ```Facility``` model. 
        >
        It creates a backref ```facility_types``` in the ```Facility``` model which allows access to the ```FacilityType``` object(s) that a specific ```Facility``` object is associated with. Effectively, with this line, we can query a facility's facility_type.
        >
        The ```lazy=True``` parameter indicates that the associated ```FacilityType``` object(s) should be loaded in the same query that loads the ```Facility``` object(s) which can reduce the number of queries required to get certain information.
    >
- owners model
    - ```facilities = db.relationship('Facility', backref="facility_owners", cascade="all, delete-orphan")```
        >
         It specifies that each ```Owner``` can have multiple ```Facility``` objects associated with it, and each ```Facility``` object belongs to only one ```Owner```. 
         >
         The backreference helps to access the ```Owner``` objects associated with a given ```Facility```.
        >
        The cascade argument specifies that when an ```Owner``` object is deleted, all of the associated ```Facility``` objects should be deleted as well (delete-orphan). This ensures that there are no orphaned ```Facility``` objects in the database. This was an important parameter to include as this is way I wanted to design the database - no Facility could exist without an Owner to avoid stale data.
>
- post_codes model
    - ```addresses = db.relationship('Address', backref='address_post_codes')```
        >
        This creates a one-to-many relationship between ```Address``` and ```PostCode```, where a single post code can be associated with multiple addresses. The backreference allows us to access ```PostCode``` object associated with an ```Address``` via ```address_post_codes```.
    >
    - Post codes were not included in the address table as an attribute to avoid data redundancy and to further maintain third normalized form. Since multiple addresses could share the same post_code, it was best to move post_codes to its own table and associate the two entities via a foreign key.
>
- promotions model
>
```python
# Add the foreign keys in the Promotions model
facility_id = db.Column(db.Integer, db.ForeignKey("facilities.id"), nullable=False) 
# Add the relationships directions to other models
facility = db.relationship('Facility', backref='facility_promotions')
```
>
These two lines define a many-to-one relationship between the ```Promotion``` and the ```Facility``` model. The first line defines the foreign key column called ```facility_id``` which is present in the ```Promotions``` table. This is in order to reference which ```Facility``` is linked to which ```Promotion``` via unique identifier.
>
The backref argument creates a ```facility_promotions``` attribute in the ```Facility``` model that is a query object for all promotions associated with that facility.


## 9. Database Relations:
The FitnessFinder API intends to implement its database relations based off the project's preliminary entity relationship diagram. 

The relations can be elaborated on as follows:

- *Facilities* 
can be only one ```facility_type```. They can also run 0 to multiple *promotions* (optional). A facility can have many *amenities* as shown thru the join table ```facility_amenities```. A facility can have only one *address*.
>
- *Facility_types* 
can be attributed to 0 or many ```facilities```. Facility types has the option to have 0 facilities as this is a prepopulated attribute in the database, in which is not required to have any facilities linked to at time of seeding.
>
- *Promotions* 
can be run at one facility (if the facility is independent) however if the facility is a chain, the promotion can be held across their multiple locations.
>
- *Amenities* 
has a many-to-many relationship with *facilities*, meaning many amenities can be present at many facilities - this relationship is defined thru the join table ```facility_amenities```. There is no associated model to the ```facility_amenities ``` table.
>
- *Addresses* 
has a one-to-one relationship with ```facilities``` as only one address can be attributed to one facility location. ```Addresses``` has a one-to-one relationship with ```post_codes``` as an address can only have one ```post_code```.
>
- *Post_codes* 
has an atleast-one-to-one relationship with ```addresses```. A postcode can have multiple addresses within that ```post_code```. The relationship is atleast-one from post_codes because there will always be atleast one address with that specific post_code if the address is entered into the database. 
    >
    ```Post_codes``` was moved to a separate table to maintain data integrity and reduce redundancy. By separating post_codes, addresses are able to link accordingly via fkey rather than having repeat *post_codes* in the *addresses* table.

## 10. Project Management
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
Between the second ERD and the final ERD, there was duplication with post_codes as a foreign key in the ```facilities``` table - there was also an entity relation to match however this was removed prior to the image capture. Additionally, in the ```facilities``` table, ```hours_of_op``` was split into two values (```opening_time``` and ```closing_time```) to allow for easier and more accurate time comparisons and querying of opening hours.
>
```promotions``` had a name attribute added, so that owners could specify the title of their promotion.
>
```facility_amenities``` had a column added ```has_amenity``` to enforce the boolean type of the amenities, as well as just to make it more clear in the database what the ids are representing.
>
The ```addresses``` table was also filled out appropriately with relevant attributes to ensure more specificity upon data entries which in turn allows for more precise filtering options.
>
Lastly, a space for ```owners``` to input their mobile number as well as name in case of a 2-factor authentication being released in future api updates.
>
### 10. Planning
To better assist me in my project planning, I chose to use **Trello** to manage my tasks. The below is the beginning trello board that I started with.
>
![project_start](/docs/trello_board1.png)
>
I chose to lay out my tasks with *preliminary* referring to environment and app structure setup, and *tasks* referring to coding actions. I labelled them with colors to signify the difficulty/time I estimated it would take, with green being quick and relatively easy, orange taking incrementally more time and requiring a little more thinking, and lastly red to symbolize tasks that required some hours. I then accordingly assigned due dates for all of them to keep on track. 

![cli_checklist](/docs/trello_cli.png)
![controller_checklist](/docs/trello_controllers.png)
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
>
Please see my progress tracking below:
>
Progress as of March 8
![project_mid](/docs/trello_board3.png)
>
Progress as of March 10
![project_mid](/docs/trello_board4.png)
>
Progress as of March 13
![project_mid](/docs/trello_board5.png)
>
Progress as of March 18
![project_end](/docs/trello_board6.png)
>
Progress as of March 19
![project_end](/docs/trello_board7.png)
>
Towards the end of the project, my progress slowed down as certain things took more time to figure out how to get working exactly as I wanted to. I found a lot of times tweaking little things here and there required great focus, as you'd have to migrate the changes in multiple locations. However, if the alteration did not go as planned, the code tended to be more mangled than desired. I also was not able to give error handling as much time as I would have liked however I think it handles well for a first-iteration api rollout.
>
>
### Sources
[^1]: EDUCBA. (2020). What is ORM? | How ORM Works? | A Quick Glance of ORM Features. [online] Available at: https://www.educba.com/what-is-orm/.


[^2]: Bitnine.net. (2023). [online] Available at: https://bitnine.net/blog-postgresql/advantages-of-postgresql/?ckattempt=1 [Accessed 27 Jan. 2023].


[^3]: Sharda, A. (2021, April 28). What is PostgreSQL? Introduction, Advantages & Disadvantages [Review of What is PostgreSQL? Introduction, Advantages & Disadvantages]. LinkedIn Pulse. https://www.linkedin.com/pulse/what-postgresql-introduction-advantages-disadvantages-ankita-sharda


[^4]: Anon, (n.d.). PostgreSQL Transaction. [online] Available at: https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-transaction/#:~:text=A%20PostgreSQL%20transaction%20is%20atomic [Accessed 27 Jan. 2023].


[^5]: Dhruv, S. (2019, May 15). PostgreSQL Advantages and Disadvantages [Review of PostgreSQL Advantages and Disadvantages]. https://www.aalpha.net/blog/pros-and-cons-of-using-postgresql-for-application-development/



[^6]: Lubenov, L. (2021). Object-Relational Mapping (ORM) [Dev Concepts #19.2]. [online] SoftUni Global. Available at: https://softuni.org/dev-concepts/object-relational-mapping-orm/ [Accessed 13 Mar. 2023].


[^7]: Liang, M. (2021). Understanding Object-Relational Mapping: Pros, Cons, and Types. [online] AltexSoft. Available at: https://www.altexsoft.com/blog/object-relational-mapping/.


[^8]: midnite.uk. (n.d.). The pros and cons of Object Relational Mapping (ORM). [online] Available at: https://midnite.uk/blog/the-pros-and-cons-of-object-relational-mapping-orm#:~:text=ORMs%20can%20drastically%20improve%20development.


[^9]: www.digitalocean.com. (n.d.). How to Use Flask-SQLAlchemy to Interact with Databases in a Flask Application | DigitalOcean. [online] Available at: https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application.


[^10]: www.sqlalchemy.org. (n.d.). Philosophy - SQLAlchemy. [online] Available at: https://www.sqlalchemy.org/philosophy.html [Accessed 19 Mar. 2023].


[^11]: EDUCBA. (2021). Flask bcrypt | How bcrypt Works in Flask | Examples. [online] Available at: https://www.educba.com/flask-bcrypt/ [Accessed 19 Mar. 2023].


[^12]: PyPI. (2020). flask-marshmallow. [online] Available at: https://pypi.org/project/flask-marshmallow/#:~:text=Flask%2DMarshmallow%20is%20a%20thin [Accessed 19 Mar. 2023].


[^13]: flask-marshmallow.readthedocs.io. (n.d.). Flask-Marshmallow: Flask + marshmallow for beautiful APIs — Flask-Marshmallow 0.14.0 documentation. [online] Available at: https://flask-marshmallow.readthedocs.io/en/latest/.


[^14]: GeeksforGeeks. (2022). Introduction to Psycopg2 module in Python. [online] Available at: https://www.geeksforgeeks.org/introduction-to-psycopg2-module-in-python/ [Accessed 19 Mar. 2023].


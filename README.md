# Crypto Exchange ETL

This is a simple app to get both realtime and historical data from [Nomics](https://nomics.com) about crypto-currencies.

It shows how to create a backend service to connect to any web data source and save the data in a database.
The data in the source could be made available by:
- REST API
- Manual historical File download

It follows a service-oriented architectural (SOA) design.

It uses the nice little ETL framework called [Bonobo](https://www.bonobo-project.org/) under the hood.

**This project is still under heavy development**

## Why service-oriented architectural (SOA) design

Service oriented architecture makes it easy to connect actual feature requests with the actual code that is written.
Many a time, software requirements are structured in typically a service-oriented manner.
For example.
- User can see realtime data about bitcoin
- User can see realtime data about etherium
- User can view historical data about bitcoin

When we have source code that follows the exact manner these requirements are laid out, it is easy to comprehend for 
anyone really.

For example, for the above example, each of those requirements will have a single pipeline, each having its own
independent folder.

It is even easy to transfer that architecture into a stable microservice architecture if there is ever need to do so.

Watch [this talk by Alexandra Noonan](https://www.youtube.com/watch?v=hIFeaeZ9_AI) and [this other one by Simon Brown](https://www.youtube.com/watch?v=5OjqD-ow8GE)

## Dependencies

- [Python3.6](https://www.python.org/downloads/release/python-368/) (attempting to use > 3.6 may cause weird errors)
- [Bonobo ETL](https://www.bonobo-project.org/)
- [SqlAlchemy](https://www.sqlalchemy.org/)

## How to set up Debian server for Selenium Chrome driver

- Install an in-memory display server (xvfb)

``` 
#!bash

sudo apt-get update
sudo apt-get install -y curl unzip xvfb libxi6 libgconf-2-4
```

- Install Google Chrome

``` 
#!bash

sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable
```

## How to Run (Example commands for Linux)
- Ensure you have Google Chrome installed. For debian servers, see instructions under the 
title "How to set up Debian server for Selenium Chrome driver"

- Clone the repo

```
#!bash

git clone <url_of_repo>
```

- Create a virtualenv

``` 
#! bash

cd stock-exchange && python3.6 -m venv env
```
- Activate the virtual environment

``` 
#!bash

source env/bin/activate

```

- Copy the `.example.env` file to `.env` and update the variables in there. You might need to get an api key from [Nomics](https://p.nomics.com/pricing)

```
#!bash

cp .example.env .env
```

- Run the command

```
#!bash

python main.py
```

- Check the database (basing on the `LIVE_DB_URI` 
and `HISTORICAL_DB_URI` you set in the `.env` file) for the records added.



## ToDo

- [x] Make the extractors keep running forever at a given interval
- [x] Change to service-oriented architecture
- [x] Add selenium source (web scraping)
- [x] Make each microservice independent of other microservices
- [ ] Add transformation types
- [ ] Add websocket destination
- [ ] Add REST api destination
- [ ] Add RabbitMQ destination
- [ ] Add kafka destination
- [ ] Add automated tests for the core
- [ ] Add automated tests for each service

## Design Ideas

- Make each pipeline a different service e.g.:
 - NOMICS_REST_API -> POSTGRES_DATABASE -> REST_API
 - NOMICS_EXPORT_SECTION -> CSV -> POSTGRES_DATABASE -> REST_API
 - NOMICS_REST_API -> DISK_CACHE -> WEBSOCKET_SERVER
 
- For realtime data, save the data in a fanoutcache of the diskcache with a preconfigured timeout,
then have fast api websocket send data to the clients

## Architecture

Here is the folder structure

.
├── app
│   ├── core
│   │   ├── controllers
│   │   │   ├── file_download_site_to_db
│   │   │   └── rest_api_to_db
│   │   ├── destinations
│   │   │   └── database
│   │   ├── sources
│   │   │   ├── file_download_site
│   │   │   └── rest_api
│   │   └── utils
│   └── services
│       └── yahoo_finance
│           ├── export_site_to_db
│           │   ├── controllers
│           │   ├── destinations
│           │   │   └── yahoo_finance_historical_db
│           │   │       └── models
│           │   └── sources
│           │       └── base
│           └── rest_api_to_db
│               ├── controllers
│               ├── destinations
│               │   └── yahoo_finance_db
│               │       └── models
│               └── sources
└── assets
    └── csv


### [main.py](./main.py)

This is the entry point for the application. It is where bonobo graph is initialized.

### [Core](./app/core)

The core has all reusable code that forms the framework this app is following
It is composed of three main sections (the services also follow the same structure)

#### [Sources](./app/core/sources)

This contains all the possible data sources we can have for such a project. These include:

##### [REST API](./app/core/sources/rest_api)
This is a package that deals with making requests to a REST API, at say a given interval and returning the data in
JSON format

##### [File download Site](./app/core/sources/file_download_site)
This is a package that deals with downloading files (CSVs) from a given web site using a web scrapper
and then converting the returned data into JSON format


#### [Destinations](./app/core/destinations)

This contains all the possible data sinks we can have in such a project. After data is processed, it is sent to 
any of these destinations. These include:

##### [Database](./app/core/destinations/database)

This package deals with making connections to Relational Databases like PostgreSQL, MySQL, SQLite etc.
It also deals with saving data into those databases


#### [Controllers](./app/core/controllers)

This contains all the possible pipelines for the data e.g. from REST API to database. It is the 
controller that manages the source and the destination. It is the one whose steps of `extract`, `transform`,
and `load` that Bonobo graph runs in the `main.py` file.

It includes:

##### [File Download Site to Database](./app/core/controllers/file_download_site_to_db)

This package connects the export site source to the database destination.

##### [REST API to Database](./app/core/controllers/rest_api_to_db)

This package connects the REST API source to the database destination.

### [Services](./app/services)

The service folder is contains services that are split down into more services until the point of the smallest service
that contains a `controller`, a `source` and a `destination`

The services folder contains independent services that can be extracted each into their own app.
In turn each service contains a set of microservices that depend on only one package/module i.e. `abstract` in that service.

Separation of microservices within services is possible by copying `abstract` together with that service folder
and the `core` and the `main.py`file. The latter would have to be edited to contain only that given service.


## Acknowledgements

- The tutorial [How to Setup Selenium with ChromeDriver on Debian 10/9/8](https://tecadmin.net/setup-selenium-with-chromedriver-on-debian/) was very useful when deploying the app
on a Debian server
- Free [Crypto Market Cap & Pricing Data Provided By Nomics.](https://nomics.com/)

## License

Copyright (c) 2020 [Martin Ahindura](https://github.com/Tinitto) Licensed under the [MIT License](./LICENSE)

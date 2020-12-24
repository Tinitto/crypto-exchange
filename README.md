# Market Exchange ETL

This is a simple app to get both realtime and historical data from a number of market data sources including:

- [Nomics](https://nomics.com)
- [Tokyo Commodity Exchange](https://www.tocom.or.jp/)
- [Finnhub](https://finnhub.io/)
- [IEX Cloud](https://iexcloud.io/s/7b028b07)
- [Blockchain](https://www.blockchain.com/)

It shows how to create a backend service to connect to any web data source and save the data in a database.
The data in the source could be made available by:
- REST API
- Websocket
- Manual historical File download

It follows a service-oriented architectural (SOA) design.

It uses the nice little ETL framework called [judah](https://github.com/sopherapps/judah) which is uses [Bonobo](https://www.bonobo-project.org/) under the hood.

**This project is still under heavy development**

## Why service-oriented architectural (SOA) design

Service oriented architecture makes it easy to connect actual feature requests with the actual code that is written.
Many a time, software requirements are structured in typically a service-oriented manner.
For example.
- User can see realtime data about bitcoin
- User can see realtime data about Ethereum
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
- [Selenium](https://selenium-python.readthedocs.io/)
- [requests](https://requests.readthedocs.io/en/master/)
- [judah](https://github.com/sopherapps/judah)
- [postgreSQL](https://www.postgresql.org/download/)

## How to set up Debian server for Selenium Chrome driver

- Install an in-memory display server (xvfb)

```bash

sudo apt-get update
sudo apt-get install -y curl unzip xvfb libxi6 libgconf-2-4
```

- Install Google Chrome

```bash

sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable
```

## How to Run (Example commands for Linux)
- Ensure you have Google Chrome installed. For debian servers, see instructions under the 
title "How to set up Debian server for Selenium Chrome driver"

- Clone the repo

```bash
git clone https://github.com/Tinitto/market_exchange.git
```

- Create a virtualenv

```bash

cd market_exchange && python3 -m venv env
```
- Activate the virtual environment

```bash

source env/bin/activate

```

- Copy the `.example.env` file to `.env` and update the variables in there. 
You might need to get API keys from:
 - [Nomics](https://p.nomics.com/pricing)
 - [IEX Cloud](https://iexcloud.io/console/tokens)
 - [Blockchain](https://exchange.blockchain.com/settings/api)
 - [Finnhub](https://finnhub.io/dashboard)

```bash
cp .example.env .env
```

- Run the command

```bash
python main.py
```

- Check the databases (basing on the settings in the `.env` file) for the records added.

### How to Run as a systemd service

- Go to the root of your user

```bash

cd ~
```

- Create a projects folder there and enter it

```bash
mkdir projects cd projects
```

- Clone the repo

```bash
git clone https://github.com/Tinitto/market_exchange.git
```

- Create a virtualenv

```bash
cd market_exchange && python3 -m venv env
```

- Activate the virtual environment and install dependencies

```bash
source env/bin/activate && pip install -r requirements.txt
```

- Copy the `.example.env` file to `.env` and update the variables in there

```bash
cp .example.env .env
```

- Copy the `market_exchange.service` file to the systemd service folder

```bash
sudo cp market_exchange.service /etc/systemd/system/market_exchange.service
```

- Change the `User` and the `MARKET_XCHANGE_WORKING_DIRECTORY` variables in `/etc/systemd/system/market_exchange.service`.

```bash
sudo nano /etc/systemd/system/market_exchange.service
``` 

- Start the service

```bash
sudo systemctl start market_exchange.service
```

- Enable the service to start on start up

``` 
#!bash
sudo systemctl enable market_exchange
```

- Check the status of the service to see if it is running

``` 
#!bash
sudo systemctl status market_exchange
```

- Press `q` to exit

- Check the databases, you set in the `.env` file, for the records added.


## ToDo

- [x] Make the extractors keep running forever at a given interval
- [x] Change to service-oriented architecture
- [x] Add selenium source (web scraping)
- [x] Make each microservice independent of other microservices
- [x] Add transformation types
- [ ] Add websocket data source
- [ ] Add websocket-to-db controller
- [x] Add nomics service
- [x] Add tokyo_commodity_exchange_service
- [ ] Add iex service
- [ ] Add finnhub service
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

The service-oriented-architecture app is found in the [`services`](./app/services) package.
It follows the folder structure recommended by the [judah](https://github.com/sopherapps/judah#expected-app-system-design-and-architecture) framework.

> **The judah framework expects all applications that use it to follow a service-oriented-architecture as shown below.**  
>- The app should have a services folder (or in python, what we call package) to contain the separate ETL services, each corresponding to a given third-party data source e.g. CNN, BBC  
>- Subsequently, each ETL service should be divided up into child services. Each child service should represent a unique data flow path e.g. REST-API-to-database, REST-API-to-cache, REST-API-to-queue, export-site-to-database, export-site-to-queue etc.  
>- Each child service should be divided up into a number of microservices. Each microservice should correspond to a single dataset, e.g. 'available_capacity', 'installed_capacity' etc.  
>- Each microservice is expected to have a destination folder, a source.py file, a controller.py file and a transformers.py file.  
>- The destination folder contains the database model file to which the data is to be saved. It contains a child class of the DatabaseBaseModel class of the judah framework  
>   - The source.py file contains a child class of the BaseSource class of the judah framework. This is the class responsible for connecting to the data source (e.g. the REST API) and downloading the data from there.  
>   - The transformers.py file contains child classes of the BaseTransformer class of the judah framework. They are responsible for transforming the source data into the data that can be saved. This may involve changing field names and types, exploading the data etc.  
>   - The controller.py file contains child class of the BaseController class of the judah framework. This class is responsible for controlling the data flow from the source class, through the transformers, to the destination model.  
>- Each child service folder should contain a registry of these microservices in its __init__.py file. The registry is just a list of the controllers of the microservices.  
>- The app should have a main.py file as the entry point of the app where the Bonobo graph is instantiated and the microservice registries mentioned in the point above are added to the graph. Look at the example_main.py file for inspiration.

The folder structure as generated by th command `tree -d --matchdirs -I 'env|__pycache__'` is as shown below

``` 
.
├── app
│   └── services
│       ├── blockchain
│       │   └── rest_api_to_db
│       │       └── abstract
│       │           └── destinations
│       │               ├── blockchain_historical_db
│       │               └── blockchain_live_db
│       ├── finnhub
│       │   └── rest_api_to_db
│       │       └── abstract
│       │           └── destinations
│       │               ├── finnhub_historical_db
│       │               └── finnhub_live_db
│       ├── iex
│       │   └── rest_api_to_db
│       │       └── abstract
│       │           └── destinations
│       │               ├── iex_historical_db
│       │               └── iex_live_db
│       ├── nomics
│       │   └── rest_api_to_db
│       │       └── abstract
│       │           └── destinations
│       │               └── nomics_live_db
│       └── tokyo_commodities_exchange
│           └── export_site_to_db
│               ├── abstract
│               │   ├── destinations
│               │   │   └── tokyo_c_e_historical_db
│               │   └── sources
│               ├── quotes_by_day_session
│               │   ├── destination
│               │   └── transformers
│               ├── quotes_by_night_session
│               │   ├── destination
│               │   └── transformers
│               └── quotes_by_trade_date
│                   ├── destination
│                   └── transformers
└── assets
    ├── csv
    └── xml
```

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

##### [File download Site](./app/core/sources/export_site)
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

##### [File Download Site to Database](./app/core/controllers/export_site_to_db)

This package connects the export site source to the database destination.

##### [REST API to Database](./app/core/controllers/rest_api_to_db)

This package connects the REST API source to the database destination.

#### [Transformers](./app/core/transformers)

This contains data transformer classes that have a `run` method that expects a dictionary 
and outputs a transformed dictionary

### [Services](./app/services)

The service folder is contains services that are split down into more services until the point of the smallest service
that contains a `controller`, a `source`, a `destination` and an optional `transformers` module

The services folder contains independent services that can be extracted each into their own app.
In turn each service contains a set of microservices that depend on only one package/module i.e. `abstract` in that service.

Separation of microservices within services is possible by copying `abstract` together with that service folder
and the `core` and the `main.py`file. The latter would have to be edited to contain only that given service.


## Acknowledgements

- The tutorial [How to Setup Selenium with ChromeDriver on Debian 10/9/8](https://tecadmin.net/setup-selenium-with-chromedriver-on-debian/) was very useful when deploying the app
on a Debian server
- Free [Crypto Market Cap & Pricing Data Provided By Nomics.](https://nomics.com/)
- [Data provided by IEX Cloud](https://iexcloud.io)
- [Blockchain API](https://exchange.blockchain.com/ap)
- [Finnhub API](https://finnhub.io/docs/api)

## License

Copyright (c) 2020 [Martin Ahindura](https://github.com/Tinitto) Licensed under the [MIT License](./LICENSE)

# CryptoWatcher

Tower Research CDP Developer Hiring Challenge
Application: Crypto Watcher

Framework:
•	Django (Python Framework)
•	JQuery
•	Bootstrap

Database: SQLite3

Deployment: docker

Frontend: 
•	HTML
•	CSS
•	Ajax
•	JS

Steps:
Environment Setup –  [Using venv] [Recommended]
•	venv package of python.
•	Download source code – CryptoWatcher
•	Activate venv present inside cryptowatcher folder.
•	Pip install –r requirements.txt (optional, added venv virtual environment, it has all the necessary packages for cryptowatcher project.
•	Just run python manage.py runserver, it will start the application. No need to migrate database, already included sqlite db.
•	Browse to 127.0.0.1:8000 to view application.

Environment Setup – [Using Docker]
•	DockerFile is included with docker-compose.yml file.


Process Flow – 
•	To load data from csv file, load_data_to_db.py in /CryptoWatcher/api, it will automatically pick all the csv files present in data_dump folder and upload the data to db.sqlite3. Currently all the data is present in sqlite db
•	After running python manage.py runserver, application will start on 127.0.0.1:8000 and index page would be loaded with all the cryptocurrencies present in the DB with its data required in assignment.
•	It has search filter to filter within currencies
•	Search for currency required, and click on Details, it will hit details api and fetch all the details relevant to that currency and it will also fetch in every 2 minutes the current data of selected cryptocurrency in USD.


Running with Docker - simply run docker-compose up
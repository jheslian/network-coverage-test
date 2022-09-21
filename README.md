
# Mobile Network Coverage
A simple API to help users choose the best provider, to provide hints with the network coverage approximately available at their location.



## API Documentation:
An [external API](https://adresse.data.gouv.fr/api) has been used to retrieve other data from an address.
You can check the documention how to use the API and see some examples : [Network Coverage API](https://documenter.getpostman.com/view/19593881/2s7Ytafrav).


## Application environments:
 - python: version 3.8
 - django: 4.0
 - postgresql
 - *complete packages used are in requirements.txt*


## Getting started:
**Note:** Make sure you have python(atleast version 3.8) , virtual environment and git on your machine.

**Commands:**
  - `python -V` : command to check the version python if its installed
  - verify that you have the venv module : `python -m venv --help` if not please check https://www.python.org/downloads/. You could also use any other virtual environment to run the program(**if you opted to use other virtual environment the next commands are not suitable to run the program**)
  - `git --version` : to check your git version if its installed or you could download it at https://git-scm.com/downloads
  - `which psql` : checks postgreSQL - this be used as a database due to the queries which isn't compatible to the other database.

**How to run:**
 1. Clone the repository on the terminal or command prompt : `git clone https://github.com/jheslian/network-coverage-test.git`
 2. Create a virtual environment with "venv"  
	 - `cd network-coverage-test` :  to access the folder 
	 - python -m venv ***environment name*** : to create the virtual environment - exemple: `python -m venv env`
3. Activate the virtual environment:
	for unix or macos:
	- source ***environment name***/bin/activate - ex : `source env/bin/activate` if "env" is used as environment name 
	for windows:
	- ***environment name***\Scripts\activate.bat - ex: `env\Scripts\activate.bat`
4. Install the packages with pip: `pip install -r requirements.txt`	
5.  Migrate the tables/data to database:
 - Make sure you have created postregSQL database and configured database parameters in settings.py
	- for unix or macos: `python3 manage.py migrate`
	- for windows: `py manage.py migrate`
 - Upload data from csv file to database:
 	- for unix or macos: `python3 manage.py load_csv`
	- for windows: `py manage.py migrate load_csv`
6. Run the program :
	- for unix or macos: `python3 manage.py runserver`
	- for windows: `py manage.py runserver`
		

**External file**: mobile_operator.csv has been used to locate network provider and it's coverage which should be uploaded to the database.

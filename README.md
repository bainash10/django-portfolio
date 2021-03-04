# django-portfolio
Django basic app to list your jobs as portfolio website

1. Git: https://git-scm.com/downloads
2. TortoiseGit: https://tortoisegit.org/download/
3. SSH Setup using PuttyGen:

Open PuttyGen

    Click Generate button

    Save Private Key button Click --> Save on secure place i.e. Desktop

Use Public Key on text box in PuttyGen at the Github.com setting --> SSH and GPG Keys:
https://github.com/settings/keys


4.VS COde: Open that folder with COde:

in terminal: "CTRL+`"

To run python command: `python`
To check python verison :
	`python -v`


Create a virtual environment by running: 

Virtual environment packages all dependencies within a single project:
	
    `py -3 -m venv venv`

Activate the virtual environment by running:
    `source venv/Scripts/activate`
	
Install the necessary python packages by running:
	`pip install -r requirements.txt`
	
Above mentioned Virtual Environment creationg and requirements install is done only one time for the project! ONE TIME ONLY!

The following is done for every changes you make in you project:

Run the migrations by running:
	`python manage.py migrate`
and then running:
	`python manage.py makemigrations`
	`python manage.py migrate`	
	
To view it on web browser i.e. Chrome browser:

Start the web server by running on the terminal:
	`python manage.py runserver`
	
To see the website, go to chrome browser and type:
	http://localhost:8000

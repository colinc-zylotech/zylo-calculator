# Zylo Calculator  
[![CircleCI](https://circleci.com/gh/ColinCrawford/gitflow-sample-app.svg?style=svg)](https://circleci.com/gh/ColinCrawford/gitflow-sample-app)  
A demo application used when presenting git flow  

[dev-deployment](https://zylo-calculator-dev.herokuapp.com/)  
[release-deployment](https://zylo-calculator-release.herokuapp.com/)  
[prod-deployment](https://zylo-calculator.herokuapp.com/)  
  
The application uses  
[pipenv](https://pipenv.readthedocs.io/en/latest/) for dependency management  
[pytest](https://docs.pytest.org/en/latest/) for testing  
[pylint](https://www.pylint.org/) for linting  
[black](https://black.readthedocs.io/en/stable/) for formatting  
[flask](http://flask.pocoo.org/) for its web ui.  
[circleci](https://circleci.com/) for ci cd   
[heroku](https://heroku.com) for deployment  

There are also git hooks to help developers remember to run the tests pre-commit  

Docker and docker-compose are also set up for containerization of the app  

### To Install Dependencies  
##### (You Should Do This Before Anything Else)
`make install`  

### To Run Tests  
`make test`  

### To Start The App Locally In Dev Mode   
`make run-dev`  

### To Start The App Locally In Prod Mode  
`make run-prod`  

### To Start The App Locally In Dev Mode (With Docker)  
`make run-docker-dev`  

### To Start The App Locally In Prod Mode (With Docker)  
`make run-docker-prod`  

# Fake employees mock data parser API
A lightweight fake mock data API written in [_responder_](http://python-responder.org/en/latest/) python HTTP service framework. 
This application will parse fake (mock) employees JSON data and build an API to work with it.
Please follow [mock parser api](https://fake-employee-api.herokuapp.com) app to see how it looks like.

[![Build Status](https://travis-ci.org/vyahello/fake-employee-api.svg?branch=master)](https://travis-ci.org/vyahello/fake-employee-api)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/fake-employee-api/badge.svg?branch=master)](https://coveralls.io/github/vyahello/fake-employee-api?branch=master)

# Table of contents
- [Run application](#run-application)
- [Demo](#demo)
- [Run static code analysis](#run-static-code-analysis)
- [Heroku deployment](#heroku-deployment)
- [Contributing](#contributing)

# Run application
Run script from the root directory of the project:
```bash
python mock_parser_api.py
```

# Demo
![Screenshot](static/mock.png)

# Run static code analysis
In general static code analysis consists of following tools: `black`, `flake8`, `pylint`, `mypy`, and `unittests` accordingly.
To be able to start static code analysis _locally_ please run following script from the root directory of the project:
```bash
./run-code-analysis.sh install-dependencies
```

# Heroku deployment
Please follow instructions from - https://python-responder.org/en/latest/deployment.html

- Install heroku following by - https://devcenter.heroku.com/articles/heroku-cli#download-and-install
- Login to heroku
```bash
heroku login
```
- Create an application
```bash
heroku create fake-employee-api
```
- Commit and push repo into a heroku
```bash
git add . && git commit -m "My first heroku app" && git push heroku master
```
- Check heroku logs
```bash
heroku logs --tail
```
- Open an application via browser: https://fake-employee-api.herokuapp.com

# Contributing
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.7+` is required to run the code
- `pip install -r requirements` to install all project dependencies

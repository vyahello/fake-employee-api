[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with pylint](https://img.shields.io/badge/pylint-checked-blue)](https://www.pylint.org)
[![Checked with flake8](https://img.shields.io/badge/flake8-checked-blue)](http://flake8.pycqa.org/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Build Status](https://travis-ci.org/vyahello/fake-employee-api.svg?branch=master)](https://travis-ci.org/vyahello/fake-employee-api)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/fake-employee-api/badge.svg?branch=master)](https://coveralls.io/github/vyahello/fake-employee-api?branch=master)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)

# Fake employees API
> A lightweight fake mock data API written in [responder](http://python-responder.org/en/latest/) python HTTP service framework. 
> 
> This application will parse fake (mock) employees JSON data and build an API to work with it.
> Please follow [mock parser api](https://fake-employee-api.herokuapp.com) app to see how it looks like.

## Tools

### Production

- python 3.7, 3.8
- [responder](http://python-responder.org/en/latest/) framework
- [heroku](https://fake-employee-api.herokuapp.com) deployment

### Development
- [travis](https://travis-ci.org/) CI
- [pytest](https://pypi.org/project/pytest/) framework
- [black](https://black.readthedocs.io/en/stable/) code formatter
- [mypy](http://mypy.readthedocs.io/en/latest) static typer
- [pylint](https://www.pylint.org/) code style
- [flake8](http://flake8.pycqa.org/en/latest/) code formatter

## Usage

![Screenshot](static/mock.png)

### Quick start
Please run next commands to start an app:
```bash
git clone git@github.com:aiopymake/fake-employee-api.git
pip install -r requirements.txt
python mock_parser_api.py
```

## Development

### Testing

Please run the following script to tun unit tests:
```bash
pytest
```

### Code analysis
In general static code analysis consists of following tools: `black`, `flake8`, `pylint`, `mypy`, and `unittests` accordingly.

To be able to start static code analysis _locally_ please run following script from the root directory of the project:
```bash
./run-code-analysis.sh install-dependencies
```

### Deployment

Please refer to [deployment](DEPLOYMENT.md) page to get instructions on how to provision an app.

## Meta
Author – _Volodymyr Yahello_.

Distributed under the `MIT` license. See [license](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://twitter.com/vyahello](https://twitter.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
I would highly appreciate any contribution and support. If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
5. Create your feature branch (`git checkout -b feature/fooBar`)
6. Commit your changes (`git commit -am 'Add some fooBar'`)
7. Push to the branch (`git push origin feature/fooBar`)
8. Create a new Pull Request

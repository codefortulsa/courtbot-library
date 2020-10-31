# Court Scraping utilities

A python library for scraping case information from court systems.



## Development Install

1. Create and activate a Python 3.7.3 virtual env
1. `git clone git@github.com:codefortulsa/courtbot-library.git`
1. `cd courtbot-library`
1. `pip install -e .`

## Usage

Install with `pip install courtbot`


## Adding a court

- Add your state to courtbot/states/{two letter state abbreviation}
- Add properties to an __init__.py file in the diretory

### Require properties (so far):
- courts:  return a list of strings with the names of available courts
  e.g 
```
  [ ..., 'tulsa', 'wagoner', 'washington', 'washita', 'woods', 'woodward']
```

- get_case:  a function that accepts a case identifier and returns an object


## Case Object  

    The case object requires:
    events:  a list of dictionaries which contain a 'date' and 'description'
```
     {'date': 'Wednesday, May 27, 2020 at 9:00 AM',
      'description': 'DISTRICT COURT ARRAIGNMENT'}
```

## Run test scripts

- `pytest tests/`

or with ipdb:

    - `pytest -s tests/`

specify a test:

   - `pytest -s tests/test_parse.py -k 'test_events'`

## Deployment steps

1. `python3 setup.py sdist bdist_wheel`
1. `twine upload dist/*`
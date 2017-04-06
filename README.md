# Outdoor Catalog

This project is a web app built with Python, Flask, Google Sign-In, HTML, CSS,
and Bootstrap that provides a list of outdoor items (such as camping and hiking
gear) suggested by registered users.

## Built With

* [Bootstrap](http://getbootstrap.com/)
* [Flask](http://flask.pocoo.org/)
* [Python 2.7](https://www.python.org/)
* [SQLAlchemy](https://www.sqlalchemy.org/)

## Prerequisites

You will need the following things properly installed on your computer:

* [Git](http://git-scm.com/)
* [Python 2.7](https://www.python.org/)

## Installation

* run `git clone https://github.com/caseyr003/catalog.git`

## Running

To run the project locally follow the following steps:

* change into the project directory
* run `python database_setup.py`
* run `python populate.py`
* run `python project.py`
* visit `http://localhost:5000` in your browser

## JSON API

The JSON API allows retrieving data from the Outdoor Catalog database_setup

* `http://localhost:5000/category/JSON`
(returns a list of all categories available)
* `http://localhost:5000/category/<category_id>/list/JSON`
(returns a list of all items in the provided category id)
* `http://localhost:5000/category/<category_id>/list/<item_id>/JSON`
(returns a item for the provided item id and category id)

## License

This project is licensed under the MIT License

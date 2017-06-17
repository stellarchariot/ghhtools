# Game of Hip Hop (GHH) Tools

Tools and utilities that help make it easier to manage the Game of Hip Hop (GHH) competition (at [r/makinghiphop](https://www.reddit.com/r/makinghiphop/)).

## Getting Started

On a Unix-like machine (e.g. a Mac or a Linux box):

```
$ git clone https://github.com/stellarchariot/ghhtools.git
$ cd ghhtools
$ virtualenv venv --python=python2.7
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Set the Reddit API client ID and client secret in the enviornment variables:

- `REDDIT_API_CLIENT_ID`
- `REDDIT_API_CLIENT_SECRET`

You can generate the client ID and client secret by creating a Reddit app via: https://www.reddit.com/prefs/apps/

Run the app locally:

```
python ghhtools/app.py
```

And visit the URL shown (the default is http://localhost:8080/) using a web browser.

### Prerequisites

You'll need to have the following installed and have a basic understanding of:

- Git
- Python
- PIP
- Flask
- Virtualenv (optional, but highly recommended)

## Running the tests

```
$ cd ghhtools
$ python -m unittest discover test/
```

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [PIP](https://pypi.python.org/pypi/pip) - Dependency/package management
* [PRAW](https://praw.readthedocs.io/en/latest/) - The Python Reddit API Wrapper

## Authors

* **Arun Neelakandan** - *Initial work* - [Stellar Chariot](https://stellarchariot.com)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

# tsm-oauth-py
This repository contains a starting point for a simple app, intended for learning about OAuth2 with python.

## Getting started
To run the code in this repository, you need [Python](https://www.python.org/downloads/).

You also need [flask](https://pypi.org/project/Flask/) and [requests](https://pypi.org/project/requests/).
Install those libraries with `pip install --user flask requests`.
If everything is set up, you can run the app with `flask run --port 5000` and then access it at `http://localhost:5000`.

You are encouraged to use a virtual environment, for example with `pipenv`, but you don't have to.

## Dependencies
Here, we use flask as a web framework and requests to make get and post requests.
flask uses Jinja as a template engine.
Templates are stored in the `templates` folder and have an `html` extension.
You can find quickstart guides here
- [flask quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
- [jinja quickstart](https://jinja.palletsprojects.com/en/2.11.x/)
- [requests quickstart](https://docs.python-requests.org/en/master/user/quickstart/)

We also use the [milligram css framework](https://milligram.io/) for styling.

If you are more comfortable with other libraries, you are free to use them.
flask and requests serve only as suggestions because they are popular and it's easy to find examples and help online.

## Workflow idea
1. The user visits the index page under `/`
    - if the user is not logged in, we display a login button
    - if the user is logged in, we receive an access token, display a greeting with the user's name, and show a logout button
2. Clicking on the login button sends the user to the `/auth` route, which then sends the user on to an authorisation URL
3. After the user has authorised the external app to provide us with their information, they are redirected to the `/auth/callback` route where we receive a temporary code that we use to get an access token for the user's information
4. We redirect the user back to the index page together with the access token

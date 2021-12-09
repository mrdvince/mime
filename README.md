<p align="center">
<img src="images/mime.jpg"/>
</p>

> Photo by <a href="https://unsplash.com/@fatihkilic?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Fatih Kılıç</a> on <a href="https://unsplash.com/s/photos/mime?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>


# mime

> Here be mimes!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/) [![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# What is this?

This is me goofing around and trying to learn some Django the only way there is, (by attempting to build something and combining it with a bunch of other things i know or have come across).

> I also don't have a job so need to do something with my life. 😏😏

## Settings

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out

- To create an **superuser account**, use this command:

      $ python manage.py createsuperuser

### Type checks

Running type checks with mypy:

    $ mypy mime

### Test coverage

To run the tests, check your test coverage, and generate an HTML
coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with py.test

    $ pytest

### Docker

See detailed [cookiecutter-django Docker
documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html)

# Chapter 3: Models

* Most of the chapter refers to three apps:
	- `src/profiles`
	- `src/sightings`
	- `src/posts`
* Refer to service objects at `src/profiles/services.py`
* Refer to signals for profile creation at `src/profiles/signals.py`
* Remember to apply migrations!

# SuperBook

SuperBook is a social network for superheroes built with [Python][0] using the [Django Web Framework][1].

This project has the following basic apps:

* App1 (short desc)
* App2 (short desc)
* App3 (short desc)

## Installation

### Quick start

To set up a development environment quickly, first install Python 3.4. It
comes with virtualenv built-in. So create a virtual env by:

    $ python3.4 -m venv superbook
    $ . superbook/bin/activate

> Sometimes, binaries like pip get installed inside `local/bin/`. So append
> this line to `superbook/bin/activate`:
>
> `PATH="$VIRTUAL_ENV/local/bin:$PATH"`

Now the pip commands should work smoothly. Install all dependencies:

    pip install -r dev-requirements.txt

Run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the docs for a detailed instructions guide.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/

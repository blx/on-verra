# on-verra

Absurdly simple Flask microapp to report current CPU and RAM usage of your server, as well as uptime.

![Screenshot](/../gh-pages/screenshots/screenshot.png?raw=true)

## Installation

    $ git clone https://github.com/blx/on-verra.git
    $ cd on-verra
    $ virtualenv env-verra
    $ . env-verra/bin/activate
    (env-verra)$ pip install -r requirements.txt


## Usage

**Simple**

Activate the relevant `virtualenv` and run `python q.py`.

Defaults to listening at `localhost:5000`, which can be changed by passing `port` and/or `host` keyword params to `app.run()`.

**uWSGI (Emperor multi-app mode)**

1. Add an appropriate config file to your uWSGI [`Emperor`](https://uwsgi-docs.readthedocs.org/en/latest/Emperor.html) config directory. A skeleton config would be (in the INI syntax):

        [uwsgi]
        chdir = /path/to/on-verra
        home = /path/to/on-verra-virtualenv-if-applicable
        module = q:app
        
        socket = :8002

    Your `socket` may be different depending on how you expose uWSGI to the world. I mostly just pulled this from my config.

2. Connect to nginx or whatever else you're running in front of uWSGI. An example nginx config block would be:

        location /on-verra/ {
            include uwsgi_params;
            uwsgi_pass 127.0.0.1:8002;
        }


## Licence

*The Fair License:*

Copyright 2015 Ben Cook.

Usage of the works is permitted provided that this instrument is retained with the works, so that any entity that uses the works is notified of this instrument.

DISCLAIMER: THE WORKS ARE WITHOUT WARRANTY.

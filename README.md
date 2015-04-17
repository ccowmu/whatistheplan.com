whatistheplan.com [![Build Status](https://travis-ci.org/ccowmu/whatistheplan.com.svg?branch=master)](https://travis-ci.org/ccowmu/whatistheplan.com)
=================

This is to become the newest rendition of the website we use for our semi-annual Parkview Lan. As opposed to previous renditions, this will have active features such as chatrooms (irc backed), user registration, and various administrative capabilities. It will be built using the popular django python web framework in an open-source and collaborative work environment.

Features
--------

- User Registration
  - PayPal Payment?
- IRC-backed chatrooms
  - KiwiIRC frontend

Development
-----------

Primary development discussion will take place on the computer club IRC network in the #plansite channel. Anybody interested in helping with development should make themselves familiar with django and python. All skill levels are welcome, however you must have a willingness to learn. A simple django introduction can be found at http://www.tangowithdjango.com/book17/index.html

### Getting started:

- Make sure you have python virtualenv installed. If you are on ubuntu, installing is as simple as `sudo apt-get install python-virtualenv`
- Make sure you have python 2 installed. Ubuntu comes with python2 as the default python
- Run the following commands

```shell
git clone git@github.com:ccowmu/whatistheplan.com.git # download the sources
cd whatistheplan                                      # change into the directory
make setup                                            # set up the project
make run                                              # start the development server
```

### Make File

- run **default target**
  - Run the django server
- setup
  - Set up the environment
  - Runs virtualenv, requirements, db
- clean
  - Deletes all files created during setup and runtime
- virtualenv
  - Sets up a local virtualenv with python2
- requirements
  - Installs requirements (in requirements.txt) into virtualenv
- db
  - Run db migrations
- test
  - Runs tests in tests/ directory
  - respects `VERBOSITY` environment variable values {0-3} (default 1)
- lint
  - Check PEP8 coding standards



### Design Decisions

- Using Python Django web framework
- Using Postgresql database backend
- Social integration
  - Twitch
  - Twitter
  - Chat rooms
    - Will be backed by IRC with a KiwiIRC frontend
- User data stored in the database
  - Payments and sign-ins
- Simple database-backed news feed
- Event schedule page with notification system
- URL Structure
  - Discussion welcomed at [#14](https://github.com/ccowmu/whatistheplan.com/issues/14)

LICENSE
-------

This work is being developed under the MIT software license.

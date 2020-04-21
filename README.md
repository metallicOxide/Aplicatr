# Aplicatr

Aplicatr is a web application helping students get on top of their job application deadlines.

## How it works

Aplicatr generates an ICS calendar file with tailored job listings and preferences from their university job portal.

1. Students provide their university login credentials which is used to generate a cookie session to scrape job listings on their relevant university job portal.
2. Students can filter job listings based on search terms and preferences, and choose preferred a date deadline to be reminded of the job listing.
3. Students then generate an ICS file based on their job listing preferences, which can then be placed in their personal calendars.

> NOTE: We do NOT store any student's password

Currently supports the following universities:

* UNSW

## Project Development Environment Setup

Ensure website and server running in different terminals

### Setting up website client

> Install website dependencies

```bash
npm run website-install
```

> Start website

```bash
npm run website-start
```

### Setting up database

> Ensure postgresql installed

> Configure database permissions

```bash
sudo su - postgres
```

> Create database

```bash
psql < ./server/dbsetup.sql
```

### Setting up server

> Open up another terminal
> Ensure pipenv installed

```bash
pip3 install pipenv
```

> Install python server virtual environment dependencies

```bash
pipenv install
```

> Start server in virtual shell environment

```bash
pipenv run python3 -m server
```

### WSL Configurations

```bash
pipenv install --python={{Path_To_Python}}
{{Path_To_Python}} = which Python
pipenv run python3 -m server
```

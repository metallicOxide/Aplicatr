# Job Scraper Project

## Project Development Environment Setup

Ensure website and server running in different terminals

### Setting up website client

1) Install website dependencies

```bash
npm run website-install
```

2) Start website

```bash
npm run website-start
```

### Setting up database

1) Ensure postgresql installed

2) Configure database permissions

```bash
sudo su - postgres
```

3) Create database

```bash
psql < ./server/dbsetup.sql
```

### Setting up server

1) Open up another terminal

2) Ensure pipenv installed

```bash
pip3 install pipenv
```

3) Install python server virtual environment dependencies

```bash
pipenv install
```

4) Start server in virtual shell environment

```bash
pipenv run python3 -m server
```


### If using WSL

```bash
pipenv install --python={{Path_To_Python}}
{{Path_To_Python}} = which Python
pipenv run python3 -m server
```
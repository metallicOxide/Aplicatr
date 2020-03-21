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

### Setting up server

1) Open up another terminal

2) Ensure pipenv installed

```bash
(cd server && pip3 install pipenv)
```

3) Install python server virtual environment dependencies

```bash
(cd server && pipenv install)
```

4) Start server in virtual shell environment

```bash
(cd server && pipenv run python3 app.py)
```

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

2) Install virtualenv

```bash
pip install virtualenv
```

3) Activate python virtual environment

```bash
source server/env/bin/activate
```

4) Install server dependencies

```bash
(cd server && pip install -r requirements.txt)
```

5) Start server

```bash
(cd server && python app.py)
```

6) Deactivate python virtual environment when finished development

```bash
deactivate
```

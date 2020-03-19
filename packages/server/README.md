# job-scrapper server

Open up a new terminal first

## Always enable python virtual environment

```bash
pip install virtualenv
```

```bash
source env/bin/activate
```

## Create python envrionment

```bash
pip install -r requirements.txt
```

## Server setup

```bash
./app.py
```

## Keeping environment consistent with new installed packages during development

```bash
pip freeze > requirements.txt
```

## Deactivate python virtual environment

```bash
deactivate
```
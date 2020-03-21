# job-scrapper server

Open up a new terminal first

## Always enable python virtual environment

```bash
pip3 install virtualenv
```

```bash
source env/bin/activate
```

## Create python envrionment

```bash
pip3 install -r requirements.txt
```

## Server setup

```bash
python app.py
```

## Keeping environment consistent with new installed packages during development

```bash
pip3 freeze > requirements.txt
```

## Deactivate python virtual environment

```bash
deactivate
```
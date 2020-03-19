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

2) Activate python virtual environment

```bash
source packages/server/env/bin/activate
```

3) Install server dependencies

```bash
(cd packages/server && pip install -r requirements.txt)
```

4) Start server

```bash
(cd packages/server && python app.py)
```

5) Deactivate python virtual environment when finished development

```bash
deactivate
```

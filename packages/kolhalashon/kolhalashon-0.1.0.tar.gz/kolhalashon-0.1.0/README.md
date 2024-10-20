# Kol Halashon API

Python wrapper for Kol Halashon website API.

## Installation
```bash
pip install kolhalashon
```

## Usage
```python
from kolhalashon import KolHalashonAPI

api = KolHalashonAPI(use_session=True)
api.login("username", "password")
```

## Features
- Search shiurim
- Download audio/video content
- Browse by Rabbi
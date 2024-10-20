# Kol Halashon API

Python wrapper for Kol Halashon website API.

## Installation
```bash
pip install kolhalashon
```

## Usage
```python
from kolhalashon import KolHalashonAPI
from dotenv import load_dotenv
load_dotenv()


api = KolHalashonAPI(
    use_session=True,
    session_file='session.pkl'
)
category = api.search_items("אברהם")

if not (category.rabanim or category.books or category.shiurim or category.others):
    print("No items found.")
    exit()

print("Rabanim:")
for rabbi in category.rabanim:
    print(rabbi)

print("\nBooks:")
for book in category.books:
    print(book)

print("\nShiurim:")
for shiur in category.shiurim:
    print(shiur)

print("\nOthers:")
for other in category.others:
    print(other)

```

## Features
- Search shiurim
- Download audio/video content
- Browse by Rabbi
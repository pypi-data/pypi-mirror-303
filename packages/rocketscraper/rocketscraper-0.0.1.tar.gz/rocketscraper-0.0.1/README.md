# Rocket Scraper API Python SDK

Python SDK for the [Rocket Scraper API](https://rocketscraper.com). For more information, visit the [GitHub repository](https://github.com/rocketscraper/rocketscraper-sdk-python).

## Requirements

- [Python](https://www.python.org/) version 3.7 or above

## Installation

```bash
pip install rocketscraper
```

## Usage

To use the SDK, you need to create a new instance of the `RocketClient` class and pass your API key as an argument.

### Setup

```python
from rocketscraper import RocketClient

rocket_client = RocketClient(api_key='YOUR_API_KEY')
```

### Scrape

The `scrape` method allows you to scrape data from a website using a schema. The method returns the scraped data in the format specified in the schema.

```python
data = rocket_client.scrape(
    url='https://ycombinator.com/companies/pagerduty',
    schema={
        'company': 'string',
        'image_url': 'string',
        'founded_at': 'string',
        'size': 'integer',
        'location': 'string',
        'short_description': 'string',
        'long_description': 'string',
        'is_active': 'boolean',
        'founders': [
            {
                'name': 'string',
                'role': 'string',
            },
        ],
    }
)

print(data)
```

For more details, visit the [Python SDK GitHub repository](https://github.com/rocketscraper/rocketscraper-sdk-python).

## Documentation

For more information on how to use the Rocket Scraper API, visit the [Rocket Scraper API documentation](https://docs.rocketscraper.com).

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/rocketscraper/rocketscraper-sdk-python/blob/main/LICENSE) file for more details.

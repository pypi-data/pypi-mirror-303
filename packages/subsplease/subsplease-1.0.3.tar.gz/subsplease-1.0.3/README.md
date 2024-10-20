## SubsPlease API Client This package provides a simple interface to fetch and parse episodes from the [SubsPlease API](https://subsplease.org/).

### Installation You can install the package using pip:

```
pip install subsplease
```

## Usage

Here’s how you can use the package:

```
from subsplease import SubsPlease
search_query = "kami"
subs_please = SubsPlease()
episodes = subs_please.search(search_query)
for episode in episodes:
	print(episode)
```

## Features

- Search for episodes based on show names.
- Retrieve download links for various quality formats (480p, 720p, 1080p).
- Easy integration with your Python applications.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to submit a pull request or create an issue in the repository.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

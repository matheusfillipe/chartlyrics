# ChartLyrics API

This is a simple wrapper for: http://api.chartlyrics.com. You can search for songs, artists and get the lyrics.

## Installation

``` sh
pip install chartlyrics
```

## Usage Example

```python
from chartlyrics import ChartLyricsClient

client = ChartLyricsClient()

for song in client.search_text("starts with one"):
    if "park" in song.artist.lower():
      print(song.artist)  # Linking Park
      print(song.lyrics)  # Starts with one\n One thing I dont know why...
    
```

Check the `tests` for more examples.

## Development

Fork the repo, run:

``` sh
poetry install
```

Add features, write tests, run:

``` sh
poetry run pytest
```

Create a Pull request.

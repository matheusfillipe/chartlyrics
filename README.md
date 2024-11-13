[![CircleCI Build Status](https://circleci.com/gh/matheusfillipe/chartlyrics.svg?style=shield)](https://circleci.com/gh/matheusfillipe/chartlyrics)
[![Pypi](https://badge.fury.io/py/chartlyrics.svg)](https://pypi.org/project/chartlyrics/)
[![Chat with me on irc](https://img.shields.io/badge/-IRC-gray?logo=gitter)](https://connect.h4ks.com/)

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

You can also use `song.lyrics_object` which will return a `Lyrics` object that you can index strophes and verses on:

```python
lyrics = song.lyrics_object
print(lyrics[0][-1])  # first strophe last verse
```

Check the `tests` for more examples.

## Development

Fork the repo, run:

```sh
poetry install
```

Add features, write tests, run:

```sh
poetry run pytest
```

Create a Pull request.

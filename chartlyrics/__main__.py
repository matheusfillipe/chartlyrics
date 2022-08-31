from .client import ChartLyricsClient

import click


@click.command()
@click.argument("search_query")
@click.option('-a', "--artist", default=None, help="Artist name")
@click.option('-l', "--lyrics", default=None, help="Show lyrics to the nth result")
def main(search_query, artist, lyrics):
    client = ChartLyricsClient()
    if lyrics is None:
        if artist is None:
            for song in client.search_text(search_query):
                print(str(song))
            return
        for song in client.search_artist_and_song(artist, search_query):
            print(str(song))
        return
    i = 0
    for song in client.search_text(search_query):
        if i == int(lyrics):
            print(str(song.lyrics))
            return
        i += 1

if __name__ == '__main__':
    main()

from .client import ChartLyricsClient

import click


@click.command()
@click.argument("search_query")
@click.option('-a', "--artist", default=None, help="Artist name")
def main(search_query, artist):
    client = ChartLyricsClient()
    if artist is None:
        for song in client.search_text(search_query):
            print(str(song))
        return
    for song in client.search_artist_and_song(search_query, artist):
        print(str(song))

if __name__ == '__main__':
    main()

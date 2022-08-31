from chartlyrics import ChartLyricsClient
from chartlyrics.lyrics import Lyrics

client = ChartLyricsClient()

def test_lyrics_parsing():
    sample = """
    One thing I don't know why
    It doesn't even matter how hard you try
    Keep that in mind, I designed this rhyme
    To explain in due time

    All I know
    Time is a valuable thing
    Watch it fly by as the pendulum swings
    Watch it count down to the end of the day
    The clock ticks life away

    It's so unreal
    Didn't look out below
    Watch the time go right out the window
    Tryin' to hold on, did-didn't even know
    I wasted it all just to watch you go
    """

    lyrics = Lyrics(sample)
    assert lyrics[0][0] == "One thing I don't know why"
    assert lyrics[1][2] == "Watch it fly by as the pendulum swings"
    assert lyrics[-1][-1] == "I wasted it all just to watch you go"


def test_search_text():
    lyrics = ""
    for song in client.search_text("starts with one"):
        if "park" in song.artist.lower():
            lyrics = song.lyrics_object
            break
    assert "starts with one" in str(lyrics)
    assert lyrics[0][-1] == "A memory of a time when"

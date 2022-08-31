from dataclasses import dataclass, asdict, fields
from typing import Generator

import requests
from lxml import etree as ElementTree
from .lyrics import Lyrics

API = "http://api.chartlyrics.com/apiv1.asmx/{}"
NAMESPACE = "{http://api.chartlyrics.com/}"


def root_element(content: str):
    parser = ElementTree.XMLParser(recover=True)
    return ElementTree.fromstring(content, parser)


def capitalize(word: str):
    """
    Capitalizes first character

    :param word str: word to capitalize
    """
    return word[0].upper() + word[1:]


@dataclass
class Endpoints:
    search_text = API.format("SearchLyricText")
    get_lyric = API.format("GetLyric")
    search_artist_and_song = API.format("SearchLyric")


@dataclass
class XmlDataclass:
    @classmethod
    def from_xml(cls, content: str):
        root = root_element(content)
        as_dict = {}
        for field in fields(cls):
            node = root.find(f"{NAMESPACE}{capitalize(field.name)}")
            text = node.text
            as_dict[field.name] = field.type(text)
        return cls(**as_dict)

    def to_dict(self):
        return asdict(self)


@dataclass
class GetLyricResult(XmlDataclass):
    trackId: int
    lyricChecksum: str
    lyricId: int
    lyricSong: str
    lyricArtist: str
    lyricUrl: str
    lyricCovertArtUrl: str
    lyricRank: int
    lyricCorrectUrl: str
    lyric: str


@dataclass
class SearchLyricResult:
    trackId: int
    lyricChecksum: str
    lyricId: int
    songUrl: str
    artistUrl: str
    artist: str
    song: str
    songRank: int
    client: "ChartLyricsClient"

    @classmethod
    def from_element(cls, element: ElementTree.Element, client=None) -> "SearchLyricResult":
        """
        Create class from content xml

        :param content str:
        :rtype SearchLyricResult:
        """
        try:
            return SearchLyricResult(
                trackId=int(element.find(f"{NAMESPACE}TrackId").text),
                lyricChecksum=element.find(f"{NAMESPACE}LyricChecksum").text,
                lyricId=int(element.find(f"{NAMESPACE}LyricId").text),
                songUrl=element.find(f"{NAMESPACE}SongUrl").text,
                artistUrl=element.find(f"{NAMESPACE}ArtistUrl").text,
                artist=element.find(f"{NAMESPACE}Artist").text,
                song=element.find(f"{NAMESPACE}Song").text,
                songRank=int(element.find(f"{NAMESPACE}SongRank").text),
                client=client,
            )
        except AttributeError:
            return None

    @property
    def lyrics(self) -> str:
        if self.client is None:
            raise Exception("Client is not set")
        return self.client.get_lyric(self.lyricId, self.lyricChecksum).lyric

    @property
    def lyrics_object(self) -> Lyrics:
        return Lyrics(self.lyrics)


class ArrayOfSearchLyricResult:
    def __init__(self, content: str, client=None):
        """
        Result from Endpoints.search_text

        :param content str: xml content
        """
        root = root_element(content)
        self.results = []
        for result in root.findall(f"{NAMESPACE}SearchLyricResult"):
            searchLyricResult = SearchLyricResult.from_element(result, client)
            if searchLyricResult is not None:
                self.results.append(searchLyricResult)

    def __iter__(self) -> Generator[SearchLyricResult, None, None]:
        for result in self.results:
            yield result

    def __repr__(self):
        return str(self.results)


class ChartLyricsClient:
    def __init__(self):
        self.session = requests.Session()
        headers = {
            "Content-Type": "text/xml; charset=utf-8",
        }
        self.session.headers.update(headers)

    def search_text(self, text: str) -> ArrayOfSearchLyricResult:
        params = {
            "lyricText": text,
        }
        response = requests.get(Endpoints.search_text,
                                params=params
                                )
        return ArrayOfSearchLyricResult(response.content, self)

    def get_lyric(self, lyricId, lyricChecksum) -> GetLyricResult:
        params = {
            "lyricId": lyricId,
            "lyricChecksum": lyricChecksum,
        }
        response = requests.get(Endpoints.get_lyric,
                                params=params
                                )
        return GetLyricResult.from_xml(response.content)

    def search_artist_and_song(self, artist: str, song: str) -> ArrayOfSearchLyricResult:
        params = {
            "artist": artist,
            "song": song,
        }
        response = requests.get(Endpoints.search_artist_and_song,
                                params=params
                                )
        return ArrayOfSearchLyricResult(response.content, self)

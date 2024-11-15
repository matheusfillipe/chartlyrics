# Lyrics base classes


from typing import Generator


class LyricsElement:
    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return self.text

    def __repr__(self) -> str:
        return f"{str(type(self))} : '{str(self)}'"

    def __eq__(self, x) -> bool:
        if isinstance(x, str):
            return str(self) == x
        return self == x


class Verse(LyricsElement):
    def __init__(self, verse: str):
        super().__init__(verse.strip())


class Strophe(LyricsElement):
    def __init__(self, strophe: str):
        super().__init__(strophe)
        self.verses = [Verse(t) for t in strophe.strip().split("\n")]

    def __getitem__(self, index) -> Verse:
        return self.verses[index]

    def __iter__(self) -> Generator[Verse, None, None]:
        for verse in self.verses:
            yield verse


class Lyrics(LyricsElement):
    def __init__(self, text: str):
        super().__init__(text)
        self.strophes = [Strophe(t) for t in text.strip().split("\n\n")]

    def __getitem__(self, index) -> Strophe:
        return self.strophes[index]

    def __iter__(self) -> Generator[Strophe, None, None]:
        for strophe in self.strophes:
            yield strophe

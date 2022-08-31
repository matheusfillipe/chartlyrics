# Lyrics base classes

class LyricsElement:
    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return self.text

    def __repr__(self):
        return f"{str(type(self))} : '{str(self)}'"

    def __eq__(self, x):
        if isinstance(x, str):
            return str(self) == x
        return self == x


class Verse(LyricsElement):
    def __init__(self, verse: str):
        super().__init__(verse.strip())


class Strophe(LyricsElement):
    def __init__(self, strophe: str):
        super().__init__(strophe)
        self.verses = [Verse(t) for t in strophe.strip().split('\n')]

    def __getitem__(self, index):
        return self.verses[index]

    def __iter__(self):
        for verse in self.verses:
            yield verse

class Lyrics(LyricsElement):
    def __init__(self, text: str):
        super().__init__(text)
        self.strophes = [Strophe(t) for t in text.strip().split('\n\n')]

    def __getitem__(self, index):
        return self.strophes[index]

    def __iter__(self):
        for strophe in self.strophes:
            yield strophe

# Lyrics base classes

class LyricsElement:
    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return self.verse


class Verse(LyricsElement):
    def __init__(self, verse: str):
        super().__init__(verse)


class Strophe(LyricsElement):
    def __init__(self, strophe: str):
        super().__init__(strophe)
        self.verses = strophe.strip().split('\n')

    def __getitem__(self, index):
        return self.verses[index]


class Lyrics(LyricsElement):
    def __init__(self, text: str):
        super().__init__(text)
        self.strophes = text.strip().split('\n\n')

    def __getitem__(self, index):
        return self.strophes[index]

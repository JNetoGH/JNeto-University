class StringBuilder:

    _text: str = ""

    def append(self, string: str):
        self._text += string

    def append_line(self, string: str):
        self._text += string + "\n"

    def add_line(self):
        self._text += "\n"

    def to_string(self) -> str:
        return self._text

class Note:
    """
    A class that contains information about a note (name, octave, pitch) in American notation.
    """

    __OCTAVE_MIN = 0
    __OCTAVE_MAX = 8

    __STANDART_POS = 9
    __STANDART_OCTAVE = 4
    __STANDART_PITCH = 440

    __NAMES = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")

    def __init__(self, name: str, octave: int) -> None:
        self.__set_name(name)
        self.__set_octave(octave)
        self.__set_pitch()

    def __set_name(self, name: str) -> None:
        name = name.capitalize()
        if name in Note.__NAMES:
            self.__name = name
        else:
            raise ValueError(
                f"The specified note name '{name}' is outside the range: {Note.__NAMES}."
            )

    def __set_octave(self, octave: int) -> None:
        if Note.__OCTAVE_MIN <= octave <= Note.__OCTAVE_MAX:
            self.__octave = octave
        else:
            raise ValueError(
                f"The specified octave number '{octave}' is outside the range: {Note.__OCTAVE_MIN} – {Note.__OCTAVE_MAX}."
            )

    def __set_pitch(self) -> None:
        i = (
            (self.__octave - Note.__STANDART_OCTAVE) * len(Note.__NAMES)
            + Note.__NAMES.index(self.__name)
            - Note.__STANDART_POS
        )
        self.__pitch = Note.__STANDART_PITCH * 2 ** (i / len(Note.__NAMES))

    @property
    def name(self) -> str:
        return self.__name

    @property
    def octave(self) -> int:
        return self.__octave

    @property
    def pitch(self) -> float:
        return self.__pitch

    def __str__(self):
        return f"{self.__name}{self.__octave} {self.__pitch:.2f} (Hz)"

    def __repr__(self):
        return f"Note({self.__name}, {self.__octave}, {self.__pitch})"


if __name__ == "__main__":
    pass

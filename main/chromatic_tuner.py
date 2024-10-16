from math import log2, trunc
from note import Note


class ChromaticTuner:
    """
    ...
    """

    def __init__(self) -> None:
        self.octave_min, self.octave_max = Note.octaves()
        self.names = Note.names()
        self.standart = Note.standart()
        self.semitones_down = (
            -len(self.names) * self.standart.octave - self.standart.position
        )
        self.semitones_up = (
            len(self.names) * (self.octave_max - self.octave_min + 1)
            + self.semitones_down
            - 1
        )

    def detect_note(self, pitch: float) -> Note:
        i = round(len(self.names) * log2(pitch / self.standart.pitch))
        i = min(self.semitones_up, max(self.semitones_down, i))
        return Note(
            self.names[(i + self.standart.position) % len(self.names)],
            self.standart.octave + trunc(i / len(self.names)),
        )


if __name__ == "__main__":
    pass

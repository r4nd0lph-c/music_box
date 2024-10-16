from note import Note

S = 14
N = 2


def main() -> None:
    """
    A function that displays the calculated note pitch values.
    """

    names = Note.names()
    octave_min, octave_max = Note.octaves()
    O = len(str(octave_max))

    print("  | ", end="")
    for i in range(octave_min, octave_max + 1):
        print(str(i).zfill(O).ljust(S), end="|")

    for k, n in enumerate(names):
        print()
        print(str(k).zfill(2), end="| ")
        for i in range(octave_min, octave_max + 1):
            note = Note(n, i)
            print(
                f"{note.name}{note.octave}".ljust(N + O + 1)
                + f"{note.pitch:.3f}".ljust(S - N - O - 1),
                end="|",
            )


if __name__ == "__main__":
    main()

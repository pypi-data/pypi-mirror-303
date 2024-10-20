import uuid
import pathlib
import typing

_UUID_NAMESPACE = uuid.uuid1()

def read_notes(notes_filename: pathlib.Path) -> typing.Iterable[str]:
    with open(notes_filename) as notes_file:
        note = ''
        for line in notes_file:
            stripped_line = line.strip()
            if stripped_line != '':
                note += stripped_line + '\n'
                continue

            stripped_note = note.strip()
            if stripped_note != '':
                yield stripped_note
                note = ''

        stripped_note = note.strip()
        if stripped_note != '':
            yield stripped_note

def generate_note_id(note: str) -> str:
    return str(uuid.uuid5(_UUID_NAMESPACE, note))

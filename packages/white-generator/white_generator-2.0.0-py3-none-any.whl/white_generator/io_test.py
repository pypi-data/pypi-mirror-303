import unittest
import tempfile
import pathlib

import termcolor

from . import logger
from . import io

class TestReadNotes(unittest.TestCase):
  _tmpDir: tempfile.TemporaryDirectory[str]

  @classmethod
  def setUpClass(self) -> None:
    logger.init_logger()

    self._tmpDir = tempfile.TemporaryDirectory(prefix='white-generator-')
    logger.get_logger().info(
      'create the temporary directory %s',
      termcolor.colored(self._tmpDir.name, 'yellow'),
    )

  @classmethod
  def tearDownClass(self) -> None:
    self._tmpDir.cleanup()

  def test_single_note_with_single_line(self) -> None:
    self._write_notes_content('note #1')

    notes = list(io.read_notes(self._get_notes_filename()))
    self.assertEqual(notes, ['note #1'])

  def test_single_note_with_multiple_lines(self) -> None:
    self._write_notes_content('note #1; line #1\nnote #1; line #2')

    notes = list(io.read_notes(self._get_notes_filename()))
    self.assertEqual(notes, ['note #1; line #1\nnote #1; line #2'])

  def test_multiple_notes_with_single_line(self) -> None:
    self._write_notes_content('note #1\n\nnote #2')

    notes = list(io.read_notes(self._get_notes_filename()))
    self.assertEqual(notes, ['note #1', 'note #2'])

  def test_multiple_notes_with_multiple_lines(self) -> None:
    self._write_notes_content(
      'note #1; line #1\nnote #1; line #2\n'
        + '\n'
        + 'note #2; line #1\nnote #2; line #2',
    )

    notes = list(io.read_notes(self._get_notes_filename()))
    self.assertEqual(notes, [
      'note #1; line #1\nnote #1; line #2',
      'note #2; line #1\nnote #2; line #2',
    ])

  def test_trailing_line_break(self) -> None:
    self._write_notes_content(
      'note #1; line #1\nnote #1; line #2\n'
        + '\n'
        + 'note #2; line #1\nnote #2; line #2\n',
    )

    notes = list(io.read_notes(self._get_notes_filename()))
    self.assertEqual(notes, [
      'note #1; line #1\nnote #1; line #2',
      'note #2; line #1\nnote #2; line #2',
    ])

  def test_extra_spaces_in_separator_line(self) -> None:
    self._write_notes_content(
      'note #1; line #1\nnote #1; line #2\n'
        + '  \n'
        + 'note #2; line #1\nnote #2; line #2',
    )

    notes = list(io.read_notes(self._get_notes_filename()))
    self.assertEqual(notes, [
      'note #1; line #1\nnote #1; line #2',
      'note #2; line #1\nnote #2; line #2',
    ])

  def test_extra_separator_lines(self) -> None:
    self._write_notes_content(
      'note #1; line #1\nnote #1; line #2\n'
        + '\n'
        + '\n'
        + '\n'
        + 'note #2; line #1\nnote #2; line #2',
    )

    notes = list(io.read_notes(self._get_notes_filename()))
    self.assertEqual(notes, [
      'note #1; line #1\nnote #1; line #2',
      'note #2; line #1\nnote #2; line #2',
    ])

  def test_extra_spaces_on_note_boundaries(self) -> None:
    self._write_notes_content(
      '  note #1; line #1\nnote #1; line #2  \n'
        + '\n'
        + '  note #2; line #1\nnote #2; line #2  ',
    )

    notes = list(io.read_notes(self._get_notes_filename()))
    self.assertEqual(notes, [
      'note #1; line #1\nnote #1; line #2',
      'note #2; line #1\nnote #2; line #2',
    ])

  def test_extra_spaces_on_line_boundaries(self) -> None:
    self._write_notes_content(
      '  note #1; line #1  \n  note #1; line #2  \n'
        + '\n'
        + '  note #2; line #1  \n  note #2; line #2  ',
    )

    notes = list(io.read_notes(self._get_notes_filename()))
    self.assertEqual(notes, [
      'note #1; line #1\nnote #1; line #2',
      'note #2; line #1\nnote #2; line #2',
    ])

  def _get_notes_filename(self) -> pathlib.Path:
    return pathlib.Path(self._tmpDir.name) / 'notes.txt'

  def _write_notes_content(self, notes_content: str) -> None:
    with open(self._get_notes_filename(), mode='w') as notes_file:
      notes_file.write(notes_content)

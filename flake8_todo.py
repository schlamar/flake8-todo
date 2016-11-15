
__version__ = '0.7'

import re

import pycodestyle

NOTE_REGEX = re.compile(r'(TODO|FIXME|XXX)')  # noqa


def check_todo_notes(physical_line):
    if pycodestyle.noqa(physical_line):
        return
    match = NOTE_REGEX.search(physical_line)
    if match:
        return match.start(), 'T000 Todo note found.'


check_todo_notes.name = name = 'flake8-todo'
check_todo_notes.version = __version__

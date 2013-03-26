
__version__ = '0.1'

import re

import pep8

NOTE_REGEX = re.compile(r'(TODO|FIXME)')  # noqa


def check_todo_notes(physical_line):
    if pep8.noqa(physical_line):
        return
    match = NOTE_REGEX.search(physical_line)
    if match:
        return match.start(), 'T000 Todo note found.'


check_todo_notes.name = name = 'flake8-todo'
check_todo_notes.version = __version__

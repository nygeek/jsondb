""" JSON DB Editor

    Using a JSON Database loaded by jsondb_loader, select a single
    item and edit it.  The result is a modified in-memory database
    object.  A separate class, jsondb-rewriter, will create a stable
    copy.

    Each record is a dictionary with a single key.  The key is what
    an SQL database would call the TABLE name.

    For now we will ASSUME that each TABLE will be stored in a
    single ASCII file, with each record a separate line.
    [ToDo: make it possible for a record to span multiple lines.]

    Each record is be a dictionary with a single key, namely the
    TABLE name.

    The value accessed by the TABLE name will be another dictionary.
    The keys of this dictionary will be the FIELD names of the
    TABLE.  One special key, 'id', will contain the unique ID for
    the row.

    Started 2024-09-25

    Copyright (C) 2024 Marc Donner

"""

from trace_debug import DebugTrace
from jsondb_loader import JDB_Loader

# Python public libraries
import sys
import argparse

# jsondb libraries
import json

class JDB_Editor:
    """Edit a JSONDB object."""

    def __init__(self, jdb):
        """Initialized the editor."""
        self.jdb = jdb


    def __str__(self):
        """Render the JSONDB object readable."""
        for _record in self.jdb:
            _result += json.dumps(_record, indent=2)
        return _result


    def list_jsondb(self):
        """List the IDs of the records in self.jdb."""
        index = 0
        for _record in self.jdb:
            for category in _record.keys():
                unique_id = _record[category]['id']
                print(f"[{index}]: {category}:{unique_id}")
                index += 1


    def dump(self):
        """ dump self.jdb """
        count = 0
        for _record in self.jdb:
            # one per
            print(f"[{count}]: {json.dumps(_record, indent=2)}")
            count += 1


def main():
    """Main - unit test goes here."""
    program_name = sys.argv[0]
    print(f"program_name: {program_name}")
    parser = argparse.ArgumentParser(description='Load a JSONDB file.')
    parser.add_argument(
            "filename",
            nargs='*',
            type=str,
            help="name the file to load"
            )
    args = parser.parse_args()
    for fn in args.filename:
        print(f"loading {fn} ...")
        loader = JDB_Loader(fn)
        loader.load()
        print("loaded.")
        # loader.dump()
        # Now list the database ...
        jdb = loader.jdb
        editor = JDB_Editor(jdb)
        editor.list_jsondb()
    

if __name__ == "__main__":
    main()

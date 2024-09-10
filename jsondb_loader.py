""" JSON DB Loader

    Load a JSON Database into memory from an ASCII file

    Started 2024-09-08

    Copyright (C) 2024 Marc Donner

"""

from trace_debug import DebugTrace

import json

class JDB_Loader:
    """Load a JSON database into memory."""

    def __init__(self, fn):
        """Initialized the loader."""
        self.fn = fn
        self.fd = open(fn, mode="rt", buffering=1)
        self.n_records = 0
        self.jdb = []


    def __str__(self):
        """Render the loader object readable."""
        _result = "fn:" + self.fn + "\n"
        _result += "n_records:" + self.n_records + "\n"
        for _record in self.jdb:
            _result += json.dumps(_record, indent=2)
        return _result


    def load(self):
        """Actually read and parse the JSON documents from the file"""
        line = self.fd.readline()
        while line:
            if line[0] != "#":
                # not a comment ... parse it
                print(f"line: '{line}'")
                jrecord = json.loads(line)
                print(f"i{json.dumps(jrecord, indent=2)}")
            line = self.fd.readline()	


def main():
    """Main - unit test goes here."""
    print("main()")
    loader = JDB_Loader("sample_1.jdb")
    loader.load()
    

if __name__ == "__main__":
    main()

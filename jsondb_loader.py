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


    def dump(self):
        """ dump self.jdb """
        count = 0
        for _record in self.jdb:
            # one per
            print(f"[{count}]: {json.dumps(_record, indent=2)}")
            count += 1


    def load(self):
        """Actually read and parse the JSON documents from the file"""
        count = 0
        line = self.fd.readline().strip()
        while line:
            if line[0] != "#":
                count += 1
                # not a comment empty ... parse it
                # print(f"line: '{line}'")
                jrecord = json.loads(line)
                # print(f"{json.dumps(jrecord, indent=2)}")
                print(f"[{count}]]")
                self.jdb.append(jrecord)
            line = self.fd.readline()	


def main():
    """Main - unit test goes here."""
    print("main()")
    loader = JDB_Loader("sample_1.jdb")
    loader.load()
    print("loaded.")
    loader.dump()
    

if __name__ == "__main__":
    main()

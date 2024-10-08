# JSON DB

Contact: marc.donner@gmail.com

Started: 2024-09-08

This is a simple and relatively stupid database to hold JSON documents.

## Primary functions:

1. Register a JSON document ==> assigns a unique ID

1. Update a JSON document (existing ID and new document)

1. Retrieve a JSON document by unique ID ==> JSON Document

1. Search the repository for documents that match a query
    * The query takes the form of a JSON object containing a list of attribute-value pairs to be matched.
    * Some day implement SQL queries?

The JSON objects will, for now, be stored in an ASCII file.  Starting the database will parse the file and load all of the items into memory.  Checkpointing or exiting will rewrite the ASCII file.

## Assumptions:

1. Each "record" in the database will be stored as a single ASCII string

1. We should probably include an update count along with the unique ID.

1. Each "table" in a conventional database sense will be a separate file.

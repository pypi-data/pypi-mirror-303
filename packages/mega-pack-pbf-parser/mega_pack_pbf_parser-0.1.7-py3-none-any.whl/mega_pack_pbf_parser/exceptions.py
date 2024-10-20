import sqlite3

class DatabaseError(sqlite3.Error):
    def __init__(self, text="No error message was provided.", data=None, *args: object) -> None:
        super().__init__(*args)
        self.text = text
        self.data = data




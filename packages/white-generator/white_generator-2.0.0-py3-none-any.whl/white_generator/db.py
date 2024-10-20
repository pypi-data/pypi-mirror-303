import sqlite3
import pathlib

def connect_to_db() -> sqlite3.Connection:
    db_file = _get_app_dir() / 'notes.db'
    db_connection = sqlite3.connect(db_file)
    with db_connection:
        db_connection.execute('''CREATE TABLE IF NOT EXISTS notes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            text TEXT NOT NULL UNIQUE
        )''')

    return db_connection

def insert_in_db(db_connection: sqlite3.Connection, text: str) -> None:
    with db_connection:
        db_connection.execute('INSERT INTO notes(text) VALUES(?)', (text,))

def exists_in_db(db_connection: sqlite3.Connection, text: str) -> bool:
    (counter,) = db_connection \
        .execute('SELECT count(*) FROM notes WHERE text=?', (text,)) \
        .fetchone()

    return bool(counter)

def _get_app_dir() -> pathlib.Path:
    app_dir = pathlib.Path.home() / ('.' + __package__.replace('_', '-'))
    app_dir.mkdir(parents=True, exist_ok=True)

    return app_dir

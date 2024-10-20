"""Main module."""

import sqlite3
import argparse
import math
import os
import sys
import time
from typing import List
from pathlib import Path
import vlc

class Storage:
    """Manage application memory and storage."""

    def __init__(self, location=None):
        """Initialize the class."""
        if not location:  # pragma: no cover
            # This is the default path when not testing.  But I do not want
            # to blow away actual configurations on this machine while testing.
            location = os.path.join(
                os.path.expanduser("~"), ".local/share/timed-audio-player"
            )
        self.location = location
        Path(self.location).mkdir(parents=True, exist_ok=True)
        self.con = sqlite3.connect(os.path.join(self.location, "data.db"))
        self.current_file = None
        self.position = None
        cur = self.con.cursor()
        cur.execute(
            (
                "CREATE TABLE IF NOT EXISTS playdata"
                "(directory TEXT NOT NULL, "
                "current_file TEXT PRIMARY KEY, "
                "position REAL NOT NULL)"
            )
        )
        cur.close()

    def set_position(self, current_file: str, position):
        """Store the current position of the file."""
        directory = os.path.dirname(current_file)
        cur = self.con.cursor()
        try:
            cur.execute(
                "INSERT INTO playdata (directory, current_file, position) VALUES (?, ?, ?);",
                [directory, current_file, position],
            )
        except sqlite3.IntegrityError:
            cur.execute(
                "UPDATE playdata SET position = ? WHERE current_file = ?",
                [position, current_file],
            )
        cur.close()

    def get_position(self, current_file: str) -> float:
        """Get the current position of a playback file."""
        cur = self.con.cursor()
        cur.execute(
            "SELECT position from playdata where current_file = ?;", [current_file]
        )
        value = cur.fetchone()
        return value[0] if value else 0


    def playback_complete(self, directory):
        """Clear out storage because all files have been played."""
        print(f"DELETING ALL FOR {directory}")
        cur = self.con.cursor()
        cur.execute("DELETE FROM playdata WHERE directory = ?;", [directory])

    def __del__(self):
        """Close the connection."""
        self.con.commit()
        self.con.close()

class Timechecker:  # pylint: disable=too-few-public-methods
    """Determine if we should keep playing."""

    def __init__(self, duration: int):
        """Initialize the class."""
        self.current_time = time.time()
        self.duration = duration

    def check(self) -> bool:
        """Check if we should keep running."""
        return self.current_time + self.duration > time.time()


class Context:  # pylint: disable=too-few-public-methods
    """Hold application state."""

    def __init__(self, directory: str, duration: str):
        """Initialize the context."""
        # Normalize the current directory
        self.directory = os.path.abspath(directory)
        self.duration: int = duration
        self.time_checker = Timechecker(self.duration)
        self.storage = Storage()


def sys_args() -> List[str]:
    """Return the args."""
    return sys.argv[1:]

def main_cli():
    """Implement the CLI entrypoint."""
    parser = argparse.ArgumentParser(
        prog="timed-audio-player",
        description=(
            "An audio player that will play audio files in a "
            "directory for a specified amount of time."
        ),
    )
    parser.add_argument("directory", help="The directory with audio files.")
    parser.add_argument(
        "duration", type=int, help="The amount of time to play the files for."
    )
    args = parser.parse_args(sys_args())
    context = Context(directory=args.directory, duration=args.duration)
    play(context)


def play(context: Context):
    """Play the directory."""
    files = list(os.listdir(context.directory))
    files.sort()
    inst = vlc.Instance()
    for current_file in files:
        current_file = os.path.join(context.directory, current_file)
        if context.time_checker.check():
            play_file(inst, context, current_file)
        else:
            break
    if context.time_checker.check():
        context.storage.playback_complete(context.directory)


def play_file(inst: vlc.Instance, context: Context, current_file: str):
    """Play a file."""
    mp = inst.media_player_new()
    media = inst.media_new(current_file)
    mp.set_media(media)
    position = context.storage.get_position(current_file)
    mp.play()
    mp.set_position(position)
    while context.time_checker.check():
        position = mp.get_position()
        context.storage.set_position(current_file, position)
        try:
            time.sleep(0.1)
        except KeyboardInterrupt as ki:
            mp.stop()
            raise ki
        print(f"Playing {os.path.basename(current_file)}: {position*100:.0f}%\r", end="")
        sys.stdout.flush()
        if math.isclose(position, 0.999, rel_tol=0.001):
            break
    else:
        print("")
        print("Stopping due to time limit")
    mp.stop()

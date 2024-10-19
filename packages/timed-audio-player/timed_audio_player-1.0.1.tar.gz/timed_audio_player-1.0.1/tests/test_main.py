"""Test the main module."""

import pytest
from py.path import LocalPath  # pylint: disable=import-error
from mockito import expect, any_, mock
from timed_audio_player import main as sut


def test_sys_args():
    """Test the sys_args function."""
    result = sut.sys_args()
    # This can vary since we're actually goint to see the args
    # used to call pytest.
    assert result


def test_main_cli_with_no_options(capsys):
    """Test main_cli function function with no options."""
    expect(sut, times=0).play(any_(sut.Context))
    expect(sut, times=1).sys_args().thenReturn([])
    with pytest.raises(SystemExit):
        sut.main_cli()
    captured = capsys.readouterr()
    assert "the following arguments are required: directory" in captured.err


def test_main_cli_with_a_directory(capsys):
    """Test main_cli function function with only a directory."""
    expect(sut, times=0).play(any_(sut.Context))
    expect(sut, times=1).sys_args().thenReturn(["/tmp"])
    with pytest.raises(SystemExit):
        sut.main_cli()
    captured = capsys.readouterr()
    assert "the following arguments are required: duration" in captured.err


def test_main_cli_with_a_directory_and_duration():
    """Test main_cli function function with only a directory and duration."""
    mock_context = mock(spec=sut.Context, strict=True)
    expect(sut, times=1).Context(directory="/tmp", duration=40).thenReturn(mock_context)
    expect(sut, times=1).play(mock_context)
    expect(sut, times=1).sys_args().thenReturn(["/tmp", "40"])
    sut.main_cli()


@pytest.fixture(name="mock_instance")
def mock_instance_fixture():
    """Create the mock_instance."""
    yield mock(spec=sut.vlc.Instance, strict=True)


@pytest.fixture(name="mock_storage")
def mock_storage_fixture():
    """Create the mock_storage."""
    yield mock(spec=sut.Storage, strict=True)


@pytest.fixture(name="mock_time_checker")
def mock_time_checker_fixture():
    """Create the mock_time_checker."""
    yield mock(spec=sut.Timechecker, strict=True)


@pytest.fixture(name="audio_directory")
def audio_directory_fixture(tmpdir: LocalPath):
    """Create the audio_directory."""
    mp3_dir = tmpdir.mkdir("audio")
    mp3 = mp3_dir.join("1.mp3")
    mp3.write("mocked")
    mp3 = mp3_dir.join("2.mp3")
    mp3.write("mocked")
    mp3 = mp3_dir.join("3.mp3")
    mp3.write("mocked")
    yield mp3_dir


@pytest.fixture(name="mock_context")
def mock_context_fixture(mock_storage, mock_time_checker, audio_directory):
    """Create the mock_context."""
    mock_context = mock(spec=sut.Context, strict=True)
    mock_context.directory = str(audio_directory.realpath())
    mock_context.time_checker = mock_time_checker
    mock_context.storage = mock_storage
    yield mock_context


def test_play_without_enough_time(
    mock_time_checker, mock_context, mock_instance, audio_directory
):
    """Test the play function without enough time."""
    expect(sut.vlc).Instance().thenReturn(mock_instance)
    expect(mock_time_checker).check().thenReturn(True).thenReturn(True).thenReturn(
        False
    ).thenReturn(False)
    expect(sut, times=1).play_file(
        mock_instance, mock_context, str(audio_directory.join("1.mp3"))
    )
    expect(sut, times=1).play_file(
        mock_instance, mock_context, str(audio_directory.join("2.mp3"))
    )
    sut.play(mock_context)


def test_play_with_too_much_time(
    mock_storage, mock_time_checker, mock_context, mock_instance, audio_directory
):
    """Test the play function with too much time."""
    expect(sut.vlc).Instance().thenReturn(mock_instance)
    expect(mock_time_checker).check().thenReturn(True).thenReturn(True).thenReturn(
        True
    ).thenReturn(True)
    expect(sut, times=1).play_file(
        mock_instance, mock_context, str(audio_directory.join("1.mp3"))
    )
    expect(sut, times=1).play_file(
        mock_instance, mock_context, str(audio_directory.join("2.mp3"))
    )
    expect(sut, times=1).play_file(
        mock_instance, mock_context, str(audio_directory.join("3.mp3"))
    )
    expect(mock_storage, times=1).playback_complete(mock_context.directory)
    sut.play(mock_context)


def test_play_file_read_end_of_file(
    audio_directory, mock_instance, mock_context, mock_storage, mock_time_checker
):
    """Test the play_file function when you reach the end of file."""
    current_file = str(audio_directory.join("1.mp3"))
    mock_media_player = mock()
    mock_media = mock()
    expect(mock_instance).media_player_new().thenReturn(mock_media_player)
    expect(mock_instance).media_new(current_file).thenReturn(mock_media)
    expect(mock_media_player).set_media(mock_media)
    expect(mock_storage).get_position(current_file).thenReturn(0.0)
    expect(mock_media_player).play()
    expect(mock_media_player).set_position(0.0)
    expect(mock_time_checker, times=2).check().thenReturn(True).thenReturn(True)
    expect(mock_media_player).get_position().thenReturn(0.0).thenReturn(0.999)
    expect(mock_storage).set_position(current_file, 0.0)
    expect(mock_storage).set_position(current_file, 0.999)
    expect(mock_media_player).stop()
    sut.play_file(mock_instance, mock_context, current_file)


def test_play_file_stop_due_to_limit(
    audio_directory, mock_instance, mock_context, mock_storage, mock_time_checker
):
    """Test the play_file function when you stop due to time limit."""
    current_file = str(audio_directory.join("1.mp3"))
    mock_media_player = mock()
    mock_media = mock()
    expect(mock_instance).media_player_new().thenReturn(mock_media_player)
    expect(mock_instance).media_new(current_file).thenReturn(mock_media)
    expect(mock_media_player).set_media(mock_media)
    expect(mock_storage).get_position(current_file).thenReturn(0.0)
    expect(mock_media_player).play()
    expect(mock_media_player).set_position(0.0)
    expect(mock_time_checker, times=2).check().thenReturn(True).thenReturn(False)
    expect(mock_media_player).get_position().thenReturn(0.0).thenReturn(0.512)
    expect(mock_storage).set_position(current_file, 0.0)
    expect(mock_storage).set_position(current_file, 0.512)
    expect(mock_media_player).stop()
    sut.play_file(mock_instance, mock_context, current_file)


def test_play_file_keyboard_interrupt(
    audio_directory, mock_instance, mock_context, mock_storage, mock_time_checker
):
    """Test the play_file function when you reach the end of file."""
    current_file = str(audio_directory.join("1.mp3"))
    mock_media_player = mock()
    mock_media = mock()
    expect(mock_instance).media_player_new().thenReturn(mock_media_player)
    expect(mock_instance).media_new(current_file).thenReturn(mock_media)
    expect(mock_media_player).set_media(mock_media)
    expect(mock_storage).get_position(current_file).thenReturn(0.0)
    expect(mock_media_player).play()
    expect(mock_media_player).set_position(0.0)
    expect(mock_time_checker, times=2).check().thenReturn(True).thenReturn(
        True
    ).thenReturn(True)
    expect(mock_media_player).get_position().thenReturn(0.0).thenReturn(0.521)
    expect(mock_storage).set_position(current_file, 0.0)
    expect(mock_storage).set_position(current_file, 0.521)
    expect(sut.time).sleep(0.1).thenReturn().thenReturn().thenRaise(KeyboardInterrupt())
    expect(mock_media_player).stop()
    with pytest.raises(KeyboardInterrupt):
        sut.play_file(mock_instance, mock_context, current_file)


def test_context(mock_time_checker, mock_storage):
    """Test the Context class."""
    expect(sut).Timechecker(60).thenReturn(mock_time_checker)
    expect(sut).Storage().thenReturn(mock_storage)
    c = sut.Context("/tmp", 60)
    assert c.directory == "/tmp"
    assert c.duration == 60
    assert c.time_checker == mock_time_checker
    assert c.storage == mock_storage


def test_timechecker():
    """Test the Timechecker class."""
    t = sut.Timechecker(1)
    assert t.check()
    sut.time.sleep(1)
    assert not t.check()


def test_storage_init():
    """Test the storage class initialization."""
    mock_cursor = mock(spec=sut.sqlite3.Cursor, strict=True)
    mock_connection = mock(spec=sut.sqlite3.Connection, strict=True)
    expect(sut.sqlite3).connect(any_(str)).thenReturn(mock_connection)
    expect(mock_connection).cursor().thenReturn(mock_cursor)
    expect(mock_cursor).execute(
        (
            "CREATE TABLE IF NOT EXISTS playdata"
            "(directory TEXT NOT NULL, "
            "current_file TEXT PRIMARY KEY, "
            "position REAL NOT NULL)"
        )
    )
    expect(mock_cursor).close()
    expect(mock_connection).commit()
    expect(mock_connection).close()


def test_storage_position(tmpdir: LocalPath, audio_directory):
    """Test position functionality of the Storage class."""
    current_file = str(audio_directory.join("1.mp3"))
    s = sut.Storage(location=str(tmpdir))
    s.set_position(current_file, 0.51)
    assert s.get_position(current_file) == 0.51
    s.set_position(current_file, 0.52)
    assert s.get_position(current_file) == 0.52


def test_storage_playback_complete(tmpdir: LocalPath, audio_directory):
    """Test the playback_complete method of the Storage class."""
    current_file = str(audio_directory.join("1.mp3"))
    s = sut.Storage(location=str(tmpdir))
    s.set_position(current_file, 0.51)
    cur = s.con.cursor()
    cur.execute("SELECT * FROM playdata where directory = ?", (str(audio_directory),))
    rs = cur.fetchall()
    assert len(rs) == 1
    assert len(rs[0]) == 3
    assert rs[0][0].endswith("audio")
    assert rs[0][1].endswith("audio/1.mp3")
    assert rs[0][2] == 0.51
    s.playback_complete(str(audio_directory))
    cur.execute("SELECT * FROM playdata where directory = ?", (str(audio_directory),))
    rs = cur.fetchall()
    assert len(rs) == 0

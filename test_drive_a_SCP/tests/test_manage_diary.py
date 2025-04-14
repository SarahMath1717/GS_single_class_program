from lib.manage_diary import *

def test_init_words():
    entry = DiaryEntry("Monday Golden Square", "Let's find out if I know what I'm doing this week")
    assert entry.title == "Monday Golden Square"
    assert entry.contents == "Let's find out if I know what I'm doing this week"


def test_format():
    entry = DiaryEntry("Monday Golden Square", "Let's find out if I know what I'm doing this week")
    result = entry.format()
    assert result == "Monday Golden Square: Let's find out if I know what I'm doing this week"


def test_count_words():
    entry = DiaryEntry("Monday Golden Square", "Let's find out if I know what I'm doing this week")
    result = entry.count_words()
    assert result == 11


def test_reading_time():
    entry = DiaryEntry("Monday Golden Square", "Let's find out if I know what I'm doing this week")
    result = entry.reading_time(6) #6 is the WPM reading level, diary owner little sister trying to spy
    assert result == 2 #rounded up to nearest interger


def test_reading_chunk():
    entry = DiaryEntry("Monday Golden Square", "Let's find out if I know what I'm doing this week. Actually it's been pretty good so far.")

    chunk1 = entry.reading_chunk(6, 1) #6 WPM, 1 minute reading block
    assert chunk1 == "Let's find out if I know"

    chunk2 = entry.reading_chunk(6, 1)
    assert chunk2 == "what I'm doing this week. Actually"

    chunk3 = entry.reading_chunk(6, 1)
    assert chunk3 == "it's been pretty good so far."

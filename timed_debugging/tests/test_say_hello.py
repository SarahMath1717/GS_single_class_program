from lib.say_hello import *

def test_say_hello():
    result = say_hello("kay")
    assert result == "hello kay"
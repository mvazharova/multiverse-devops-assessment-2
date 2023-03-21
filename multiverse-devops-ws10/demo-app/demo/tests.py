from demo import *

def test_hello():
    assert hello() == 'Hello World!'
def test_concat():
    assert concat('foo', 'bar') == 'foo-bar'
def test_uppercase():
    assert uppercase('foo') == 'FOO'
    assert uppercase('bar') == 'BAR'
    
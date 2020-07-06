from app.targets import *
import pytest



def test_expand_input_line_single():
    assert expand_input_line('192.168.1.1:10000') == \
           [('192.168.1.1', 10000)]
    assert expand_input_line('example.com:12345') == \
           [('example.com', 12345)]


def test_expand_input_line_multi_port():
    assert expand_input_line('192.168.1.1:10000-10005') == \
           [('192.168.1.1', 10000),
            ('192.168.1.1', 10001),
            ('192.168.1.1', 10002),
            ('192.168.1.1', 10003),
            ('192.168.1.1', 10004),
            ('192.168.1.1', 10005)]

def test_expand_input_line_multi_ip_port():
    assert expand_input_line('192.168.1.1-2:10-12') == \
           [('192.168.1.1', 10),
            ('192.168.1.1', 11),
            ('192.168.1.1', 12),
            ('192.168.1.2', 10),
            ('192.168.1.2', 11),
            ('192.168.1.2', 12)]

@pytest.mark.parametrize('inp', ['192.168.1.1:114514',
                                 '192.168.1.1:0',
                                 '192.168.1-10.1:65530-65536',
                                 '192.168.1.1:',
                                 '192.168.1.1',
                                 '192.168.1.1:三天之内杀了你'])
def test_illegal_expand_input_line(inp):
    with pytest.raises(ValueError):
        expand_input_line(inp)



def test_parse_input_single():
    assert parse_input('192.168.1.1:10000') == [('192.168.1.1', 10000)]

@pytest.mark.parametrize('inp', ['192.168.1.1:10000, 192.168.1.2:10000',
                                 '192.168.1.1:10000 , 192.168.1.2:10000',
                                 '192.168.1.1:10000 \n 192.168.1.2:10000',
                                 '192.168.1.1:10000 192.168.1.2:10000'])
def test_parse_input_two(inp):
    assert parse_input(inp) ==\
           [('192.168.1.1', 10000), ('192.168.1.2', 10000)]

def test_parse_input_three():
    assert parse_input('localhost:1\nlocalhost:2\nlocalhost:3') == \
            [('localhost', 1),
             ('localhost', 2),
             ('localhost', 3)]

def test_parse_multi_var():
    assert parse_input('p1-3.example.com:80-81, 192.168.1.1-2:1-2') == \
           [('p1.example.com', 80),
            ('p1.example.com', 81),
            ('p2.example.com', 80),
            ('p2.example.com', 81),
            ('p3.example.com', 80),
            ('p3.example.com', 81),
            ('192.168.1.1', 1),
            ('192.168.1.1', 2),
            ('192.168.1.2', 1),
            ('192.168.1.2', 2)]
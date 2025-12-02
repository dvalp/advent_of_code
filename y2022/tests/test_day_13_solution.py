import pytest
from src.day_13_solution import process_packets, get_decoder_key


@pytest.fixture
def message_packets():
    return """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".split("\n\n")


def test_get_shortest_path_from_start(message_packets):
    assert process_packets(message_packets) == 13


def test_get_decoder_key(message_packets):
        assert get_decoder_key(message_packets) == 140

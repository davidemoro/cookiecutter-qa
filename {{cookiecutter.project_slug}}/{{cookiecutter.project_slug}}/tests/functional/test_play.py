import os


def test_play(play_json, data_getter):
    data = data_getter(
        os.path.abspath(os.path.dirname(__file__)),
        'data',
        'play.json')
    play_json.execute(data)

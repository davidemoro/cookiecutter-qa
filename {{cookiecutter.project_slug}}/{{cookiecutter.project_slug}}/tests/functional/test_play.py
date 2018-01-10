import os


def test_play(play_json):
    data = play_json.get_file_contents(
        os.path.dirname(__file__),
        'data',
        'play.json')
    play_json.execute(data)

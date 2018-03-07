

def test_play(play_json, data_base_path):
    data = play_json.get_file_contents(
        data_base_path,
        'play.json')
    play_json.execute(data)

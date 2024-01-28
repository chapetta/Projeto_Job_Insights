from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path_mock = 'tests/mocks/brazilians_jobs.csv'
    result = {'title': 'Maquinista', 'salary': '2000', 'type': 'trainee'}
    result_2 = {'titulo': 'Maquinista', 'slario': '2000', 'tipo': 'trainee'}

    assert read_brazilian_file(path_mock)[0] == result
    assert read_brazilian_file(path_mock)[0] != result_2

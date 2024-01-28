from src.pre_built.counter import count_ocurrences


def test_counter():
    path = 'data/jobs.csv'

    assert count_ocurrences(path, 'python') == 1639
    assert count_ocurrences(path, 'python') != 1633
    assert count_ocurrences(path, 'javascript') == 122
    assert count_ocurrences(path, 'zero opções') == 0
    assert count_ocurrences(path, 'PYTHON') == 1639
    assert count_ocurrences(path, 'JAVAscript') == 122

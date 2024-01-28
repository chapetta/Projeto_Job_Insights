from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"min_salary": 50, "max_salary": 70000, "date_posted": "2022-01-10"},
        {"min_salary": 60, "max_salary": 80000, "date_posted": "2022-01-15"},
        {"min_salary": 45, "max_salary": 75000, "date_posted": "2022-01-05"},
        {"min_salary": 70, "max_salary": 90000, "date_posted": "2022-01-20"},
        {"min_salary": 55, "max_salary": 85000, "date_posted": "2022-01-12"},
        {"min_salary": 80, "max_salary": 100000, "date_posted": "2022-01-25"},
    ]

    sort_by(jobs, "min_salary")
    assert [job["min_salary"] for job in jobs] == [45, 50, 55, 60, 70, 80]

    sort_by(jobs, "max_salary")
    result = [100000, 90000, 85000, 80000, 75000, 70000]
    assert [job["max_salary"] for job in jobs] == result

    sort_by(jobs, "date_posted")
    result_2 = [
        "2022-01-25",
        "2022-01-20",
        "2022-01-15",
        "2022-01-12",
        "2022-01-10",
        "2022-01-05"
    ]
    assert [job["date_posted"] for job in jobs] == result_2

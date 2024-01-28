from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    file = read(path)
    list_of_max_salaries = []
    for item in file:
        if item['max_salary'] != '':
            try:
                max_salary_value = int(item['max_salary'])
                list_of_max_salaries.append(max_salary_value)
            except ValueError:
                pass
    return max(list_of_max_salaries)


def get_min_salary(path: str) -> int:
    file = read(path)
    list_of_min_salaries = []
    for item in file:
        if item['min_salary'] != '':
            try:
                min_salary_value = int(item['min_salary'])
                list_of_min_salaries.append(min_salary_value)
            except ValueError:
                pass
    return min(list_of_min_salaries)


def validate_salary_fields(job: Dict):
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError("must be present in the job dictionary.")


def validate_numeric_values(value, field_name):
    if not isinstance(value, (int, str)):
        raise ValueError("must be a int or a str representing a number.")


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    validate_salary_fields(job)

    min_salary = job['min_salary']
    max_salary = job['max_salary']

    validate_numeric_values(min_salary, 'min_salary')
    validate_numeric_values(max_salary, 'max_salary')
    validate_numeric_values(salary, 'salary')

    min_salary, max_salary, salary = map(int, [min_salary, max_salary, salary])

    if min_salary >= max_salary:
        raise ValueError("must be less than the value of 'max_salary'.")

    return min_salary <= salary <= max_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError

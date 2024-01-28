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


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError("Both 'min_salary' and 'max_salary' must be present in the job dictionary.")
    
    min_salary = job['min_salary']
    max_salary = job['max_salary']

    if type(min_salary) != int or type(max_salary) != int:
         raise ValueError("Both 'min_salary' and 'max_salary' must be numeric values or strings representing numbers.")
    if min_salary >= max_salary:
         raise ValueError("The value of 'min_salary' must be less than or equal to the value of 'max_salary'.")
    if not isinstance(salary, (int, str)):
         raise ValueError("The parameter 'salary' must be a numeric value or a string representing a number.")
    try:
        salary = int(salary)
    except ValueError:
        raise ValueError("Invalid numeric value for 'salary'.")

    return min_salary <= salary <= max_salary
    # Returns
    # -------
    # bool
    #     True if the salary is in the salary range of the job, False otherwise

    # Raises
    # ------
    # ValueError
    #     If `job["min_salary"]` or `job["max_salary"]` doesn't exists
    #     If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
    #     If `job["min_salary"]` is greather than `job["max_salary"]`
    #     If `salary` isn't a valid integer
    # """
    # raise NotImplementedError


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

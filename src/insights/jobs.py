from functools import lru_cache
from typing import List, Dict
import csv

@lru_cache
def read(path: str) -> List[Dict]:
    result = []
    try:
        with open(path, encoding='utf-8') as file:
            content = csv.DictReader(file, delimiter=',', quotechar='"')
            for row in content:
                result.append(row)
    except FileNotFoundError:
        print(f'Ops! parece que houve um erro ao encontrar o arquivo {path}')
    return result
def get_unique_job_types(path: str) -> List[str]:
    content = read(path)
    list_of_job_types = []
    for item in content:
        list_of_job_types.append(item['job_type'])
    return list(set(list_of_job_types))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError

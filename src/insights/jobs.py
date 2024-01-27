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
    list_of_jobs = [job for job in jobs if job['job_type'] == job_type]
    return list_of_jobs
from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    file = read(path)
    results = []
    for item in file:
        if item['industry'] != '':
            results.append(item['industry'])
    return list(set(results))


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    list_of_industries = [item for item in jobs if item['industry'] == industry]
    return list_of_industries

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
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError

import sys
import os
from typing import List, Dict
from .unswJobTypes import JobTypes

# returns a list of job types and values
# will return a str and int tuple
def getAllUNSWJobTypes() -> List[Dict]:
    result = []
    for jobType in JobTypes:
        result.append({
            "jobType": jobType, 
            "jobId": JobTypes[jobType]
        })
    return result




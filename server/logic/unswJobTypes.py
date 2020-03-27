import sys
import os
from typing import List, Dict

JobTypes = {
  "any": -1,
  "part-time-casual-employment": 1138,
  "vacation-employment-internships": 1139,
  "full-time-entry-level": 1140,
  "structured-graduate-program": 1164,
  "experienced-professional-employment": 1141,
  "full-time": 1142,
  "contract": 1143,
  "volunteering": 1144,
  "overseas-employment": 1145,
  "international-students": 1146,
  "on-Campus-employment": 1147,
  "postgraduates": 1148,
  "scholarships-cadetships": 1149,
  "disability-program": 1175,
  "indigenous-program": 1176,
  "equal-opportunity-program": 1177
}

def getUnswJobTypes() -> (List[Dict]):
    return [{'jobType': jobType, 'jobId': JobTypes[jobType]} for jobType in JobTypes]




import pandas as pd

def dataset_mapping(data: pd.DataFrame) -> pd.DataFrame:
    # Define mappings
    MSSubClass_mapping = {
        20: '1-STORY 1946 & NEWER ALL STYLES',
        30: '1-STORY 1945 & OLDER',
        40: '1-STORY W/FINISHED ATTIC ALL AGES',
        45: '1-1/2 STORY - UNFINISHED ALL AGES',
        50: '1-1/2 STORY FINISHED ALL AGES',
        60: '2-STORY 1946 & NEWER',
        70: '2-STORY 1945 & OLDER',
        75: '2-1/2 STORY ALL AGES',
        80: 'SPLIT OR MULTI-LEVEL',
        85: 'SPLIT FOYER',
        90: 'DUPLEX - ALL STYLES AND AGES',
        120: '1-STORY PUD (Planned Unit Development) - 1946 & NEWER',
        150: '1-1/2 STORY PUD - ALL AGES',
        160: '2-STORY PUD - 1946 & NEWER',
        180: 'PUD - MULTILEVEL - INCL SPLIT LEV/FOYER',
        190: '2 FAMILY CONVERSION - ALL STYLES AND AGES'
    }

    OverallQual_mapping = {
        10: 'Very Excellent',
        9: 'Excellent',
        8: 'Very Good',
        7: 'Good',
        6: 'Above Average',
        5: 'Average',
        4: 'Below Average',
        3: 'Fair',
        2: 'Poor',
        1: 'Very Poor'
    }

    OverallCond_mapping = OverallQual_mapping

    # Apply mappings
    data['MSSubClass'] = data['MSSubClass'].map(MSSubClass_mapping)
    data['OverallQual'] = data['OverallQual'].map(OverallQual_mapping)
    data['OverallCond'] = data['OverallCond'].map(OverallCond_mapping)

    return data

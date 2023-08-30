import pandas as pd
import numpy as np

censo2020 = pd.read_csv("data/censo2020_filtrado.csv")
censo2021 = pd.read_csv("data/censo2021_filtrado.csv")

def getValuesForEvasion(objeto2020, objeto2021):
    merged_df = pd.merge(objeto2020, objeto2021, on='CO_CURSO', suffixes=('_2020', '_2021'))
    results_df = merged_df[['QT_MAT_2021', 'QT_ING_2021', 'QT_MAT_2020', 'QT_ING_2020']]
    results = results_df.values.tolist()
    print('results',results)
    return results


def getColumUniqueNames(colum_name):
    unique_course_names = censo2020[colum_name].unique()
    course_names_list = np.unique(unique_course_names).tolist()
    return course_names_list


def find_and_get_matching_courses(colum_name, searchName):
    course_data_2020 = censo2020[censo2020[colum_name] == searchName]
    course_data_2021 = censo2021[censo2021[colum_name].str.upper() == searchName]

    if not course_data_2020.empty and not course_data_2021.empty:
        unique_codes_2020 = course_data_2020["CO_CURSO"].unique()
        unique_codes_2021 = course_data_2021["CO_CURSO"].unique()
        common_course_codes = np.intersect1d(unique_codes_2020, unique_codes_2021)

        matching_rows_2020 = censo2020[censo2020["CO_CURSO"].isin(common_course_codes)]
        matching_rows_2021 = censo2021[censo2021["CO_CURSO"].isin(common_course_codes)]

        values = getValuesForEvasion(matching_rows_2020, matching_rows_2021)
        return [values, [matching_rows_2020, matching_rows_2021]]
      
    else:
        return None, None

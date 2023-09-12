import pandas as pd
import numpy as np
import dataFactory
import streamlit as st

censo2020 = pd.read_csv("data/censo2020_filtrado.csv")
censo2021 = pd.read_csv("data/censo2021_filtrado.csv")

def testFunction():
    return [censo2020, censo2021]

def getValuesForAge(colum_name,searchName):
    # Filtrar dados com base no nome do curso
    course_data_2020 = censo2020[censo2020[colum_name] == searchName]
    course_data_2021 = censo2021[censo2021[colum_name].str.upper() == searchName]

    if not course_data_2020.empty and not course_data_2021.empty:
        unique_codes_2020 = course_data_2020["CO_CURSO"].unique()
        unique_codes_2021 = course_data_2021["CO_CURSO"].unique()
        common_course_codes = np.intersect1d(unique_codes_2020, unique_codes_2021)

        # Aplicar filtros adicionais
        filtered_rows_2020 = censo2020[censo2020["CO_CURSO"].isin(common_course_codes)]
        filtered_rows_2021 = censo2021[censo2021["CO_CURSO"].isin(common_course_codes)]

        return [filtered_rows_2020, filtered_rows_2021]

    else:
        return None


def getValuesForEvasion(objeto2020, objeto2021):
    merged_df = pd.merge(
        objeto2020, objeto2021, on="CO_CURSO", suffixes=("_2020", "_2021")
    )
    results_df = merged_df[["QT_MAT_2021", "QT_ING_2021", "QT_MAT_2020", "QT_ING_2020"]]
    results = results_df.values.tolist()
    print("results", results)
    return results


def getColumUniqueNames(colum_name):
    unique_course_names = censo2020[colum_name].unique()
    course_names_list = np.unique(unique_course_names).tolist()
    return course_names_list


def find_and_get_matching_courses(colum_name, searchName, org_type=None, network_type=None, modality=None, gender=None
):
    # Filtrar dados com base no nome do curso
    course_data_2020 = censo2020[censo2020[colum_name] == searchName]
    course_data_2021 = censo2021[censo2021[colum_name].str.upper() == searchName]

    if not course_data_2020.empty and not course_data_2021.empty:
        unique_codes_2020 = course_data_2020["CO_CURSO"].unique()
        unique_codes_2021 = course_data_2021["CO_CURSO"].unique()
        common_course_codes = np.intersect1d(unique_codes_2020, unique_codes_2021)

        # Aplicar filtros adicionais
        filtered_rows_2020 = censo2020[censo2020["CO_CURSO"].isin(common_course_codes)]
        filtered_rows_2021 = censo2021[censo2021["CO_CURSO"].isin(common_course_codes)]

        if org_type is not None and dataFactory.getOrganizacao(org_type):
            filtered_rows_2020 = filtered_rows_2020[
                filtered_rows_2020["TP_ORGANIZACAO_ACADEMICA"]
                == dataFactory.getOrganizacao(org_type)
            ]
            filtered_rows_2021 = filtered_rows_2021[
                filtered_rows_2021["TP_ORGANIZACAO_ACADEMICA"]
                == dataFactory.getOrganizacao(org_type)
            ]

        if network_type is not None and dataFactory.getNetworkType(network_type):
            filtered_rows_2020 = filtered_rows_2020[
                filtered_rows_2020["TP_REDE"]
                == dataFactory.getNetworkType(network_type)
            ]
            filtered_rows_2021 = filtered_rows_2021[
                filtered_rows_2021["TP_REDE"]
                == dataFactory.getNetworkType(network_type)
            ]

        if modality is not None and dataFactory.getModality(modality):
            filtered_rows_2020 = filtered_rows_2020[
                filtered_rows_2020["TP_MODALIDADE_ENSINO"]
                == dataFactory.getModality(modality)
            ]
            filtered_rows_2021 = filtered_rows_2021[
                filtered_rows_2021["TP_MODALIDADE_ENSINO"]
                == dataFactory.getModality(modality)
            ]

        # Obter os valores relevantes para o cálculo da taxa de evasão
        values = getValuesForEvasion(filtered_rows_2020, filtered_rows_2021)
        return [values, [filtered_rows_2020, filtered_rows_2021]]

    else:
        return None, None

def getValuesForShift(colum_name,searchName, grauAcademico=None):
    # Filtrar dados com base no nome do curso
    course_data_2020 = censo2020[censo2020[colum_name] == searchName]
    course_data_2021 = censo2021[censo2021[colum_name].str.upper() == searchName]

    if not course_data_2020.empty and not course_data_2021.empty:
        unique_codes_2020 = course_data_2020["CO_CURSO"].unique()
        unique_codes_2021 = course_data_2021["CO_CURSO"].unique()
        common_course_codes = np.intersect1d(unique_codes_2020, unique_codes_2021)

        # Aplicar filtros adicionais
        filtered_rows_2020 = censo2020[censo2020["CO_CURSO"].isin(common_course_codes)]
        filtered_rows_2021 = censo2021[censo2021["CO_CURSO"].isin(common_course_codes)]

        if grauAcademico is not None and dataFactory.getOrganizacao(grauAcademico):
            filtered_rows_2020 = filtered_rows_2020[
                filtered_rows_2020["TP_GRAU_ACADEMICO"]
                == dataFactory.getOrganizacao(grauAcademico)
            ]
            filtered_rows_2021 = filtered_rows_2021[
                filtered_rows_2021["TP_GRAU_ACADEMICO"]
                == dataFactory.getOrganizacao(grauAcademico)
            ]

        return [filtered_rows_2020, filtered_rows_2021]

    else:
        return None
    
def getRawdata():
    # Filtrar dados com base no nome do curso
    course_data_2020 = censo2020
    course_data_2021 = censo2021

    return [course_data_2020, course_data_2021]


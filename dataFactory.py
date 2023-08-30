def getOrganizacao(name):
    org_mapping = {
        "Universidade": 1,
        "Centro universitario": 2,
        "Faculdade": 3,
        "Instituto Federal de Educação, Ciência e Tecnologia": 4,
        "Centro Federal de Educação Tecnológica": 5,
    }
    return org_mapping.get(name, False)


def getModality(name):
    org_mapping = {"Presencial": 1, "Curso a distância": 2}
    return org_mapping.get(name, False)


def getNetworkType(name):
    org_mapping = {"Pública": 1, "Privada": 2}
    return org_mapping.get(name, False)

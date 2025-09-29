# main.py
import pandas as pd
from utils.clinvar_api import consulta_clinvar
from utils.ensembl_api import consulta_ensembl

def analisar_variantes(variantes):
    resultados = []

    for var in variantes:
        clinvar_info = consulta_clinvar(var)
        ensembl_info = consulta_ensembl(var)

        combinado = {**clinvar_info, **ensembl_info}
        resultados.append(combinado)

    return pd.DataFrame(resultados)

if __name__ == "__main__":
    # Exemplo: mutações de teste
    variantes = ["NM_000162.5:c.626C>T"]  # Exemplo: gene GCK

    df = analisar_variantes(variantes)
    df.to_csv("output/relatorio.csv", index=False)
    print("Relatório salvo em output/relatorio.csv")
    print(df)

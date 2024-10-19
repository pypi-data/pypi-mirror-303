# -*- coding: utf-8 -*-
"""
Realiza a avaliação de trabalhos na Feira de Ciências do CAp-UERJ.

Usage:
    afc [-i --input=<input>] [-o --output=<output>]
    afc (-h | --help)
    afc (-v | --version)

Options:
    -h --help                         Mostra esta tela.
    -v --version                      Mostra a versão.
    -i <input>, --input=<input>       Arquivo de entrada.
    -o <output>, --output=<output>    Arquivo de saída.

"""

from datetime import datetime as dt
import pathlib as pl
import os

from docopt import docopt
import pandas as pd


__author__ = "Beethoven Santos (https://github.com/bthoven)"
__version__ = "24.10.19"


def remove_prefix_from_keys(prefix, dicionary):
    """Remove um dado prefixo do início das chaves em um dicionário."""
    dicionary_new = dicionary.copy()
    for arg in dicionary:
        new_arg = arg[len(prefix) :] if arg.startswith(prefix) else arg
        dicionary_new[new_arg] = dicionary_new.pop(arg)
    return dicionary_new


def get_output_filename(input_filename: str) -> str:
    r"""
    Cria o nome do arquivo de saída a partir do nome do arquivo de entrada.

    Parameters
    ----------
    input_filename : <str>
        O nome do arquivo de entrada.

    Returns
    -------
    output_filename : <str>
        O nome do arquivo de saída.
    """
    basename = os.path.basename(input_filename)
    basename_without_ext, extension = os.path.splitext(basename)
    extension = extension.replace(".", "")  # Remove the dot from extension
    output_filename = "__".join([basename_without_ext, defaults["OUTPUT_SUFFIX"]])
    return output_filename


def parse_args():
    r"""
    Analisa os argumentos passados pela linha de comando.

    Returns
    -------
    args : <dict>
        Dicionário que armazena os argumentos passados via linha de comando.
    """
    args = docopt(__doc__, version=__version__)
    args = remove_prefix_from_keys("--", args)
    if args["output"] is None:
        args["output"] = get_output_filename(args["input"])
    del args["help"]
    del args["version"]
    return args


def get_work(row):
    r"""
    Obtém o nome do trabalho a partir do código da turma.

    Parameters
    ----------
    row : <dict>
        Dicionário com os pares chave-valor de uma linha do dataframe.

    Returns
    -------
    work : <str>
        O nome do trabalho do grupo.
    """
    work = row[
        " ".join([defaults["WORK_NAME_PREFIX"], row[defaults["CLASS_COLUMN_NAME"]]])
    ]
    return work


def filter_df_by_degree_and_year(
    df: pd.DataFrame, degree: str, year: str
) -> pd.DataFrame:
    r"""
    Filtra um dataframe por grau de ensino e ano de escolaridade..

    Parameters
    ----------
    df : <pd.DataFrame>
        Dataframe a ser filtrado por grau de ensino e ano de escolaridade.

    degree : <str>
        Grau de ensino.

    year : <str>
        Ano de escolaridade.

    Returns
    -------
    <pd.DataFrame>
        Dataframe filtrado por grau de ensino e ano de escolaridade e ordenado
        em ordem descendente pela média das notas.
    """
    return df[
        (df[defaults["DEGREE_COLUMN_NAME"]] == degree)
        & (df[defaults["YEAR_COLUMN_NAME"]] == year)
    ].sort_values(by=defaults["AVERAGE_COLUMN_NAME"], ascending=False)


def run_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    r"""
    Realiza a pipeline do processamento do dataframe.

    Parameters
    ----------
    df : <pd.DataFrame>
        O dataframe a ser processado.

    Returns
    -------
    df_new : <pd.DataFrame>
        O dataframe processado.
    """
    df_new = df.copy()

    # Reduz os dados usando o filtro definido
    df_new = df_new[df_new[defaults["FILTER_COLUMN"]] == "Sim"]

    # Calcula a média das notas
    df_new[defaults["AVERAGE_COLUMN_NAME"]] = df_new[GRADES_COLUMNS].mean(axis=1)

    # Simplifica os nomes de algumas colunas
    df_new.rename(columns=COLUMN_REPLACEMENTS, inplace=True)

    # Obtém o ano de escolaridade a partir do código da turma
    df_new[defaults["YEAR_COLUMN_NAME"]] = df_new[defaults["CLASS_COLUMN_NAME"]].apply(
        lambda value: value[:1]
    )

    # Remove a parte inútil dos valores na coluna de códigos das turmas
    df_new[defaults["CLASS_COLUMN_NAME"]] = df_new[defaults["CLASS_COLUMN_NAME"]].apply(
        lambda value: value.split(" ")[0]
    )

    # Obtém o grau de ensino a partir do código da turma
    df_new[defaults["DEGREE_COLUMN_NAME"]] = df_new[
        defaults["CLASS_COLUMN_NAME"]
    ].apply(lambda value: defaults["CLASS_DEGREE_MAPPING"][value])

    # Condensa todos os valores não vazios das colunas com os trabalhos em
    # apenas uma coluna.
    df_new[defaults["WORK_NAME_COLUMN_NAME"]] = df_new.apply(get_work, axis=1)

    # Organiza as colunas finais do novo dataframe
    df_new = df_new[FINAL_COLUMNS]

    # Separa o dataframe final em diversos dataframes para cada ano de escolaridade
    dataframes = {}
    for degree_year in defaults["DEGREE_YEAR_PAIRS"]:
        degree, year = degree_year
        dataframes[" ".join(degree_year)] = filter_df_by_degree_and_year(
            df_new, degree, year
        )

    return dataframes


def main():
    args = parse_args()

    input_file = args["input"]
    output_file = args["output"]

    # Reads the input data
    df = pd.read_csv(input_file)

    # Process the dataframe
    dfs = run_pipeline(df)

    # Write the output to a .XLSX file
    for dataframe in dfs:
        output_file_path = pl.Path(
            output_file + "__" + dataframe + "__" + EXECUTION_TIME + ".xlsx"
        )
        dfs[dataframe].to_excel(output_file_path, index=False)


defaults = {
    "OUTPUT_SUFFIX": "AVALIADO",
    "FILTER_COLUMN": "Indica o trabalho para a sessão Destaques?",
    "OUTPUT_EXTENSION": "xlsx",
    "WORK_NAME_PREFIX": "Selecione o trabalho da turma",
    "DEGREE_COLUMN_NAME": "Grau de ensino",
    "YEAR_COLUMN_NAME": "Ano de escolaridade",
    "CLASS_COLUMN_NAME": "Turma",
    "WORK_NAME_COLUMN_NAME": "Trabalho",
    "AVERAGE_COLUMN_NAME": "Média",
    "CLASS_DEGREE_MAPPING": {
        "61": "Fundamental",
        "62": "Fundamental",
        "63": "Fundamental",
        "64": "Fundamental",
        "71": "Fundamental",
        "72": "Fundamental",
        "73": "Fundamental",
        "74": "Fundamental",
        "81": "Fundamental",
        "82": "Fundamental",
        "83": "Fundamental",
        "84": "Fundamental",
        "91": "Fundamental",
        "92": "Fundamental",
        "93": "Fundamental",
        "94": "Fundamental",
        "1A": "Médio",
        "1B": "Médio",
        "1C": "Médio",
        "1D": "Médio",
        "2A": "Médio",
        "2B": "Médio",
        "2C": "Médio",
        "2D": "Médio",
    },
    "DEGREE_YEAR_PAIRS": {
        ("Fundamental", "6"),
        ("Fundamental", "7"),
        ("Fundamental", "8"),
        ("Fundamental", "9"),
        ("Médio", "1"),
        ("Médio", "2"),
    },
}

COLUMN_REPLACEMENTS = {
    "Selecione a turma do trabalho a ser avaliado": defaults["CLASS_COLUMN_NAME"],
    "Escreva o nome dos alunos ausentes:": "Alunos ausentes",
}

WORK_NAME_COLUMNS = [
    " ".join([defaults["WORK_NAME_PREFIX"], t])
    for t in defaults["CLASS_DEGREE_MAPPING"].keys()
]

GRADES_COLUMNS = [
    "Notas [Organização geral]",
    "Notas [Clareza na apresentação do trabalho]",
    "Notas [Domínio e conhecimento técnico do conteúdo]",
    "Notas [Trabalho em equipe]",
    "Notas [Postura dos alunos perante os visitantes]",
    "Notas [Criatividade ao abordar o conteúdo]",
]

FINAL_COLUMNS = (
    ["Timestamp", "Nome Completo", "E-mail"]
    + [
        defaults["DEGREE_COLUMN_NAME"],
        defaults["YEAR_COLUMN_NAME"],
        defaults["CLASS_COLUMN_NAME"],
        defaults["WORK_NAME_COLUMN_NAME"],
        defaults["AVERAGE_COLUMN_NAME"],
    ]
    + GRADES_COLUMNS
    + ["O grupo estava completo?", "Alunos ausentes"]
)

EXECUTION_TIME = dt.now().strftime("%Y-%m-%d_%Hh%Mm")

if __name__ == "__main__":
    main()


import re
import pandas as pd
from utils import remove_stopwords, busca_nomes

class IdentificadorPII():

    def __init__(self) -> None: 
        self.patterns = None

    def load_patterns(self) -> dict:
        """
        Carrega os padrões para buscar documentos brasileiros.



        Returns:
            dict: Dicionário com os padrões regex que serão buscados.
        """

        patterns  = {
        'cpf':  r'^\d{11}$|^\d{3}\.\d{3}\.\d{3}-\d{2}$',
        'telefone': r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$',
        'cnh': r'^[A-Z]{2}\d{9}$',
        'email':  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
        'nis': r'\b\d{3}\.\d{5}\.\d{2}-\d{1}\b|\b\d{11}\b'
        }

        self.patterns = patterns

 
    
    def add_pattern(self, pattern_name: str, pattern_regex: str) -> dict:
        """
        Função que adiciona um novo padrão regex a ser buscado

        Args:
            pattern_name (str): nome que será dado ao novo padrão
            pattern_regex (str): reges que registra o comportamento daquele padrão
        """
        self.patterns[pattern_name] = pattern_regex
    
    def remove_pattern(self, pattern_name: str):
        """
        Função que adiciona um novo padrão regex a ser buscado

        Args:
            pattern_name (str): nome que será dado ao novo padrão
        """
        
        self.patterns.pop(pattern_name)


    def classify_column(self, df, coluna):
        """
        Função que clasifica uma única coluna de um dataframe

        Args:
            df (pandas.DataFrame): Conjunto de dados a ser analisao.
            coluna (str): Nome da coluna a ser analisada.

        Returns:
            coluna (str): Nome da coluna.
            nome (str): nome.
            match_count (int): Quantidade de correspondencias encontradas.
            perc_match_count (float): Percentual de correspondencias encontradas.
        """

        self.load_patterns()
        patterns_to_check = self.patterns

        match_counts = {}
        for pattern in patterns_to_check:
            matches = df[coluna].astype(str).str.match(patterns_to_check[pattern], na=False)
            match_counts[pattern] = matches.sum()

        max_matches_col = max(match_counts, key=match_counts.get)
        max_matches_count = match_counts[max_matches_col]
        max_matches_perc = round((max_matches_count / len(df)),2)


        if df[coluna].dtype == object:
            res = busca_nomes(df, coluna)
            if res[2] > max_matches_count:
                pred = 'nome'
                max_matches_count = res[2]
                max_matches_perc = res[3]
                max_matches_col = 'nome'

        if max_matches_count == 0:
            pred = 'any'
            max_matches_col = ''
        elif max_matches_perc <= .3:
            pred = 'other'
        else:
            pred = max_matches_col

        return [coluna, pred, max_matches_col,max_matches_count,  max_matches_perc]


    
    def classify_df(self, df):
        """
        Classifica um dataframe.

        Args:
            df (pandas.DataFrame): Conjunto de dados a ser analisao.

        Returns:
            df (pandas.DataFrame): Dataframe as informações de classificação.
        """
        preds = []
        
        for column in df.columns:
            preds.append(self.classify_column(df, column))
        return pd.DataFrame(preds, columns= ['column_name', 'prediction', 'most_matched_pii','match_count', 'match_perc'])
            

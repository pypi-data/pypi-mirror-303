from collections import Counter

if __name__ == "__main__":
    ...

def remove_stopwords(texto: str):
    """
    Remove as stopwords do texto.

    Args:
        texto (str): Texto a ser processado.
    
    Returns:
        texto (str): Texto sem stopwords.
    """
    stop_words = set([
    'a', 'o', 'e', 'é', 'ao', 'aos', 'à', 'às', 'de', 'do', 'da', 'dos', 'das',
    'em', 'no', 'na', 'nos', 'nas', 'para', 'por', 'com', 'um', 'uma', 'uns', 'umas',
    'que', 'eu', 'tu', 'ele', 'ela', 'nós', 'vós', 'eles', 'elas', 'me', 'te',
    'se', 'nos', 'vos', 'lhe', 'lhes', 'meu', 'teu', 'seu', 'nosso', 'vosso',
    'minha', 'tua', 'sua', 'nossa', 'vossa', 'meus', 'teus', 'seus', 'nossos',
    'vossos', 'minhas', 'tuas', 'suas', 'nossas', 'vossas', 'este', 'esse', 'aquele',
    'esta', 'essa', 'aquela', 'estes', 'esses', 'aqueles', 'estas', 'essas',
    'aquelas', 'isto', 'isso', 'aquilo', 'ou'
    ])

    # Tokenizar o texto e remover as stopwords
    palavras_filtradas = [palavra for palavra in texto.split() if palavra.lower() not in stop_words]

    # Juntar as palavras filtradas de volta em uma string
    texto_filtrado = ' '.join(palavras_filtradas)

    return texto_filtrado

def busca_nomes(df, coluna): 
    """
    Função que busca os nomes e sobrenomes mais comuns no conteúdo da coluna.

    Args:
        df (pandas.DataFrame): Conjunto de dados a ser analisao.
        coluna (str): Nome da coluna a ser analisada.

    Returns:
        coluna (str): Nome da coluna.
        nome (str): nome.
        match_count (int): Quantidade de correspondencias encontradas.
        perc_match_count (float): Percentual de correspondencias encontradas.
    """
    with open('.files\\nomes_e_sobrenomes_comuns.txt', 'r') as arquivo:
            # Ler todas as linhas do arquivo e armazenar em uma lista
            nomes = arquivo.readlines()
    nomes = nomes[0].split(' ')

    valores_a_comparar = df[coluna].str.cat(sep=' ')
    valores_a_comparar = remove_stopwords(valores_a_comparar)
    valores_a_comparar = valores_a_comparar.lower()
    valores_a_comparar = valores_a_comparar.split()

    contagem_nomes = Counter((nome) for nome in valores_a_comparar)
    match_count = sum(contagem for nome, contagem in contagem_nomes.items() if nome in nomes)
    perc_match_count = round(match_count / len(valores_a_comparar), 2)

    return [coluna, 'nome', match_count, perc_match_count]

        
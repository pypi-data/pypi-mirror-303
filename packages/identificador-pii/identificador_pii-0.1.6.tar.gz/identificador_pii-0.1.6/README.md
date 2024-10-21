# Início rápido

## Contexto

 Este projeto PII Brasil consiste no resultado do trabalho de conclusão de curso de Pedro Henrique Camapgna para o MBA em Data Science and Analytics USP Esalq. 

> Este pacote visa criar uma ferramenta simples que pode auxiliar pessoas que trbalham com dados a identificar se em um determinado conjunto de dados, existem dados pessoais. Isso porque, ainda que existem outros pacotes e ferramentas dedicadas a fazer o mesmo, muitos deles não estão costumizados para encontrar dados no padrão brasileiro, desde nomes de pessoas à documentos específicos como o Cadastro de Pessoas Físicas (CPF).



## Instalação 

### Instalando o pacote via pip

<code> pip install identificador-pii </code>

## Documentação

Clique [aqui](https://projeto-pii-brasil.readthedocs.io/en/latest/) para ir para a documentação oficial

## Comece aqui

### Classificando uma coluna de um DataFrame



```python

    from identificador_pii.identificador import IdentificadorPII
    import pandas as pd

    a = IdentificadorPII()


    data = {'coluna1': ['12345678901', '98765432109', '123.456.789-01', '987.654.321-09', '123.456.789.01'],
            'coluna2': ['(11) 1234-5678', '(22) 98765-4321', '12345-6789', '98765-4321', '11 12345-6789'],
            'coluna3': ['Fábio Santos', 'Sergio Conceição', 'Maria Souza', 'João Rodrigues', 'Richard Tomiaka' ],
            'coluna4':[15, 200, 456, 22, 765 ]}
    df = pd.DataFrame(data

    a.clasify_column(df, 'coluna1')

```

![](docs\assets\classify_column_result.png)

### Classificando todas as colunas de um DataFrame


```python

    from identificador_pii.identificador import IdentificadorPII
    import pandas as pd

    data = {'coluna1': ['12345678901', '98765432109', '123.456.789-01', '987.654.321-09', '123.456.789.01'],
            'coluna2': ['(11) 1234-5678', '(22) 98765-4321', '12345-6789', '98765-4321', '11 12345-6789'],
            'coluna3': ['Fábio Santos', 'Sergio Conceição', 'Maria Souza', 'João Rodrigues', 'Richard Tomiaka' ],
            'coluna4':[15, 200, 456, 22, 765 ]}
    df = pd.DataFrame(data)

    a.classify_df(df)
```

![](docs\assets\classify_df_result.png)

### Fluxograma de uso da biblioteca

```mermaid
graph TD;
    %% Definição do fluxo
    A[Início] --> B[Carregar dataset];
    B --> C[Usar biblioteca identificador_pii?];
    C -->|Sim| D[Escolher função];
    C -->|Não| F[Fim];
    
    D --> E1[Classificar uma coluna];
    D --> E2[Classificar todas as colunas];
    
    E1 --> G1[Passar nome da coluna como parâmetro];
    G1 --> H1[Classificar coluna];
    
    H1 --> I1[Verificar resultados];

    E2 --> G2[Classificar todas as colunas do dataframe];
    G2 --> H2[Classificar dataframe];
    H2 --> I2[Verificar resultados];

    I1 --> F[Fim];
    I2 --> F[Fim];

    %% Definindo animações para os nós
    classDef animated fill:#AAA4,stroke:#333,stroke-width:4px,animation: fade-in 2s ease-in-out infinite alternate;

    %% Aplicando animações aos nós para guiar o usuário
    class A,B,C,D,E1,E2,G1,H1,I1,G2,H2,I2,F animated;

```
 <br>

### Badges
<br>

[![Documentation Status](https://readthedocs.org/projects/projeto-pii-brasil/badge/?version=latest)](https://projeto-pii-brasil.readthedocs.io/en/latest/?badge=latest)
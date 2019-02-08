# Contador de Moedas

Trabalho Final da disciplina de Visão computacional (2019/0) da Universidade de Brasília.


## Requisitos

### Modelo 1

Para executar o `modelo I` do software o usuário deve fazer o download do dataset (moedas.rar) de imagens contidos no link abaixo e deixá-lo na pasta raiz do projeto.

```sh
https://www.kaggle.com/durvalcarvalho/thebrazilianrealbrlcentavos
```
É necessário ter o `Jupyter Notebook` no computador para poder abrir os softwares.

Pode ser necessário instalar pacotes que estão sendo usados com o pacote `pip` do Python

### Modelo 2

Caso não tenha o seu próprio `dataset` com moedas, execute em sequência:
*   Faça os imports;
*   Execute as funções: `coin_regions`, `coins_numbers`.
*   Em seguida, execute o bloco que possui a função `main`.
*   Por fim, execute o bloco que está abaixo da função `main` para executar o algoritmo.

Caso tenha o seu próprio `dataset`:
*   Crie uma pasta para treino na raiz do projeto e, em seguida, altere os atributos `folder_src` com o local da pasta que possui as moedas e `folder_out` para o nome da pasta que deseja que o algoritmo salve apenas as imagens das moedas.
    *   A pasta de treino deve possuir sub-pastas da seguinte maneira: `5`, `10`, `25`, `50`, `100`.
    *   Deve-se ter uma moeda por cada imagem.
*   Ao seguir as instruções, a função `create_dataset` irá criar uma pasta com o nome em `folder_out` com moedas isoladas da imagem.

> Para criar `dataset`: passe 0 para `create_dataset` para criar uma pasta de treino e 1 para criar uma pasta de teste.
> OBS: Execute os mesmos passos para criar uma pasta de treino.

*   Nos valores `train_generator` e `validation_generator` coloque o local para as respectivas pastas de treino e teste já processadas pela função `create_dataset`.

## Execução
Para executar o código, basta abrir o notebook a ser executado, clicar na aba `Kernel` e executar o comando `Restart & Run All`

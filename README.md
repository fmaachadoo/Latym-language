# LatimPython
Uma linguagem de programação em latim baseada em python

# Instalando as dependências :

  + Instalar o Lark-parser usando pip: [Lark-Parser](https://github.com/lark-parser/lark)
    + ``` pip3 install lark-parser ```
    
  + Instalar o Click
    + ``` pip3 install click ```
  
  + Instalar o pytest
    + ``` pip3 install pytest ```
    
  + Instalar o flit
    + ``` pip3 install flit ```

# Executando :
  É possível usar essa lingaguem de dois modos, no modo interativo e no modo não-interativo(lendo código de algum arquivo)
  
  ## Modo interativo
  
  + Basta executar o comando ```python3 latym``` na pasta raíz deste repositório
  + Pronto, o terminal mostrará algo assim esperando algum input:
    + ```latym> ```
    
  ## Modo não-interativo
  
  + Execute o mesmo comando do modo interativo porém use o nome do arquivo a ser lido como parâmetro
    + Assim: ```python3 latym script.txt``` como por exemplo
  
  ## Testes
  
  + É possível realizar testes unitários usando o pytest, basta usar o comando ```pytest latym/test_basic.py```

# Exemplos de Código

  ## Hello World
  
```
 inprimo "salve mundi"
```

  ## Verificar se um número é par ou ímpar

```
  numerus aequipar 7

resultado aequipar numerus recide 2

inprimo posthac die "Verificar se o número é par" usque huc

inprimo posthac die "O número é: " . numerus usque huc

si resultado aequalis 0 fac
  sic
    inprimo posthac die "O número é par" usque huc .
  cis

si resultado non aequalis 0 fac
  sic
    inprimo posthac die "O número é impar" usque huc .
  cis
  
```

  ## Contar de 0 até 33 de 3 em 3 números

```

contagem aequipar 0

dum contagem minus quam 33 fac
    sic
        contagem aequipar contagem adde 3 .
        inprimo posthac die contagem usque huc .
    cis
    
 ```


<hr>
<hr>

# Sugestões:
Tais sugestões servem para possíveis implementações futuras
### Pontos importantes:
  
  + Fazer com que não haja simbolos tipo "{", "}", ",", ":", "(", ")" por exemplo, ou seja, todo o código escrito com palavras.
  

## Tipos de dados

Os dados nessa linguagem são definidos dinâmicamente, porém é possível executar TYPECAST, ou seja, converter uma variavel de um tipo para outro

  Variavel | Latim
  ---------|-------
  int      | integer
  float    | decimales
  string   | scriptum
  
#### Atribuir valor à uma variavel

  Simbolo | Latim
  --------|-------
  =       | aequipar
  (       | posthac die
  )       | usque huc

## Entrada e saída de dados

  Função  | Latim
  --------|---------
  input   | inserta 
  print   | inprimo

## Condicionais e Loops de Repetição 

  + "{" e "}" se tornarem "sic" e "cis" respectivamente, usadas para determinar blocos de código
  + "si" para ser o "if" e o "fac" para representar o fim da condição, por exemplo 
 
```
si ...[condição]... fac
  sic
    ...[codigo]...
  cis
```
  + "nisi" para se tornar o "else" seguido de ...[condição]... e "fac"
  
  Estrutura | Latim                 | OBS
  ----------|-----------------------|--------------
  do        | fac                   | 
  { ... }   | sic ... cis           |
  if ()     | si <condição> fac     | 
  else      | nisi fac              | 
  for ```x``` in ```y```| per ```x``` in ```y``` fac | 
  while ()  | dum ... fac           | 
  return    | reditu                |
  break     | intermissum           |
  continue  | confectus             |
  
## Operadores Matematicos

  Latim | Operador
  ---------|-------
  adde | +
  minuas | -
  multiplica | *
  divide | /
  recide | %
  
  
## Operadores Lógicos

  Latim | Operador
  ------|---------
  maior quam | >
  minus quam | <
  atque | &&
  vel | \|\|
  non | !
  aequalis | ==
  
## Alguns literais

  Latim | Literal
  -------|-------
  verum | true
  falsus | false
  nullum | NULL
  etiam | ```,```
  


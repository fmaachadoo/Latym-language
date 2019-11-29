# LatimPython
Uma linguagem de programação em latim baseada em python


# Pontos importantes:
  
  + Fazer com que não haja simbolos tipo "{", "}", ",", ":", "(", ")" por exemplo, ou seja, todo o código escrito com palavras.
  
# Sugestões:

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

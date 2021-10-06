Estrutura de repetições (Repetições, laços ou interações. )
***

<br/>
 
# Repetição Determinadas
Quando a repetição tem uma extensão determinada, não depende de um condição que pode variar a qualquer momento.  

```py
for c in range(3,1,-1):
    print(f'Ação {c}')
```

* range = extensão (Início, Fim antes de, Interação)  

    Resultado:  
    Ação 3  
    Ação 2  

<br/>
 
# Repetição Indeterminadas ou não
Boa para quando o usuário ou algo que não pode ser previsto decide até quando dura a repetição.

```py
c = 1
while c <= 10:
    print(c)
    c += 1
```

<br/>
 
# Repetições úteis para Vetores

```py
for c in lanche:
    print(c)
```
_Resultados:  
pão  
suco  
fruta_

```py
animais = ('cavalo', 'camelo', 'carneiro')
for num, val in enumerate(animais):
    print(f'{num} - {val}')
```
_Resultados:  
0 - cavalo   
1 - camelo  
2 - carneiro_

# Controle de Loop

* `Break;` sai do loop da repetição.	

* `Continue;` ignora o resto código passa para próxima repetição.
Estruturas Seletivas
***
<br/>

A endentação é muito importante para a interpretação do código o que tiver uma tabulação a direita fica sujeito a condição superior.
 
# Condições Simples		

```py
if condição:
    # SE VERDADEIRO
```
 
<br/>
 
# Condições Composta		

```py
if condição:
    # SE VERDADEIRO
else:
    # SE FALSO
```
 
<br/>
 
# Condições Encadeada		

```py
if condição 1:
    # SE 1 VERDADEIRO
elif condição 2:   
    # SE 1 FALSO, MAS 2 VERDADEIRO (break, não testa 'condição 3')
elif condição 3:   
    # SE 1 e 2 FALSO, MAS 3 VERDADEIRO
else:
    # SE TODOS FALSO
```
 
<br/>
 
# Condição Simplificada

```py
print('Verdadeiro!' if condição else 'Falso')
```
 
<br/>
 
# Condições Aninhadas		

`(¿)`
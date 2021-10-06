Interações
***
<br/>
 
# Saídas

```py
print('Olá mundo!')
```
* Aspas duplas também são aceitas.

* f strings (concatenação?)
    ```py
    n1 = 5
    n2 = 2
    print(f'Somando {n1} com {n2} temos: {n1+n2}')
    ```

* Maneira antecessora das f strings:
    ```py
    n1 = 5
    n2 = 2
    print('Somando {} com {} temos: {}'.format(n1, n2, n1 + n2))
    ```

* Trabalhar apresentação de variável     

    * {:20} completar com no mínimo 20 caracteres..  
    * {:>20} completar e alinhar a direita.
    * {:<20} completar e alinhar a esquerda.
    * {:^20} completar e alinhar ao centro.
    * {:=^20} completar com '=' e alinhar ao centro.
    * {:.3f} três casas decimais.
    * `print().format(), end=""` não quebrar linha.
    * `'texto \n outra linha'` quebrar linha.

<br/>

# Entradas

```py
input('Mensagem: ')
```

<br/>

# Importação

```py
import bebidas  #Importar todas as bebidas

bebidas.café
```

```py
from bebidas import café  #Importar apenas café

café
```

# Outras Interações

`(¿)`

<br/>
Manipulações
***
<br/>
 
# Memoria

<br/>

## Variáveis

```py
língua = 'português'
```

## Vetores

```py
# "mostrar" vetores 

meses[-1]       # Dezembro  
meses[0:3]      # Janeiro    Fevereiro     Março

len(lanche)     # Length (Quantidade de elementos em lanche).

sorted(lanche)  # Coloca em ordem.

c = a + b       # A soma de vetores é outra vetor que contem o vetor 'a' seguido do vetor 'b'.

c.count(5)      # Quantos 5 aparece em c.

c.index(5)      # Em que posição aparece o primeiro 5.

pessoa = ('João', 23, Estudante)

del(pessoa)     # Remove da memória o vetor pessoa.
```

### Duplas

Dá para definir, mas não dá para modificar.

```py
lanche = ('pão', 'suco', 'fruta')
```
\* Os parentes são opcionais.


### Listas

```py
animais = ['cão', 'cavalo', 'vaca']     # Caracterizado pelos colchetes.
animais = list('cão', 'cavalo', 'vaca')
pessoas = [['Pedro', 25], ['Ana', 30]]

# Adicionar Elementos
animais.append('galinha')
animais.insert(0, 'cabra')              # Manda todo mundo para frente e ocupa a posição 0.

# Eliminar Elementos (Não fica posição vaga entre posições ocupadas)
del animais[2]
lanche.pop(3)                           # Sem parâmetro remove o último.
lanche.remove('cão')                    # Remove o primeiro cão da lista.
```

### Dicionários

<!--
* Definir um vetor  

`$n = array(2,5,8);`

* Atribuir valor a um elemento do vetor

    - `$n[0] = 7;` - colocar o valor '7' no índice '0'.

    - `$a[] = 4;` - colocar o valor '4' no próximo índice vago.

* Ver um vetor

`print_r($vet);`

* Preencher um vetor em passos

`$c = range(5,20,5);` (de 5 até 20 pulando de 5 em 5.) `$c = array (5, 10, 15, 20)`

### Usar índices determinados

```php
$cadastro = array(
    "nome" => "Ana", 
    "idade => 23
);
```
 
### Percorre um vetor 

Para cada **_elemento_** do **vetor** `$vet` coloque o **índice** em `$ind` e o **valor** em `$val`.

```php
foreach ($vet as $ind => $val) {
    echo "O índice $ind tem o valor $val";
}
```
-->

<br/>

## Tipo de Dados (Tipagem)

* int
* float  
* bool (True, False)
* str
    <br/>  
    Para verificar o tipo de dado: &nbsp; &nbsp; `type(variável)`  
    Representar com duas casas decimais: &nbsp; &nbsp; `print({:.2f}.format(var))`  

<br/>  

### Manipulação de Strings  
<br/>  

```py
frase = 'Uma bela frase em português.'

len(frase)                                      # 28

frase.count('u')                                # 2

frase.find('bela')                              # 4 (começa em [4])

doc = frase[9:13:2]                             # da posição 9 até 20 pulando de dois em dois.

doc = frase[:8]                                 # da posição 0 até 8.

'português' in frase                            # True

doc = frase.replace('português', 'español')     # doc = '[...] em español'

doc = frase.upper() #lower, captalize, title    # doc = 'UMA BElLA [...]'

frase.strip()                                   # remove espaços nos extremos.

frase.split()                                   # joga cada palavra em uma posição

'-'.join(frase)                                 # junta posições em uma frase separando as por -.

```



<br/>

***
# Operadores

## Atribuição

#### `=`

## Concatenação

#### `,`
#### `+` ( somente para strings )  

<br>

* Auto concatenação  
`(¿)`

## Aritméticos

som. | sub.
-- | --
 `+` | `-`  

mult. | div. | resto da div. | div. int.
-- | -- | -- | --
` *` | ` /` | ` %` | ` //` 

potência | ~
-- | --
`**` | ~

* Auto atribuição      ``s += n`` 

* Operador de Incremento        `(¿)`

* Operador de Decremento        `(¿)`

<!--
## Relacionais

`>` `<` `>=` `<=` `==` ( `!=` ou `<>` )     

* Inversor `$a =! $b`  

* Idêntico `$a === $b`

## Lógicos

`!` (Negação) `&&` (Conjunção) `||` (Disjunção)  

(Esta é a ordem de execução (precedência)).
-->
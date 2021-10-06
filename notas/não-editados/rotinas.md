Rotinas
***
<br/>
 
# Funções

```php
function fun ($par_1, $par_2) {
    $adic = $par_1 + $par_2;
    return $adic;
}

$soma = fun (2, 4);
```

# Funções com Parâmetros Dinâmicos

Função que não determina a quantidade de parâmetros.

```php
function mehdia(){
      $p = func_get_args();   # retorna um vetor com todos os parâmetros passados para a função 'mehdia'.
      $f = func_num_args();   # retorna a quantidade de parâmetros repassados.

      $s = 0;

      foreach ($p as $val) {
            $s += $val;
      }

      $mehdia = $s / $f;

      return $mehdia;
}

$med = mehdia(22, 4, 8, ... ,5);
```

# Passagem de Parâmetro por Referência

Entregar uma variável por inteiro não só um valor.
```php
function soma (&$parahhmetro) {        # '&' marca que se trata de passagem de referência e não de valo.
    $parahhmetro += 2;                # Irar trabalhar com $num
    echo "$parahhmetro";             # >>>>     5      <<<<
}

$num = 3;
fun ($num);
echo "$num";             # >>>>     5      <<<<
```

# Alguns métodos úteis

* `isset()` - para verificar se chegou algum valor do formulário.
```php
$ano = isset($_GET["ano"])?$_GET["ano"]:"0";
```

* `date("Y")` - para pegar o ano atual.

## Alguns métodos úteis em matemática

`pow($v, $w)` potencia ( $v<sup> $w</sup> )

`abs($v)` valor absoluto   

`sqrt($v)` raiz quadrada   

`intVal($v)` valor inteiro   

`round($v)` arredondamento. Também: _ceil ( ) floor ( )_  

`number_format($v1, 2, ",", ".")` separação de milhar por . e duas cas decimais por ,
Orientação a Objeto
***
<br/>
 
# > > > > > > &nbsp; &nbsp; Básico &nbsp; &nbsp; < < < < < <

# Classe

```php
class Caneta {
        // Atributos
        var $cor;  		 
        var $tampada, $ponta, $marca;

        // Construtor

        // Métodos Especiais
        function tampar() {     	                
                $this->tampada = true;        
        }

        // Métodos Sobrescritos
        // Métodos abstratos Implementados
        // Métodos abstratos Herdados
        // Getters
        // Setters
}
```

* `$this -> 'atributo/atributo'`   -  this faz referência ao objeto estanciado. Pode haver espaço antes e depois de ` -> `

# Objeto

```php
$c1 = new Caneta;                // instanciar

$c1->tampada = false;	        // modificar atributo

$c1->tampar();                 // chamar método
```

`var_dump()` - server para descrever os atributos de um objeto, colocar o nome do objeto como parâmetro.

# Método Construtor

Método especial de uma classe. Quando instanciado um objeto dessa classe é acionado o método construtor
```php
public function __construct($cor){                // Dois subtraços 
        $this->ponta = 0.5;                    // -> vai ter/fazer
        $this->cor = $cor;                   
}
```
Os presença de parâmetros é opcional, mas se hover será obrigado a passar quando for instanciado.

```php
// Se não hover construtor ou se ele não tiver parâmetros.
$d[0] = new Aluno;
$d[1] = new Aluno();  

// Se hover construtor com parâmetros, se sobrar não dá erro apenas se faltar.
$e[0] = new Aluno("Pedro", 20);              
```

É possível usar o construtor da classe herdada.

```php
class Aluno extends Pessoa {
        function __construct($nome, $idade, $matricula) {
                parent::__construct($nome, $idade); //chama o método construtor de Pessoa para ajuda a construir um aluno.
                $this->matricula = $contator++;
        }
}
```

# Atributo do tipo Objeto

Usar objetos de uma classe A como atributos de uma classe B. Com isso posso alterar/chamar seus atributos e métodos dentro de outra classe.

```php
// Inscrever os lutadores:
        $lutador1= new Lutador("Cabano");
        $lutador2 = new Lutador("Julio");
 
// Declarar um combate:
        $lutaA = new Luta($lutador1, $lutador2);
```

Se um objeto for atributo posso inclusive usar seu métodos, embora sejam de outra classe. Deve se importar o arquivo onde está a outra classe.

```php
class Livro {
        public quemTahLendo() {
                $this -> leitor -> getNome();   
                // getNome() não pertence a essa classe, mas sim a classe da qual leitor foi instanciado.
        }
}
```

<br/><br/> 

# > > > > > > &nbsp; &nbsp; Encapsulamento &nbsp; &nbsp; < < < < < <

# Visibilidade

Para restringir o acesso de atributos ou métodos:

* `public`  - objetos e classes filhas.

* `private`  - nem objeto, nem classe filhas.

* `protected` - apenas classe filhas.

```php
class Cavalo {
        public $corPelo;                // o 'var' some.
        private $tamanho, $raça;
}
```

# Métodos Getters e Setters

Quando a certo atributo não pode ser modificado de qualquer forma e ou a qualquer momento faz se necessário torna-lo privado e permitir o seu acesso apenas por métodos públicos (Getters e Setters) que terão o controle se tal atributo pode ser alterado e como ou se pode ser repassado e como. É de bom tom criar todos os métodos Getter e Setter para todos os atributos.

* `Getter` - quem irar passar o valor de algum atributo.

* `Setter` - quem irar modificar o valor de algum atributo.

# Interface

Se implemento uma interface fico obrigado a desenvolver todos seus métodos.
```php
interface Controlador{                                  // Interface.
        public function ligar();  //Posso também determinar a existência de parâmetros.                        
}
 
class ControleRemoto implements Controlador{            // Classe que implementa a Interface.
        var $ligado;

        // IMPLEMENTAÇÃO DO MÉTODO
        public function ligar(){
                $this->$ligado = true;
        }
}
```

<br/><br/>

# > > > > > > &nbsp; &nbsp; Herança &nbsp; &nbsp; < < < < < <

```php
class Aluno extends Pessoas {
        // Aluno tem todos (talvez nem todos) os tributos e métodos de Pessoas.
}
```

## Tipos de Herança

* `abstract class Pessoa {` - não pode ser instanciada só pode ser mãe.

* `final class Bolsista {` - não pode ser herdada.

* `final function minhaEscola() {` - não pode ser sobrescrito.

* `abstract function oQueSou();` - é declarado na classe mãe, mas seu conteúdo só é definido nas classe filhas.  
(Só pode ser colocado dentro de uma interface ou de uma classe abstrata, quando uma classe implementa ou herda outra classe com métodos abstratos se obriga a desenvolver-los).

```php
class Visitante extends Pessoa { }
/* 
 * Se Pessoa for uma classe abstract e for necessário instanciar um objeto só com suas características 
 * pode se criar uma classe vazia que herde a classe abstract, mas que permita que objeto seja estanciados. 
 *
 */
```

<br/><br/>

# > > > > > > &nbsp; &nbsp; Polimorfismo &nbsp; &nbsp; < < < < < <

\* _**Assinatura**: parâmetro (tipos e quantidades)_


## Sobreposição

Rescrever um método herdado mantendo seu nome e assinatura, porém alterando sua funcionalidade.

No PHP não uma palavra como _`@sobrescrito`_ para identificar uma sobreposição.

```php
class Ave {
        function locomover($velocidade) {
                if ($velocidade == 'rahpido') { echo"voa"; }
                if ($velocidade == 'lento') { echo"caminha"; }
        }
}

class Galinha {
        function locomover($velocidade) {
                echo "Só caminha :(";
        }
}
```

## Sobrecarga

O PHP não suporta sobrecarga de métodos.
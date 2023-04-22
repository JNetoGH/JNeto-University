# PYTHON RPG IN CLI(Command Line Interface)
https://github.com/JNetoGH/JNeto_Productions_Python_Terminal_RPG

Joao Neto (a22200558):
- arquitetura do software
- desenvolvimento das classes de core combat

Daniela (a22202104):
- desenvolvimento de utilities para UI
- assistência no desenvolvimento das classes de core combat


## GAME PREVIEW
![image](https://user-images.githubusercontent.com/24737993/201548631-dc99607f-f3a6-4b37-8956-24b184e1130a.png)



## ARQUITETURA
Estamos disponibilizando junto ao source um diagrama que mostra a arquitetura do sistema como um todo.
Este diagrama também pode ser acessado, por este link: 
https://drive.google.com/drive/folders/11IZPW_Waw7i5_KGCOitn4BVyMqHW58dN?usp=sharing

### Core Combat System
O sistema de Batalha é composto de uma classe **Battle** necessita de dois objetos **Squad**, sendo cada **Squad ** uma lista de **Charater**, que carrega um atributo do tipo **Ownership**, este sendo um Enum com dois valores possíveis, Player e Enemy.

Ao ser instanciada, uma **Squad** set seus **Character** para terem a sua **Ownership**, **Characeter** tamém possui um atributo do tipo **Ownership**. 

Um loop é feito que se quebra quando uma **Battle** encontra um campeão, dado pela **Ownership** do **Squad** vencedor.
Enquanto não houver um campeão, um novo objeto de **Round** é instanciado, sendo este composto por uma **InitiaviePhase** e uma **ActionPhase.**

**InitiativePhase**: serve exclusivamente para gerar uma lista com orderm de ação, utilizando o d20 + initiativa do **Character**

**ActionPhase**: recebe a lista de ordem de ação da **initiativePhase** e executa a ação sendo player based ou AI based, a depender da **Ownership** do **Character** (Player/Enemy), a ação executada é um objeto do tipo **Ability**

**Ability**: está é a super classe de todas as habilidades do game, sando mãe de **PhysicalDmg** e **Spell**, que são mães das habilidades de fato usadas no game. **Ability** possui um método exec(caster, target) que é sobrescrito por todas as suas subclasses, garantindo assim, um funcionamento genérico para a execução de objeto filhos de **Ability**


### UI System
O sistema de UI do game é majoritariamente isolodo dos elementos que compõe o sistema de combate, ela foi arquitetada dessa forma com o intuito de gerar flexibilidade para futuras implementações.

Este sistema possui algumas funcionalidades interessantes, como por exemplo, criar um card de **Character** ou uma linha de cards de uma **Squad**, as fases de um **Round** tem sua renderização fortemente tercerizada para o UI System

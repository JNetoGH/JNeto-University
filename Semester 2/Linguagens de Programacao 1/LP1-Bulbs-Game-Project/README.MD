# Bulbs Game
Este é um puzzle onde se deve ligar todas as lâmpadas em um número limitado de rounds.

link GitHub: https://github.com/JNetoGH/LP1-Bulbs-Game-Project

## ALUNOS
João Neto (a22200558):
- arquitetura do game.
- desenvolvimento do controle de fluxo do game.
- desenvolvimento geral dos Game Objects.

João Silva (a22004451):
- assistência no desenvolvimento das mecânicas.
- documentção do projeto.
- assistência no planejamento de projeto.

## ARQUITETURA
A arquitetura da solução é relativamente simples. 
Há implementado uma classe para as lâmpadas(Bulb), botão simples(SimpleButton) e botão switcher(SwitchButton).

As lâmpadas possuem uma Read-Only property chamada State, esta guarda um valor do enum BulbState, o qual define os valores On e Off.
A classe Bulb, possui nela implementado o método SwitchState(), para mudar o estado atual desta lâmpada (On => Off e Off => On).

Os botões por sua vez implementam a interface IBulbButton, a qual define um método void Press(), este é o método chamado no game loop para a ativação deste botão.
O SimpleButton recebe em seu construtor apenas uma lâmpada, na call de Press() apenas chama o SwitchState() da lâmpada manejada por ele.
O SwitchButton por sua vez, recebe em seu construtor duas lâmpadas, as quais se tiverem estados diferente serão trocados na call de Press().

O gameloop do jogo foi implementado na classe Program, não há nada de especial, apenas faz 6 rondas, tendo uma validação de input interna com tratamento de exceções e ao final, checa se todas as bulbs estão On ou não, para dar a mensagem de vitória ao player.

## FLOWCHART
![BulbsFlowchart](https://user-images.githubusercontent.com/24737993/232344174-0f36f7eb-de92-45d9-a9ac-82ef3565c7be.png)



# Cannon-Ball
It's a game where you can shoot a cannon ball in order to sink ships

link: https://github.com/JNetoGH/Cannon-Ball

## ALUNOS
João Neto (a22200558):
- desenvolvimento da game engine
- arquitetura do game
- desenvolvimento do controle de fluxo do game
- desenvolvimento geral dos GameObjects

Margarida Teles (a22204247):
- desenvolvimento das artes para UI e Sprites
- assistência no desenvolvimento de mecânicas
- assistência no desenvolvimento de prefabs
- assistência nas layers
- assistência na criação do mapa

<br>
<br>
<br>

## GAME-ENGINE (quick overview)

#### ENGINE VS JOGO EM MINHA ARQUITETURA
O jogo está separado em pastas, há pastas exclusivas da JNeto Productions Game Engine, esta é uma ferramenta discreta, o jogo em si, é composto por GameObjects, os quais não ficam localizados juntamente da engine, porém, acessam seus recursos, tais quais, Systems, GameLoop, Components, Scenes, Prefabs, RenderingLayers e Cameras.

Com isso em mente, eu considero tudo aquilo que não está na pasta da engine, como sendo de fato a lógica do game.

#### RUNNING THE GAME
Para rodar o game é simples, basta executar o comando para o script main.py ou equivalente em outros sistemas operacionais:
```
python main.py
```
desde que o main.py esteja na maior hierarquia dos scripts, o jogo deve rodar sem maiores problemas, `pygame` package é necessário.

<br>
<br>
<br>

## START SCREEN
![image](https://user-images.githubusercontent.com/24737993/212774785-4d5825f0-fc00-44ca-a018-17372dfb799b.png)

<br>
<br>
<br>

## CÂMERA
A câmera da scene principal pode ser movida no eixo horizontal usando as arrows `←`/`→` ou as teclas `A`/`D`

![camera](https://user-images.githubusercontent.com/24737993/212778067-cb04a8bf-ca78-4c84-b707-e6d974bdd9cf.gif)

<br>
<br>
<br>

## CANNON
* O canhão pode ter seu ângulo mudado com as arrows `↑`/`↓` os as teclas `W`/`S`. <br>
* A rotação do sprite é feita usando os sistemas internos da Jneto Game Engine

![cannon](https://user-images.githubusercontent.com/24737993/212778318-b1549403-89df-43e1-a1da-9656b09c2705.gif)

<br>
<br>
<br>

## SHOOTING CANNON BALLS
- um disparo é gerado ao pressionar `SPACE`, tendo este a mesma direção em que o player estava rotacionado.
- os disparos possuem uma cadência com 1 segundo de intervalo (obrigatório pelo professor).
- há um texto em cima do canhão que indica o tempo do intervalo, quando zerado, pode-se disparar novamente.
- cada disparo é removido da cena após colidir, com a água ou com um barco
- deixa partículas de impacto com a água ou de explosão com os barcos

<br>
<br>
<br>

## THRUST, GRAVITY, AIR DRAG ON CANNON BALLS
Basicamente, aplicamos um sistema de velocity com aplicação de forças nas bolas do canhão:

```
  # DIR
  self.cannon_angle = cannon_angle
  self.cannon_angle_rad = math.radians(self.cannon_angle)
  self.direction = pygame.Vector2(math.cos(self.cannon_angle_rad), - math.sin(self.cannon_angle_rad))
  self.direction = self.direction.normalize() if self.direction.magnitude() > 0 else self.direction

  # INITIAL POSITION
  self.initial_position = initial_pos  # comes from the constructor, it is the same as the cannon

  # PHYSICS
  self.THRUST = 480
  self.velocity = pygame.Vector2(self.THRUST, self.THRUST)
  self.GROUND_Y_POS = 380
  self.GRAVITY = 480
  self.AIR_DRAG = 48

  def move(self):
      new_pos = self.transform.world_position_read_only
      new_pos.x += self.velocity.x * self.direction.x * GameTime.DeltaTime
      new_pos.y += self.velocity.y * self.direction.y * GameTime.DeltaTime
      self.transform.move_world_position(new_pos)

  def apply_gravity(self):
      self.velocity.y -= 0.5 * self.GRAVITY * GameTime.DeltaTime * 2
      # stop applying when the CannonBall reaches the ground
      self.velocity.y = 0 if self.has_reached_the_ground else self.velocity.y

  def apply_air_drag(self):
      self.velocity.x -= self.AIR_DRAG * GameTime.DeltaTime
      # stop applying when the CannonBall reaches the ground or has been already stop by the air drag
      self.velocity.x = 0 if self.velocity.x < 0 or self.has_reached_the_ground else self.velocity.x
```


<br>
<br>
<br>

## Barcos
- Os Boats são manejados por um GameObject chamado BoatsManager.
- Quando o RectTriggerComponent colide com a Fortress ou uma CannonBall, este Barco é manejado para garbage collection. 
- Cada barco destruído dá uma pontuação diferente:
    - HUGE   -> 1 ponto
    - LARGE  -> 2 pontos
    - MEDIUM -> 3 pontos
    - SMALL  -> 4 pontos
    - TINY   -> 5 pontos
- A cada 10 barcos destruídos o Multiplier dos pontos é incrementado em 1
- A cada segundo o player ganha 1 ponto


<br>
<br>
<br>

## GAME OVER SCENE & SCORE SCENE
Quando o jogador é morto, a scene atual é setada para a game_over_scene, esta por sua vez, conta alguns segundo para setar a cena atual como sendo a score_scene.

Uma vez na score_scene, a scene é capaz de entender em que contexto foi setada, e ao perceber que um GameOver a setou como a current_scene no GameLoop, verifica os pontos marcados do player, e caso ele se qualifique, um ScoreRegistrationFloatingMenu é mostrado na scene, onde o player por ele, poderá ter sua pontuação registrada na score sheet juntamente com um nome de até 3 characteres.

#### DETALHES DE IMPLEMENTAÇÃO
* são mostrados apenas os 4 primeiros elementos do arquivo CSV que guarda os nomes e os scores.
* este CSV é sorted toda vez que a score_scene é setada como a current_scene.
* toda a manipulação do CVS é feita com um sistema na engine chamado FileManager.

#### VALIDAÇÃO DE REGISTRO:
* pontuação maior que 0.
* pontuação maior que o 4º elemento ou último elemento caso o CSV possua menos de 4 elementos.
* o nome inserido obrigatoriamente deve possuir 3 caracteres.

<br>
<br>
<br>

## SOUNDS
O game possui som para todos os lados, eu utilizei uma coleção de efeitos sonoros, um asset pessoal que comprei na Unity Asset Store, não havendo assim nenhum problema legal de copyright.

#### SONS USADOS
![image](https://user-images.githubusercontent.com/24737993/212777855-a07df5f3-91d6-44f4-bc49-9c4dbaee3bd7.png)

#### ASSET 
https://assetstore.unity.com/packages/audio/music/orchestral/total-music-collection-89126

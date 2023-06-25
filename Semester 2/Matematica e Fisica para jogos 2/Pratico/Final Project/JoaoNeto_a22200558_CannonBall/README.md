# CANNON BALL
João Mendes de Almeida Neto (a22200558)
___






## HOW TO RUN
Para rodar o game é simples, basta executar o comando para o script main.py ou equivalente em outros sistemas operacionais:
```
python main.py
```
Desde que o main.py esteja na maior hierarquia dos scripts, o jogo deve rodar sem maiores problemas, `pygame` package é necessário.
___





##  OVERVIEW
Eu decidi não utilizar a nova engine, mas sim, desenvolver o jogo em cima da engine feita há algum tempo para o projeto
de IMFJ1, pois, a nova engine com um motor de física integrado, seria muito complicada de corrigir, já que apenas o 
componente do Rigidbody possuía 400 linhas, logo, decidi por usar esta mais antiga, 
a qual não possui motor de física integrado e programar a física diretamente nos objetos.

O Jogo em questão "Cannon Ball", é um projeto de minha autoria, o qual nunca tive a oportunidade de finalizar,
e que ao mostrar ao professor, o mesmo me deu a ideia de que eu o terminasse para o projeto final de IMFJ2, porém,
fazendo a implementação com algoritmos de física, e foi o que fiz. 

### Engine vs Jogo, Agilizando a Avaliação
O jogo está separado em pastas, há pastas exclusivas da JNeto Productions Game Engine, esta é uma ferramenta discreta.
O jogo em si, é composto por GameObjects, os quais ficam localizados fora da engine, porém, acessam seus recursos, 
tais quais, Systems, GameLoop, Components, Scenes, Prefabs, RenderingLayers e Cameras.

Assim, para facilitar a avaliação, eu organizei as pastas dos GameObjects em regular_game_objects e physics_game_objects, 
onde apenas na segunda há as minhas implementações de física, que eu condensei em 3 objetos, a cannon ball, os barcos e o golfinho, 
mas já adianto que as implementações serão explicadas neste README.

![image](https://github.com/JNetoGH/Test/assets/24737993/39f67489-3ca1-4a17-b10f-01dbfe564117)
___






## HOW TO PLAY

### Camera
A câmera da scene principal pode ser movida no eixo horizontal usando as arrows `←`/`→` ou as teclas `A`/`D`

### Boats
- Cada barco destruído dá uma pontuação diferente a depender de seu rank
    - HUGE   -> 1 ponto
    - LARGE  -> 2 pontos
    - MEDIUM -> 3 pontos
    - SMALL  -> 4 pontos
    - TINY   -> 5 pontos
- A cada 10 barcos destruídos o Multiplier dos pontos é incrementado em 1
- A cada segundo o player ganha 1 ponto
- O tipo de barco spawnado é aleatório

### Shooting Cannon Balls
- um disparo é gerado ao pressionar `SPACE`, tendo este a mesma direção em que o player estava rotacionado.
- os disparos possuem uma cadência com 1 segundo de intervalo.
- há um texto em cima do canhão que indica o tempo do intervalo, quando zerado, pode-se disparar novamente.
- cada disparo é removido da cena após colidir, com a água ou com um barco
- deixam partículas de impacto com a água ou de explosão com os barcos

### Cannon
* O canhão pode ter seu ângulo mudado com as arrows `↑`/`↓` os as teclas `W`/`S`. <br>
* A rotação do sprite é feita usando os sistemas internos da Jneto Game Engine <br>
![cannon](https://user-images.githubusercontent.com/24737993/212778318-b1549403-89df-43e1-a1da-9656b09c2705.gif)


### Gizmos
Os gizmos podem ser ligados pressionandon `C` e desligados pressionando `V`. <br>
Permitem que o usuário veja os colisores em verde, relative up arrow em azul, e os retângulios de sprite em vermelho. <br>
![image](https://github.com/JNetoGH/Test/assets/24737993/6110e6db-722f-438d-b5af-44bd582bb1ed)
___






## METHODOLOGY (technical implementations)
Eu procurei o máximo possível usar os conceitos passados em aula, a temática do jogo foi refinada com os insights do
professor, que me ajudaram a encontrar um formato de jogo que justificasse a implementação de conceitos em quantidade.

Gostaria de salientar, que eu tentei ao máximo deixar as fórmulas o mais parecido com os slides.

<br>

### Projectiles and Gravity
Como primeiro exemplo, essa implementação está na cannon ball. <br>
Esta simulação de projéteis e aplicação da força da gravidade foi retirada diretamente dos slides. <br>
localizada em: physics_game_objects/cannon_ball.py <br>
```
    # ESTE FICA NO CONSTRUTOR
    # MOVE DIRECTION: cos and sin of the angle
    self.direction = pygame.Vector2(math.cos(self.cannon_angle_rad), - math.sin(self.cannon_angle_rad))
    self.direction = self.direction.normalize() if self.direction.magnitude() > 0 else self.direction
        
    def apply_gravity(self):
        # formula that was literally took from the slides
        self.velocity.y -= 0.5 * self.GRAVITY * GameTime.DeltaTime
        # stop applying when the CannonBall reaches the ground
        self.velocity.y = 0 if self.has_reached_the_ground else self.velocity.y

    def move(self):
        # updates the cannon ball position
        new_pos = self.transform.world_position_read_only
        new_pos.x += self.velocity.x * self.direction.x * GameTime.DeltaTime
        new_pos.y += self.velocity.y * self.direction.y * GameTime.DeltaTime
        self.transform.move_world_position(new_pos)

```

Slide Original: <br>
![image](https://github.com/JNetoGH/Test/assets/24737993/3e70b9ac-ed71-4004-ab2a-4c0c2317a6c5)

<br>

### Air Friction / Drag
Para representar a fricção, eu escolhi por colocar drag na Cannon Ball, localizada em: physics_game_objects/cannon_ball.py <br>
Novamente, busquei por literalmente o que havia nos slides, para que ficasse o mais parecido o possível .<br>
```
    def apply_air_drag(self):
        # applies air drag using the formulas from the math classes
        surface_area = self.radius / 4
        velocity_squared = self.velocity.x ** 2
        drag_force = 0.5 * self.DRAG_COEFFICIENT * self.air_density * velocity_squared * surface_area
        acceleration = - drag_force / self.mass                # Calculate the acceleration based on drag force
        self.velocity.x += acceleration * GameTime.DeltaTime   # Update ball velocity and position
```
Slide Original: <br>
![image](https://github.com/JNetoGH/Test/assets/24737993/d9b33962-ac0a-4971-96f5-d04d18b97ad5)

<br>

### Buoyancy (Flutuabilidade)
Escolhi por golfinhos no jogo para implementar a flutuabilidade. <br>
Eles descem normalmente, mas fazem o movimento de emersão  usando fórmulas físicas para flutuabilidade. <br>
E mais uma vez, busquei por literalmente o que havia nos slides, para que ficasse o mais parecido o possível. <br>
localizado em: physics_game_objects/dolphin.py <br>
```
    def float(self):
        # Calculate the submerged depth
        submerged_depth = ((self.pos_y + self.dolphin_height) - Dolphin.WaterLevel)
        # total_volume=0. # m^3 (dimensions: 1m x 0.4m x 0.1m)
        submerged_volume = 0.4 * submerged_depth / self.dolphin_height
        # Calculate the buoyant force
        buoyant_force = Dolphin.WaterDensity * Dolphin.Gravity * submerged_volume
        # Calculate the net force
        net_force = self.dolphin_mass * Dolphin.Gravity - buoyant_force
        # Apply the net force to the rectangle's position
        acceleration = net_force / self.dolphin_mass
        self.pos_y += acceleration * GameTime.DeltaTime
```
Slide Original: <br>
![image](https://github.com/JNetoGH/Test/assets/24737993/c1fc420e-5e94-4632-b132-5edaa404441b)

<br>

### Applying Forces
Utilizo da fórmula de aplicação de força para mover os Barcos, altero as massas dos barcos em cada rank para 
tenham velocidades diferentes. <br>
localizado em: physics_game_objects/boat_and_boat_manager.py <br>
```
    def move_boat_with_wind_force(self):
        # resets velocity to get the new force form the wind
        self.velocity = pygame.Vector2(0, 0)
        wind_direction = pygame.Vector2(-1, 0)
        self.apply_force(wind_direction, Boat.WindForce * GameTime.DeltaTime)
        new_pos = self.transform.world_position_read_only + self.velocity
        self.transform.move_world_position(new_pos)

    def apply_force(self, force_direction: pygame.Vector2, force_units) -> None:
        # Applies a force to the velocity: (F = m * a) => a = (F / m) * direction
        acceleration = (force_units / self.mass) * force_direction
        self.velocity += acceleration

```

Fórrmula usada:<br>
![image](https://github.com/JNetoGH/Test/assets/24737993/402b8a19-922f-479d-94dc-054c85072a58)

<br>

### Collisions
As collisions são manejadas pela engine usando um algoritmo de Discrete Collision, uma técnica de detecção de colisões
mais avançada, usada nas engine profissionais, que usa projeções  na tentativa de encontrar por intersecções entre 
formas geométricas. <br>
Os colisores podem ser vistos ao ligar o gizmos, como já mencionado anteriormente na secção "How to PLay".
  
  - Quando o RectTriggerComponent colide com a Fortress ou uma CannonBall, este Barco é manejado para garbage collection. 

  - Discrete Collision Model (há outros mais preciso, mas para o projeto, este está de bom tamanho) <br>
  ![image](https://github.com/JNetoGH/Test/assets/24737993/45b3a68b-ac07-411a-9b51-fa7e18bbb093)

Os exemplos de implementação ficam dentro da engine em: <br>
- **Discrete Collision:** engine_JNeto_Productions/components/transform_component.py (no method move_world_position_with_collisions_calculations)
- **Cálculo de Intersecção:** engine_JNeto_Productions / components/circle_trigger_component.py <br>

<br>

### Engine Base Architecture Flowchart
Esta é uma representação da estrutura base da engine, claro que ela possui muitos outros sistemas e componente, mas a estrutura base é essa. <br>
Essa arquitetura foi inspirada na "Unity Game Engine", a qual, deixarei nas referências um link que leva até o diagrama da mesma. <br>
![flowchart](https://github.com/JNetoGH/Test/assets/24737993/9029209b-2ccf-41cd-97ad-164ea72b4791)
___






## References

**Unity Game Engine Architecture** (Mar 18, 2019 by Unity Technologies): <br>
https://docs.unity3d.com/Manual/ExecutionOrder.html

**Collision detection modes in Unity’s Rigidbody component** (May 17, 2022 by Terence Dev): <br>
https://blog.terresquall.com/2019/12/collision-detection-modes-in-unitys-rigidbody-component/#:~:text=For%20dynamic%20objects%20(i.e.%20objects,collide%20with%20fast-moving%20objects.

**Introduction to Physics in Unity** (Apr 4, 2021, by Kyle W. Powers): <br>
https://levelup.gitconnected.com/introduction-to-physics-in-unity-1113ff12397b

**Creating a Stardew Valley inspired game in Python** (Aug 10, 2022, by Clear Code): <br>
https://www.youtube.com/watch?v=T4IX36sP_0c

<br>
<br>
<br>

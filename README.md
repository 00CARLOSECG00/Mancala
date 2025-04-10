# Mancala - Juego de Consola en Python

## Autores

- Juan Andrés Rodríguez Rubio  
- Carlos Enrique Caicedo Guerrero  
- Alejandro Caicedo Caicedo  

---

# Juego Mancala por Consola

Este proyecto es una implementación del clásico juego de **Mancala** utilizando Python y una **interfaz por consola**.

## ¿Cómo se juega Mancala?

- Dos jugadores se enfrentan.
- Cada jugador tiene 6 pozos frente a él con 4 piedras cada uno.
- A la derecha de cada jugador hay una "Mancala", donde acumula piedras capturadas.
- En su turno, un jugador elige uno de sus pozos y reparte las piedras una por una hacia la derecha.
- Se **salta** la Mancala del oponente al repartir.
- Si la última piedra cae en su propia Mancala, el jugador gana otro turno.
- Si la última piedra cae en un pozo vacío del propio lado, y el pozo opuesto tiene piedras, el jugador **captura ambas**.

El juego termina cuando uno de los jugadores ya no tiene más piedras en sus pozos. El jugador con más piedras en su Mancala gana.

---

## Interfaz de consola explicada

Cada turno se verá algo así en la consola:

![image](https://github.com/user-attachments/assets/9b8ba6a4-2389-4784-a4d7-4459a5d792c8)


### Significado:

- `Jugador 2 (Mancala: 0)`: cantidad de piedras acumuladas por el jugador 2.
- `Pozo jugador 2`: estado actual de los pozos 12 al 7 (en ese orden).
- `Pozo jugador 1`: estado actual de los pozos 0 al 5.
- `Jugador 1 (Mancala: 0)`: piedras en la Mancala del jugador 1.
- `Turno del Jugador`: indica quién juega actualmente.
- `Jugador 1, elige un pozo (0-5)`: se solicita que el jugador introduzca un número de pozo válido.

---

## Posibles errores

-  Si eliges un número fuera del rango permitido (0-5 para jugador 1, 7-12 para jugador 2).
-  Si eliges un pozo que no contiene piedras.
- En ambos casos, el sistema imprime:

![image](https://github.com/user-attachments/assets/26435898-8c26-4bde-92a6-5222190d9c4b)


## Estructura del Código

El juego se organiza en una clase `Mancala`, con los siguientes métodos principales:

### `__init__`
Inicializa el tablero con:
- 6 pozos para cada jugador con 4 piedras cada uno.
- 1 Mancala para cada jugador con 0 piedras.
- El jugador 1 inicia el juego.

### `print_board()`
Muestra el estado actual del tablero en consola, incluyendo:
- Cantidad de piedras en los pozos.
- Mancalas de cada jugador.
- Turno actual.

### `make_move(pit)`
Realiza el movimiento de un jugador:
- Verifica que el pozo seleccionado sea válido.
- Distribuye las piedras.
- Aplica reglas especiales (turno extra, captura).
- Cambia el turno si es necesario.

### `check_game_over()`
Verifica si el juego terminó (cuando un jugador no tiene más piedras). Si finaliza:
- Se suman las piedras restantes a la Mancala del otro jugador.
- Se vacían todos los pozos.

### `get_winner()`
Retorna el nombre del jugador ganador o "Empate" en caso de igualdad.

---

## Variables Clave

- `board`: Lista de 14 posiciones:
  - `0-5`: Pozos del jugador 1
  - `6`: Mancala del jugador 1
  - `7-12`: Pozos del jugador 2
  - `13`: Mancala del jugador 2

- `player_turn`: Indica qué jugador tiene el turno (1 o 2)

---

## Ejecución
-Para correr el juego, asegúrate de tener Python 3 y ejecuta:

![image](https://github.com/user-attachments/assets/6a5cc811-e450-407b-9dce-1cfbc7ca5cf8)

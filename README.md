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

## Ejecución
-Para correr el juego, asegúrate de tener Python 3 y ejecuta:

![image](https://github.com/user-attachments/assets/6a5cc811-e450-407b-9dce-1cfbc7ca5cf8)



# Global game state representation (Standard Setup).
# 1 is black, 2 is white, -9 is the non-use position.
# WARNING: This convention should be strictly followed.
global_game_state = [
    [-9, -9, -9, -9,  0,  0,  0,  1,  1],
    [-9, -9, -9,  0,  0,  0,  0,  1,  1],
    [-9, -9,  0,  0,  0,  0,  1,  1,  1],
    [-9,  2,  0,  0,  0,  0,  1,  1,  1],
    [ 2,  2,  2,  0,  0,  0,  1,  1,  1],
    [ 2,  2,  2,  0,  0,  0,  0,  1, -9],
    [ 2,  2,  2,  0,  0,  0,  0, -9, -9],
    [ 2,  2,  0,  0,  0,  0, -9, -9, -9],
    [ 2,  2,  0,  0,  0, -9, -9, -9, -9]
]










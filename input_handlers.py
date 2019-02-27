from game_states import GameStates


def handle_keys(user_input, game_state):
    if user_input:
        if game_state == GameStates.PLAYERS_TURN:
            return handle_player_turn_keys(user_input)
        elif game_state == GameStates.PLAYER_DEAD:
            return handle_player_dead_keys(user_input)
        elif game_state == GameStates.TARGETING:
            return handle_targeting_keys(user_input)
        elif game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
            return handle_inventory_keys(user_input)
        elif game_state == GameStates.LEVEL_UP:
            return handle_level_up_menu(user_input)
        elif game_state == GameStates.CHARACTER_SCREEN:
            return handle_character_screen(user_input)

    return {}


def handle_player_turn_keys(user_input):
    key_char = user_input.char

    input_map = {
        'KP8':{'move': (0, -1)},
        'KP2':{'move': (0, 1)},
        'KP4':{'move': (-1, 0)},
        'KP6':{'move': (1, 0)},
        'KP7':{'move': (-1, -1)},
        'KP3':{'move': (1, 1)},
        'KP9':{'move': (1, -1)},
        'KP1':{'move': (-1, 1)},
        'ESCAPE':{'exit': True}
    }

    char_map = {
        'g':{'pickup': True},
        'i':{'show_inventory': True},
        'd':{'drop_inventory': True},
        'c':{'show_character_screen': True},
        'z':{'wait': True}
    }

    if key_char in char_map:
        return char_map[key_char]

    if user_input.key in input_map:
        return input_map[user_input.key]
  
    if user_input.key == 'ENTER' and user_input.alt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}

    elif key_char == '.' and user_input.shift:
        return {'take_stairs': True}
    # No key was pressed

    return {}


def handle_targeting_keys(user_input):
    if user_input.key == 'ESCAPE':
        return {'exit': True}

    return {}


def handle_player_dead_keys(user_input):
    key_char = user_input.char

    if key_char == 'i':
        return {'show_inventory': True}

    if user_input.key == 'ENTER' and user_input.alt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif user_input.key == 'ESCAPE':
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}


def handle_inventory_keys(user_input):
    if not user_input.char:
        return {}

    index = ord(user_input.char) - ord('a')

    if index >= 0:
        return {'inventory_index': index}

    if user_input.key == 'ENTER' and user_input.alt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif user_input.key == 'ESCAPE':
        # Exit the game
        return {'exit': True}

    return {}


def handle_main_menu(user_input):
    if user_input:
        key_char = user_input.char

        if key_char == 'a':
            return {'new_game': True}
        elif key_char == 'b':
            return {'load_game': True}
        elif key_char == 'c' or user_input.key == 'ESCAPE':
            return {'exit': True}

    return {}


def handle_level_up_menu(user_input):
    if user_input:
        key_char = user_input.char

        if key_char == 'a':
            return {'level_up': 'hp'}
        elif key_char == 'b':
            return {'level_up': 'str'}
        elif key_char == 'c':
            return {'level_up': 'def'}

    return {}


def handle_character_screen(user_input):
    if user_input.key == 'ESCAPE':
        return {'exit': True}

    return {}


def handle_mouse(mouse_event):
    if mouse_event:
        (x, y) = mouse_event.cell

        if mouse_event.button == 'LEFT':
            return {'left_click': (x, y)}
        elif mouse_event.button == 'RIGHT':
            return {'right_click': (x, y)}

    return {}

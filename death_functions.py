from game_messages import Message

from game_states import GameStates

from render_functions import RenderOrder

import random


def kill_player(player, colors):
    player.char = '%'
    player.color = colors.get('dark_red')

    return Message('You died!', colors.get('red')), GameStates.PLAYER_DEAD


def kill_monster(monster, colors):
    msg_int = random.randint(1,4)

    monster_death_message = {
    1:Message('{0} dies!'.format(monster.name.capitalize()), colors.get('orange')),
    2:Message('{0} drops down dead.'.format(monster.name.capitalize()), colors.get('orange')),
    3:Message('Life fades away from {0}.'.format(monster.name.capitalize()), colors.get('orange')),
    4:Message('{0} lives no more.'.format(monster.name.capitalize()), colors.get('orange'))
    }

    death_message = monster_death_message[msg_int]

    monster.char = '%'
    monster.color = colors.get('dark_red')
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = 'remains of ' + monster.name
    monster.render_order = RenderOrder.CORPSE

    return death_message

"""The implementation of the Harden move.

This move increases the user's Defense stat."""

import random
from utils import Printer

NAME = 'Harden'
PP_COST = 5
CAN_DISABLE = True

def perform(user, other):
    """Perform Harden."""
    increase = random.randint(2, 3 + int(0.1 * user.stats['Special'] * user.stats['Defense']))
    other.stats['Recent damage'] = 0
    user.stats['Base Defense'] += increase
    Printer.print_ui('  {} increases its Defense by {}.'.format(user.name, increase))

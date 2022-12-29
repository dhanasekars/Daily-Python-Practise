""" 
Created on : 29/12/22 2:43 PM
@author : ds
https://www.youtube.com/watch?v=g8nQ90Hk328
"""

import logging

# Create and configure logger
import math

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="/Users/ds/Documents/Lumberjack.Log", level=logging.DEBUG, format=LOG_FORMAT, filemode='w')
logger = logging.getLogger()


# logger.debug("this is a harmless debug message.")
# logger.info("just some useful info.")
# logger.warning("i'm sorry, but i can't do that")
# logger.error("Did you just try to divide by zero?")
# logger.critical("The entire internet is down")


def quadratic_formula(a, b, c):
    """ Return the solutions to the equation ax^2 + bx + c = 0."""
    logger.info("quadratic_formula( {0}, {1}, {2})".format(a, b, c))

    # compute the discriminant
    logger.debug("# compute the discriminant")
    disc = b ** 2 - 4 * a * c

    # compute the two roots
    logger.debug("# Compute the two roots")
    root1 = (-b + math.sqrt(disc)) / (2 * a)
    root2 = (-b - math.sqrt(disc)) / (2 * a)

    # Return the roots
    logger.debug(" # Return the roots")
    return root1, root2


roots = quadratic_formula(1, 0, 1)
print(roots)
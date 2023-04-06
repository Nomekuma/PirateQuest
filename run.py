import sys
import main # The main function of your game
# Remeber to add name in terminal after running the game
# ------------------ main ------------------#
# The major, minor version numbers your require
MIN_VER = (3, 9)
# The major, minor version numbers of the current Python interpreter
if sys.version_info[:2] < MIN_VER:
    sys.exit("This game requires Python {}.{}.".format(*MIN_VER)) 
else:
    main()
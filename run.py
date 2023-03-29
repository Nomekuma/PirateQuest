#Both works to run the game, but the second one is better because it's more portable
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path + "/src")
import main
# more portable
import  sys
import main
MIN_VER = (3, 9)

if sys.version_info[:2] < MIN_VER:
    sys.exit("This game requires Python {}.{}.".format(*MIN_VER))
else:
    main()
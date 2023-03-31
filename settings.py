# # Basic level map,tiles pixel,screen width and height
# level_map = [
# '                            ',
# '                            ',
# '         P                   ',
# ' XX   XXXX            XX    ',
# ' XX                        ',
# ' XXXX         XX         XX ',
# ' XXXX       XX              ',
# ' XX    X  XXXX    XX  XX    ',
# '      X  XXXX    XX  XXXX   ',
# '    XXXX  XXXXXX  XX  XXXX  ',
# 'XXXXXXXX  XXXXXX  XX  XXXX  ']
# #------------------------------------------------------------------------------------------------
# # pixel size of each tile
# tile_size = 55
# width = 1280
# # height is calculated based on the level map/it is relative to the level map
# height = len(level_map) * tile_size # len(level_map) is the number of rows in the level map
# #------------------------------------------------------------------------------------------------
vertical_tile_number = 11
tile_size =64
height = vertical_tile_number * tile_size
width= 1280

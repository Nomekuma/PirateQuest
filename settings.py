# Basic level map,tiles pixel,screen width and height
level_map = [
'                            ',
'                            ',
'         P                   ',
' XX   XXXX            XX    ',
' XX                        ',
' XXXX         XX         XX ',
' XXXX       XX              ',
' XX    X  XXXX    XX  XX    ',
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']
#------------------------------------------------------------------------------------------------
# pixel size of each tile
tile_size = 55
width = 1200
# height is calculated based on the level map/it is relative to the level map
height = len(level_map) * tile_size # len(level_map) is the number of rows in the level map

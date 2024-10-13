from Array2D import Array2D
class LifeGrid :
# Defines constants to represent the cell states.
 DEAD_CELL = 0
 LIVE_CELL = 1

# Creates the game grid and initializes the cells to dead.
 def __init__( self, numRows, numCols ):
# Allocate the 2-D array for the grid.
  self._grid = Array2D( numRows, numCols )
# Clear the grid and set all cells to dead.
  #self.configure( list() )

# Returns the number of rows in the grid.
 def numRows( self ):
  return self._grid.numrows()

# Returns the number of columns in the grid.
 def numCols( self ):
  return self._grid.numcols()

# Configures the grid to contain the given live cells.
 def configure(self, coordList):
     self._grid.clear(LifeGrid.DEAD_CELL)
     for coord in coordList:
         self.setCell(coord[0], coord[1])


# Does the indicated cell contain a live organism?
 def isLiveCell( self, row, col ):
  return self._grid[row, col] == LifeGrid.LIVE_CELL

# Clears the indicated cell by setting it to dead.
 def clearCell( self, row, col ):
  self._grid[row, col] = LifeGrid.DEAD_CELL

# Sets the indicated cell to be alive. 
 def setCell( self, row, col ):
  self._grid[row, col] = LifeGrid.LIVE_CELL



#Returns the number of live neighbors for the given cell.
#def numLiveNeighbors( self, row, col ):

 def numLiveNeighbors(self, row, col):
       count = 0

       for i in range(max(0, row-1), min(self.numRows(), row+2)):
           for j in range(max(0, col-1), min(self.numCols(), col+2)):
               if (i, j) != (row, col) and self.isLiveCell(i, j):
                    count += 1

       return count
 


 # Program for playing the game of Life.
#from life import LifeGrid

# Define the initial configuration of live cells.
#INIT_CONFIG = [ (1,1), (1,2), (2,2), (3,2) ]
INIT_CONFIG = [ (1,2), (2,1), (2,2), (2,3) ]

# Set the size of the grid.
GRID_WIDTH = 10
GRID_HEIGHT = 10

# Indicate the number of generations.
NUM_GENS = 8

def main():
# Construct the game grid and configure it.
 grid = LifeGrid( GRID_WIDTH, GRID_HEIGHT )
 grid.configure( INIT_CONFIG )
 # Play the game.
 draw( grid )
 print()
 print("------------------------------------------------")
 for i in range( NUM_GENS ):
  evolve( grid )
  print("Generation = ",i+1 )
  print("------------------------------------------------")

  draw( grid )
  print()
  print("------------------------------------------------")


def evolve( grid ):
  # List for storing the live cells of the next generation.
  liveCells = list()

  # Iterate over the elements of the grid.
  for i in range( grid.numRows() ) :
    for j in range( grid.numCols() ) :

      # Determine the number of live neighbors for this cell.

      neighbors = grid.numLiveNeighbors( i, j )

      # Add the (i,j) tuple to liveCells if this cell contains
      # a live organism in the next generation.
      if (neighbors == 2 and grid.isLiveCell( i, j )) or (neighbors == 3 ) :
        liveCells.append( (i, j) )


  # Reconfigure the grid using the liveCells coord list.
  grid.configure( liveCells )


# Prints a text-based representation of the game grid.
def draw(grid):
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            print('*' if grid.isLiveCell(i, j) else '.', end=" ")
        print()


main()
// Java program to get least cost path
// in a grid from top-left to bottom-right
import java.io.*;
import java.util.*;

// Always modify ROW, and COLUMN COUNT
class Day15{
	
static int[] dx = { -1, 0, 1, 0 };
static int[] dy = { 0, 1, 0, -1 };
static int ROW = 500;
static int COL = 500;

// Custom class for representing
// row-index, column-index &
// distance of each cell
static class Cell
{
	int x;
	int y;
	int distance;
	
	Cell(int x, int y, int distance)
	{
		this.x = x;
		this.y = y;
		this.distance = distance;
	}
}

// Custom comparator for inserting cells
// into Priority Queue
static class distanceComparator
implements Comparator<Cell>
{
	public int compare(Cell a, Cell b)
	{
		if (a.distance < b.distance)
		{
			return -1;
		}
		else if (a.distance > b.distance)
		{
			return 1;
		}
		else {return 0;}
	}
}

// Utility method to check whether current
// cell is inside grid or not
static boolean isInsideGrid(int i, int j)
{
	return (i >= 0 && i < ROW &&
			j >= 0 && j < COL);
}

// Method to return shortest path from
// top-corner to bottom-corner in 2D grid
static int shortestPath(int[][] grid, int row,
									int col)
{
	int[][] dist = new int[row][col];
	
	// Initializing distance array by INT_MAX
	for(int i = 0; i < row; i++)
	{
		for(int j = 0; j < col; j++)
		{
			dist[i][j] = Integer.MAX_VALUE;
		}
	}
	
	// Initialized source distance as
	// initial grid position value
	dist[0][0] = grid[0][0];
	
	PriorityQueue<Cell> pq = new PriorityQueue<Cell>(
				row * col, new distanceComparator());
				
	// Insert source cell to priority queue
	pq.add(new Cell(0, 0, dist[0][0]));
	while (!pq.isEmpty())
	{
		Cell curr = pq.poll();
		for(int i = 0; i < 4; i++)
		{
			int rows = curr.x + dx[i];
			int cols = curr.y + dy[i];
			
			if (isInsideGrid(rows, cols))
			{
				if (dist[rows][cols] >
					dist[curr.x][curr.y] +
					grid[rows][cols])
				{
					
					// If Cell is already been reached once,
					// remove it from priority queue
					if (dist[rows][cols] != Integer.MAX_VALUE)
					{
						Cell adj = new Cell(rows, cols,
									dist[rows][cols]);
										
						pq.remove(adj);
					}
					
					// Insert cell with updated distance
					dist[rows][cols] = dist[curr.x][curr.y] +
									grid[rows][cols];
										
					pq.add(new Cell(rows, cols,
							dist[rows][cols]));
				}
			}
		}
	}
	return dist[row - 1][col - 1];
}

// Driver code
public static void main(String[] args)
throws IOException
{
	final Scanner scanner = new Scanner(new File("data.txt"));    
	final int[][] matrix = new int[ROW][COL];
	String sample = scanner.next();
	for (int i = 0; i < matrix.length; ++i) {
		for (int j = 0; j < matrix[i].length; ++j) {
			matrix[i][j] = sample.charAt(j) - '0';
		}
		if(scanner.hasNext())
			sample = scanner.next();
	}
		
	System.out.println(shortestPath(matrix, ROW, COL) - matrix[0][0]);
}
}

// This code is contributed by jigyansu

'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

Coordinates:
    x+
------>
|
|+y

Table:              Example Route:
*    *    *         *----*    *         
                         |
*    *    *         *    *    *  
                         |   
*    *    *         *    *----*
'''

class Node:
    def __init__(self,x,y,prev):
      self.coord_x = x
      self.coord_y = y
      self.prev_node = prev
    
    def print_coord(self):
        print("(" + self.coord_x + ", " + self.coord_y + ")")

class Grid:
    def __init__(self,xmax, ymax):
        self.xmax = xmax
        self.ymax = ymax

class Route_List:
    def __init__(self, origin, final):
      self.origin = origin
      self.final = final

    def listprint(self): 
        to_print = self.final
        while to_print is not None:
            print("(", to_print.coord_x, ", ", to_print.coord_y,  ")", end=" ")
            to_print = to_print.prev_node
        print()

    def return_list_route(self):
        list_route = []
        to_list = self.final
        while to_list is not None:
            list_route.append((to_list.coord_x, to_list.coord_y))
            to_list = to_list.prev_node 

def print_route(list_route):
    if (not(list_route)):
        return None
    cube_size = 3
    print(list_route)
    Coordinates = [
        [0,0], [1,0], [2,0], [3,0],
        [0,1], [1,1], [2,1], [3,1],
        [0,2], [1,2], [2,2], [3,2],
        [0,3], [1,3], [2,3], [3,3]]

    print(" ")

    for j in range(cube_size):
        i = 0
        while (i<cube_size):
            if [i,j] in Coordinates:
                print("*", end=" ")
            else:
                print(" ", end=" ")
            if ([i,j] in list_route)and([i+1,j] in list_route):
                print("->", end=" ")
            else:
                print("  ", end=" ")
            i+=1
        print(" ")
        for x in range(cube_size):       
            if ([x,j] in list_route)and([x,j+1] in list_route):
                print("|", end = "")
            else:
                print("     ", end = "")
        print(" ")

#route_list = [[0,0],[0,1],[1,1],[1,2],[2,2]]
#print_route(route_list)
#route_list = [[0,0],[1,0],[2,0],[2,1],[2,2]]
#print_route(route_list)

def get_next_nodes_alternatives(node, grid):

    temp_list = []
    if ( node.coord_x< grid.xmax):
        right_node = Node(node.coord_x +1, node.coord_y, node)
        temp_list.append(right_node)
    if (node.coord_y < grid.ymax):
        down_node = Node(node.coord_x, node.coord_y+1, node)
        temp_list.append(down_node)
    return temp_list

# It's takes a lot of time to get the routes, but it's possible to get the first so see the paterns (The Pascal Triangle)
def get_routes(origin, grid):
    num_routes = 0
    nodes_to_check = [origin]
    final_nodes = []
    while (True):
        actual_node = nodes_to_check.pop()
        temp_list = get_next_nodes_alternatives(actual_node, grid)
        if (len(temp_list) == 0): # To check final reach
            num_routes +=1
            final_nodes.append(actual_node)
        else:
            for item in temp_list:
                nodes_to_check.append(item)
        if (not nodes_to_check):
            break
        if num_routes>1000000:
            print("above 1 million")
    return [num_routes,final_nodes]
    #return routes

def print_pascal_triangle(gird_size):

    list = [[]]
    for i in range (1, gird_size+2):
        list[0].append(1)

    list.append([])
    for i in range (1, gird_size+2):
        list[1].append(i)

    for j in range(2, gird_size+1):
        list.append([1])
        for i in range(1, gird_size+1):
            list[j].append(list[j][i-1]+list[j-1][i])

    for fila in list:
        for valor in fila:
            print (valor, end =" ")
        print()

# Code to get number of routes in small grids. Costly expensive
for i in range(2,10):
    print("Grid size: ", i)
    g = Grid(i,i)
    origin = Node(0,0,None)
    gr = (get_routes(origin,g))[0]
    print ("Number of routes: ", gr)

#Example of one of the routes:
i = 2
print("Particular Example Route Grid Size", i)
print("Grid size: ", i)
g = Grid(i,i)
origin = Node(0,0,None)
gr = (get_routes(origin,g))[0]
print ("Number of routes: ", gr)
final_nodes = get_routes(origin,g)[1]
print("One of the final nodes: ", final_nodes[0]) #the first final node of
route_list_grid_5 = Route_List(None, final_nodes[0])
route_list_grid_5.listprint()
##print_route(route_list_grid_5.return_list_route()) #Solo funciona por ahora con listas de array, no listas de nodos

#The last value of this printing it's the solution:
#print_pascal_triangle(20)
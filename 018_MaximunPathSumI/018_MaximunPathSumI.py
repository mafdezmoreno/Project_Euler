from operator import ne


class Node:
    
    def __init__(self, dataval = None, padre = None, index = 0):
        self.dataval = dataval
        self.padre = padre
        self.index = index
        if padre:
            self.dataval = dataval + padre.dataval
 
def max_path_calculator(triangle_list):
    prev_nodes = [Node(dataval=triangle_list[0][0])]
    for i in range(1,len(triangle_list)):
        next_nodes = []
        while prev_nodes:
            transfer_node = prev_nodes.pop()
            next_nodes.append(Node(dataval=triangle_list[i][transfer_node.index], 
                                    padre = transfer_node, 
                                    index = transfer_node.index))
            next_nodes.append(Node(dataval=triangle_list[i][transfer_node.index+1], 
                                    padre =transfer_node, 
                                    index = transfer_node.index+1))
        prev_nodes = next_nodes

    values = []
    for element in prev_nodes:
        #print(element.dataval)
        values.append(element.dataval)

    print('Máximo', max(values))

def file_to_list(path):
    a_file = open(path, "r")

    test_numbers = []
    for line in a_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        line_list_int = []
        for element in line_list:
            line_list_int.append(int(element))
        test_numbers.append(line_list_int)

    a_file.close()
    #print(test_numbers)
    return test_numbers

print("\nTest 0")
TriangleTest0 =[ 
        [3],
      [7, 4],
     [2, 4, 6],
    [8, 5, 9, 3],
]

max_path_calculator(TriangleTest0)
print()

print("\nTest 1")
TriangleTest1 = file_to_list("018_MaximunPathSumI/Test.txt")
max_path_calculator(TriangleTest1)
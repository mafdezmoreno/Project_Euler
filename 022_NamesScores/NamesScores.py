'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
import string
alphabet_dict = {chr(i+64):i for i in range(1,27)}



def name_score(name):
    
    score = 0
    for element in name:
        score += alphabet_dict[element]
        #print (element , alphabet_dict[element] )
    
    return score

def calculate_full_scores(sorted_list):
    
    score = 0
    i=1
    for element in sorted_list:
        score += name_score(element)*i
        if element == "COLIN":
            print (i, element, name_score(element))
        i+=1
    return(score)

def file_to_sorted_array():

    text_file = open("022_NamesScores/p022_names.txt", "r")
    lines = text_file.read().split('","')
    lines[-1]=lines[-1][:-1] #Remove first ""
    lines[0]=lines[0][1:] #Remove last ""
    #print(lines)
    #print(lines[0])
    lines.sort()
    #print(lines)
    return lines

def tests():
    
    print(alphabet_dict)
    print(name_score ("COLIN"))
    print(file_to_sorted_array())
    print(calculate_full_scores(file_to_sorted_array()))

def solution():
    print(calculate_full_scores(file_to_sorted_array()))

#tests()
solution()

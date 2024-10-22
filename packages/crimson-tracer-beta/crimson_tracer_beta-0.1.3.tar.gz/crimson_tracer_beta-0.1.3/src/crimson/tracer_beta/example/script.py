from anytree import Node


def lvl1(
        

):

    node = Node('root')

    lvl2_1(


    )

    lvl2_2()

    lvl3(node.name)


def lvl2_1(
        

):

    "hi, I am level 2-1. I have a return value"
    return 1


def lvl2_2(
        
):

    lvl3("lvl2_2")

    output = "return value with variable"
    return output


def lvl3(name):
    f"hi, I am {name}"

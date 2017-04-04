import copy
out = open('output.txt', 'w+')
class TreeNode:
    def __init__(self):  # object initializer to set attributes (fields)
        self.depth = 0
        self.parent = None
        self.children = []
        self.state = []
        self.nodename = None
        self.eval = None
        self.gamescore = None
        self.player = None  # Person who will play now
        row1 = [99, -8, 8, 6, 6, 8, -8, 99]
        row2 = [-8, -24, -4, -3, -3, -4, -24, -8]
        row3 = [8, -4, 7, 4, 4, 7, -4, 8]
        row4 = [6, -3, 4, 0, 0, 4, -3, 6]
        row5 = [6, -3, 4, 0, 0, 4, -3, 6]
        row6 = [8, -4, 7, 4, 4, 7, -4, 8]
        row7 = [-8, -24, -4, -3, -3, -4, -24, -8]
        row8 = [99, -8, 8, 6, 6, 8, -8, 99]
        self.weights = []
        self.weights.append(row1)
        self.weights.append(row2)
        self.weights.append(row3)
        self.weights.append(row4)
        self.weights.append(row5)
        self.weights.append(row6)
        self.weights.append(row7)
        self.weights.append(row8)

    def addchild(self, child):
        self.children.append(child)

    def caleval(self):
        if player == 'X':
            pl='X'
            op='O'
        else:
            pl='O'
            op='X'
        sum1 = 0
        sum2 = 0
        for i in range(8):
            for j in range(8):
                if (self.state[i][j] == pl):
                    sum1 = sum1 + self.weights[i][j]
                elif (self.state[i][j] == op):
                    sum2 = sum2 + self.weights[i][j]
        return sum1 - sum2

    def addparent(self, parent):
        self.parent = parent


import sys
answer = []
#Class (AlphaBeta)
class AlphaBeta:
    #First call to AlphaBeta using the given state
    def execalphabeta(self, rootnode):
        rootnode.children = self.generatechildren(rootnode)
        v = self.maxvalue(rootnode, -sys.maxint - 1, sys.maxint)
        for child in rootnode.children:
            if child.eval == v:
                return child

    #Max player
    def maxvalue(self, node, alpha, beta):
        # for ln in node.state:
        #     print ln
        # print node.depth
        if self.checkcutoff(node, depth):
            value = self.eval(node)
            self.display(node.nodename, node.depth, value, alpha, beta)
            print node.nodename, " ", str(node.depth), " ", value, " ", alpha, " ", beta
            return value
        node.children = self.generatechildren(node)
        if self.checkterminal(node):
            value = self.eval(node)
            self.display(node.nodename, node.depth, value, alpha, beta)
            print node.nodename, " ", node.depth, " ", value, " ", alpha, " ", beta
            return value
        v = -sys.maxint - 1
        for child in node.children:
            # print child.nodename,"  depth:",child.depth
            # for l in child.state:
            #     print l
            self.display(node.nodename, node.depth, v, alpha, beta)
            print node.nodename, " ", node.depth, " ", v, " ", alpha, " ", beta
            v = max(v, self.minvalue(child, alpha, beta))
            if v >= beta:
                node.eval = v
                self.display(node.nodename, node.depth, v, alpha, beta)
                print node.nodename, " ", node.depth, " ", v, " ", alpha, " ", beta
                return v
            alpha = max(alpha,v)

        self.display(node.nodename, node.depth, v, alpha, beta)
        print node.nodename, " ", node.depth, " ", v, " ", alpha, " ", beta
        node.eval = v
        return v

    #Min player
    def minvalue(self, node, alpha, beta):
        # for ln in node.state:
        #     print ln
        # print node.depth
        if self.checkcutoff(node, depth):
            value = self.eval(node)
            self.display(node.nodename, node.depth, value, alpha, beta)
            print node.nodename, " ", node.depth, " ", value, " ", alpha, " ", beta
            return value
        node.children = self.generatechildren(node)
        if self.checkterminal(node):
            value = self.eval(node)
            self.display(node.nodename, node.depth, value, alpha, beta)
            print node.nodename, " ", node.depth, " ", value, " ", alpha, " ", beta
            return value
        v = sys.maxint
        for child in node.children:
            # print child.nodename,"  depth:",child.depth
            # for l in child.state:
            #     print l


            self.display(node.nodename, node.depth, v, alpha, beta)
            print node.nodename, " ", node.depth, " ", v, " ", alpha, " ", beta
            v = min(v, self.maxvalue(child, alpha, beta))
            if v <= alpha:
                node.eval = v
                self.display(node.nodename, node.depth, v, alpha, beta)
                print node.nodename, " ", node.depth, " ", v, " ", alpha, " ", beta
                return v
            beta = min(beta,v)
        self.display(node.nodename, node.depth, v, alpha, beta)
        print node.nodename, " ", node.depth, " ", v, " ", alpha, " ", beta
        node.eval = v
        return v

    #Test to check for a terminal state
    def checkterminal(self, node):
        if len(node.children) == 0:
            return True
        else:
            return False

    #Return the utility of a state
    def eval(self,node):
        node.eval = node.gamescore
        return node.eval

    #Generate the next possible moves for any given state
    def generatechildren(self, node):
        cutoff = self.checkcutoff(node, depth)
        if (cutoff == True):
            return None
        else:
            if (node.player == 'X'):
                op = 'O'
            else:
                op = 'X'
            for i in range(8):
                for j in range(8):
                    if (validposition(i, j, node.state)):
                        newstate = searchpositions(node.state, i, j, node.player)
                        if newstate == [] or self.childpresent(node, newstate):
                            continue
                        else:
                            childnode = TreeNode()
                            childnode.nodename = self.getnodename(i, j)
                            childnode.state = newstate
                            childnode.player = op
                            childnode.parent = node
                            childnode.gamescore = childnode.caleval()
                            childnode.depth = childnode.parent.depth + 1
                            node.children.append(childnode)
                            # return childnode
                            # self.generatechildren(childnode)
            if node.parent is None and len(node.children)==0:
                childnode = TreeNode()
                childnode.nodename = "pass"
                childnode.state = node.state
                childnode.player = op
                childnode.parent = node
                childnode.gamescore = childnode.caleval()
                childnode.depth = childnode.parent.depth + 1
                node.children.append(childnode)
            elif node.parent is not None and len(node.children)==0 and node.parent.nodename != 'pass':
                childnode = TreeNode()
                childnode.nodename = "pass"
                childnode.state = node.state
                childnode.player = op
                childnode.parent = node
                # check this can we negate?
                # Wrong state OP for IP 4
                # Ans wrong for 1,3,4
                childnode.gamescore = childnode.caleval()
                childnode.depth = childnode.parent.depth + 1
                node.children.append(childnode)
            return node.children

    #Run a cutoff check on the current depth
    def checkcutoff(self, node, d):
        if (node.depth >= d):
            return True
        else:
            return False

    #Get the position of placement
    def getnodename(self, i, j):
        if (j == 0):
            a = 'a'
        if (j == 1):
            a = 'b'
        if (j == 2):
            a = 'c'
        if (j == 3):
            a = 'd'
        if (j == 4):
            a = 'e'
        if (j == 5):
            a = 'f'
        if (j == 6):
            a = 'g'
        if (j == 7):
            a = 'h'
        # print a+str(i+1)
        return a + str(i + 1)


    def childpresent(self, parent, newstate):
        for elem in parent.children:
            if (elem.state == newstate):
                return 1;
        return 0;

    def display(self,name,dep,val,alpha,beta):
        if (alpha == (-sys.maxint - 1)):
            alphastring = "-Infinity"
        else:
            alphastring = str(alpha)

        if (beta == sys.maxint):
            betastring = "Infinity"
        else:
            betastring = str(beta)
        if (val == sys.maxint):
            valuestring = "Infinity"
        elif (val == (-sys.maxint - 1)):
            valuestring = "-Infinity"
        else:
            valuestring = str(val)
        answer.append("%s,%d,%s,%s,%s\n" % (name, dep, valuestring, alphastring, betastring))


#Main
file = open("input.txt", "r")
fr = file.read();
l = fr.splitlines();
test = []
state = []
for line in l:
    print line
    test = []
    if len(line) > 1:
        for i in range(len(line)):
            test.append(line[i])
        state.append(test)


def validposition(x, y, stat):
    if (x >= 0 and y >= 0 and x < 8 and y < 8 and stat[x][y] == '*'):
        return 1
    else:
        return 0


# Are there 2 moves play and pass??

def searchpositions(abc, i, j, player):
    if (player == 'X'):
        op = 'O'
    else:
        op = 'X'
    flag = []
    board = copy.deepcopy(abc)
    xpos = i
    ypos = j
    if (validposition(i, j, board) == 1):
        cnt = 0;
        # print ("i=",xpos," j=",ypos)
        while (i - 1 >= 0 and j - 1 >= 0 and board[i - 1][j - 1] == op):
            # print i - 1," ",j - 1," ",state[i - 1][j - 1]
            i -= 1
            j -= 1
        # print state[i - 1][j - 1]
        if (i > 0 and j > 0 and board[i - 1][j - 1] == player and board[i][j] == op and not flag.__contains__(
                [xpos, ypos])):
            # flag.append([xpos, ypos])
            while (i - 1 <= xpos and j - 1 <= ypos):
                board[i - 1][j - 1] = player
                i += 1
                j += 1
        i = xpos
        j = ypos

        while (i - 1 >= 0 and j >= 0 and board[i - 1][j] == op):
            i -= 1
        if (i > 0 and board[i - 1][j] == player and board[i][j] == op and not flag.__contains__([xpos, ypos])):
            # flag.append([xpos, ypos])
            while (i - 1 <= xpos):
                board[i - 1][j] = player
                i += 1

        i = xpos
        j = ypos
        while (i - 1 >= 0 and j + 1 <= 7 and board[i - 1][j + 1] == op):
            i -= 1
            j += 1
        if (i > 0 and j < 7 and board[i - 1][j + 1] == player and board[i][j] == op and not flag.__contains__(
                [xpos, ypos])):
            # flag.append([xpos, ypos])
            while (i - 1 <= xpos and j + 1 >= ypos):
                board[i - 1][j + 1] = player
                i += 1
                j -= 1

        i = xpos
        j = ypos

        while (i >= 0 and j + 1 <= 7 and board[i][j + 1] == op):
            # print i, " ", j + 1, " ", board[i][j + 1]
            j += 1
            # print i, " ", j + 1, " ", board[i][j + 1]
        if (j < 7 and board[i][j + 1] == player and board[i][j] == op and not flag.__contains__([xpos, ypos])):
            while (j + 1 >= ypos):
                board[i][j + 1] = player
                j -= 1
        i = xpos
        j = ypos

        while (i >= 0 and j - 1 >= 0 and board[i][j - 1] == op):
            j -= 1
        if (j > 0 and board[i][j - 1] == player and board[i][j] == op and not flag.__contains__([xpos, ypos])):
            # flag.append([xpos, ypos])
            while (j - 1 <= ypos):
                board[i][j - 1] = player
                j += 1

        i = xpos
        j = ypos

        while (i + 1 <= 7 and j + 1 <= 7 and board[i + 1][j + 1] == op):
            i += 1
            j += 1
        if (i < 7 and j < 7 and board[i + 1][j + 1] == player and board[i][j] == op and not flag.__contains__(
                [xpos, ypos])):
            # flag.append([xpos, ypos])
            while (i + 1 >= xpos and j + 1 >= ypos):
                board[i + 1][j + 1] = player
                i -= 1
                j -= 1

        i = xpos
        j = ypos

        while (i + 1 <= 7 and board[i + 1][j] == op):
            i += 1
        if (i < 7 and board[i + 1][j] == player and board[i][j] == op and not flag.__contains__([xpos, ypos])):
            # flag.append([xpos, ypos])
            while (i + 1 >= xpos):
                board[i + 1][j] = player
                i -= 1
        i = xpos
        j = ypos

        while (i + 1 <= 7 and j - 1 >= 0 and board[i + 1][j - 1] == op):
            i += 1
            j -= 1
        if (i < 7 and j > 0 and board[i + 1][j - 1] == player and board[i][j] == op and not flag.__contains__(
                [xpos, ypos])):
            # flag.append([xpos, ypos])
            while (i + 1 >= xpos and j - 1 <= ypos):
                board[i + 1][j - 1] = player
                i -= 1
                j += 1

    # for line in board:
    #     print line
    if board == abc:
        return []
    else:
        return board
        # if(state[i-1][j-1]=='*' and state[i-1][j]=='*' and state[i-1][j+1]=='*' and state[i][j-1]=='*' and state[i][j+1]=='*' and state[i+1][j-1]=='*' and state[i+1][j]=='*' and state[i+1][j+1]=='*'):


player = l[0]
depth = (int)(l[1])
print("player=%s" % player)
print("depth=%d" % depth)
# print("state=", state)
# row=[0,0,0,0,0,0,0,0]
positions = []

obj = AlphaBeta()

rootnode = TreeNode()
rootnode.nodename = "root"
rootnode.state = state
rootnode.player = player
rootnode.gamescore = rootnode.caleval()
rootnode.eval = -sys.maxint - 1
rootnode.depth = 0
result = obj.execalphabeta(rootnode)
print "answer"
if result is None:
    for line in rootnode.state:
        for i in line:
            out.write(i)
        out.write('\n')
    out.write('Node,Depth,Value,Alpha,Beta')
    out.close()
else:
    for line in result.state:
        print line

    for line in result.state:
        for i in line:
            out.write(i)
        out.write('\n')
    out.write('Node,Depth,Value,Alpha,Beta\n')
    for l in answer:
        out.write(l)
    out.close()

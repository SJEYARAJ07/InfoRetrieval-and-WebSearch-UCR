dampingFactor = 0.85
epsilon = 0.00001
pageRankNode1 = 1
pageRankNode2 = 1
pageRankNode3 = 1
pageRankNode4 = 1
pageRankNode5 = 1

diff = 1
itr = 0

while diff > epsilon:
    # print('***Iteration %d***' % itr)

    print('Page rank of Node 1:%.6f' % (pageRankNode1))
    print('Page rank of Node 2:%.6f' % (pageRankNode2))
    print('Page rank of Node 3:%.6f' % (pageRankNode3))
    print('Page rank of Node 4:%.6f' % (pageRankNode4))
    print('Page rank of Node 5:%.6f' % (pageRankNode5))

    new_pageRankNode1 = (1 - dampingFactor) + dampingFactor * (pageRankNode3/1)
    new_pageRankNode2 = (1 - dampingFactor) + dampingFactor * (pageRankNode1/1)
    new_pageRankNode3 = (1 - dampingFactor) + dampingFactor * (pageRankNode2/2)
    new_pageRankNode4 = (1 - dampingFactor)
    new_pageRankNode5 = (1 - dampingFactor) + dampingFactor * ((pageRankNode2/2) + (pageRankNode4/1) + (pageRankNode5/1))

    itr+=1
    print('***Iteration %d***' % itr)
    print('Page rank of Node 1:%.6f' % (new_pageRankNode1))
    print('Page rank of Node 2:%.6f' % (new_pageRankNode2))
    print('Page rank of Node 3:%.6f' % (new_pageRankNode3))
    print('Page rank of Node 4:%.6f' % (new_pageRankNode4))
    print('Page rank of Node 5:%.6f' % (new_pageRankNode5))

    difference_list = []
    differenceInRanking1 = abs(new_pageRankNode1-pageRankNode1)
    differenceInRanking2 = abs(new_pageRankNode2-pageRankNode2)
    differenceInRanking3 = abs(new_pageRankNode3-pageRankNode3)
    differenceInRanking4 = abs(new_pageRankNode4-pageRankNode4)
    differenceInRanking5 = abs(new_pageRankNode5-pageRankNode5)
    print('Rank Difference \t\t Node 1:%.6f, Node 2:%.6f, Node 3:%.6f, Node 4:%.6f, Node 5:%.6f' % \
    (differenceInRanking1, differenceInRanking2, differenceInRanking3, differenceInRanking4, differenceInRanking5))
    difference_list.extend([differenceInRanking1, differenceInRanking2, differenceInRanking3, differenceInRanking4, differenceInRanking5])
    diff = max(difference_list)

    pageRankNode1 = new_pageRankNode1
    pageRankNode2 = new_pageRankNode2
    pageRankNode3 = new_pageRankNode3
    pageRankNode4 = new_pageRankNode4
    pageRankNode5 = new_pageRankNode5

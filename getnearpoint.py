


def getNearestPoint(root, parent, point, minDis, tarPoint):
    if root == None:
        return
    root.isVisited = True
    dis = pow(point.x - root.point.x, 2) + pow(point.y - root.point.y, 2)
    if minDis < 0 or dis < minDis:
        tarPoint = root.point
        minDis = dis
    if (root.splitX and point.x < root.point.x) or (root.splitY and point.y < root.point.y):
        if root.leftTree and not root.leftTree.isVisited:
            getNearestPoint(root.leftTree, root, point, minDis, tarPoint)
    else:
        if root.rightTree and not root.rightTree.isVisited:
            getNearestPoint(root.rightTree, root, point, minDis, tarPoint)
    rL = minDis + 1
    rR = minDis + 1
    childrL = minDis + 1
    childrR = minDis + 1
    if parent.leftTree:
        rL = pow(point.x - parent.leftTree.point.x, 2) + pow(point.y - parent.leftTree.point.y, 2)
    if parent.rightTree:
        rR = pow(point.x - parent.rightTree.point.x, 2) + pow(point.y - parent.rightTree.point.y, 2)
    if root.leftTree:
        childrL = pow(point.x - root.leftTree.point.x, 2) + pow(point.y - root.leftTree.point.y, 2)
    if root.rightTree:
        childrR = pow(point.x - root.rightTree.point.x, 2) + pow(point.y - root.rightTree.point.y, 2)
    if parent.leftTree and not parent.leftTree.isVisited and rL < minDis:
        getNearestPoint(parent.leftTree, parent, point, minDis, tarPoint)
    if parent.rightTree and not parent.rightTree.isVisited and rR < minDis:
        getNearestPoint(parent.rightTree, parent, point, minDis, tarPoint)
    if root.leftTree and not root.leftTree.isVisited and childrL < minDis:
        getNearestPoint(root.leftTree, root, point, minDis, tarPoint)
    if root.rightTree and not root.rightTree.isVisited and childrR < minDis:
        getNearestPoint(root.rightTree, root, point, minDis, tarPoint)
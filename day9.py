def backspaceCompare(self, S: str, T: str):
    sStack = []
    tStack = []
    for i in range(len(S)):
        if S[i] is not '#':
            sStack.append(S[i])
        elif sStack:
            sStack.pop()
    for i in range(len(T)):
        if T[i] is not '#':
            tStack.append(T[i])
        elif tStack:
            tStack.pop()
    return sStack == tStack
'''
For given list of folders, we need to find out what is the folder path for
a given folder id from root.
Root folder id is always zero. no other folder can have zero as there folder ID.
There would be multiple path from root folder.
A node can have multiple parents.

folderList = [
        {id: 0, subfolders : [7,3], name: 'abc1'},
        {id: 0, subfolders : [9], name: 'abc2'},
        {id: 9, subfolders : [], name: 'abc3'},
        {id: 3, subfolders : [2], name: 'abc4'},
        {id: 2, subfolders : [], name: 'abc5'},
        {id: 7, subfolders : [], name: 'abc6'},
        {id: 8, subfolders : [], name: 'abc7'}
];
for target folder = 2 it should return

/abc1/abc4/abc5
for target folder 8, it should return "" as it is not reachable from root.
'''

from typing import Dict

class Folder:
    def __init__(self, f_id, subfolders, name):
        self.f_id = f_id
        self.subfolders = subfolders
        self.name = name


def find_path(root: Folder, subfolders: Dict[int, Folder], target):
    visited = set()
    path = []

    def dfs(node: Folder):
        if node.f_id in visited:
            return False

        visited.add(node.f_id)
        path.append(node.name)

        if node.name == target:
            return True

        for f_id in node.subfolders:
            if dfs(subfolders[f_id]):
                return True

        path.pop()
        return False

    if dfs(root):
        return "->".join(path)
    return "no-path"


def main():

    # Case 1: There are no roots
    # Case 2: There are multiple roots
    # Case 3: There is a cycle (can be solved with a visited stack)
    # Case 4: If there is no path, it should return 'no-path
    # Case 5: If there is a path, it should return 'abc1->abc2->abc3'
    # Case 6: Using a DFS, we should pop the path if it's not correct

    folderList = [
        Folder(f_id=0, subfolders=[7, 3], name='abc1'),
        Folder(f_id=0, subfolders=[9], name='abc2'),
        Folder(f_id=9, subfolders=[], name='abc3'),
        Folder(f_id=3, subfolders=[2], name='abc4'),
        Folder(f_id=2, subfolders=[], name='abc5'),
        Folder(f_id=7, subfolders=[], name='abc6'),
        Folder(f_id=8, subfolders=[], name='abc7')
    ]

    folders = {folder.f_id: folder
               for folder in folderList if folder.f_id != 0}

    if not any(folder.f_id == 0 for folder in folderList):
        print('no-path')
    else:
        for folder in folderList:
            if folder.f_id == 0:
                print(find_path(root=folder, subfolders=folders, target='abc5'))


if __name__ == '__main__':
    main()

'''

    ��Ŀ��
        ����һ����������һ��Ŀ��ͣ��ҵ����дӸ��ڵ㵽Ҷ�ӽڵ�·���ܺ͵��ڸ���Ŀ��͵�·����
        ˵��:?Ҷ�ӽڵ���ָû���ӽڵ�Ľڵ㡣

            ʾ��:
            �������¶��������Լ�Ŀ���?sum = 22��

                          5
                         / \
                        4   8
                       /   / \
                      11  13  4
                     /  \    / \
                    7    2  5   1
            ����:
            [
               [5,4,11,2],
               [5,8,4,5]
            ]
    ˼·��
         ������Ҫ�ռ�·�����Ҹо�����dfs����ȱ�����ͬʱ��·�����ռ����ɡ�


'''
class Solution:
    def __init__(self):
        self.cur_path = []
        self.res = []

    def pathSum(self, root, sum):
        if not root:
            return []
        self.cur_path.append(root.val)
        sum -= root.val
        if not root.left and not root.right:  # ��Ҷ�ӽڵ�
            if sum == 0:
                print("��ǰ·����", self.cur_path)
                self.res.append(self.cur_path[:])
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        self.cur_path.pop()
        return self.res


#___________________________________    ��ϰ1    ______________________________#
# �ǳ��򵥵�һ����ɣ� ����DFS�������ٽ��� ·�����ռ�����  112���˼·����һ�¡�
cur_path=[]
res=[] # �洢�ɹ���·��
def fun1(root,sum):
    #  �߽���������ʾ��ǰ���ǽڵ㣬��ôֱ�ӷ�����ΪDFSֹͣλ�ü���
    if not root:
        return []

    # ��������£�������
    cur_path.append(root.val)
    sum-=root.val

    #�����Ҷ�ӽڵ�����,�Ǿ��б��Ƿ�����Ч·��
    if not root.left and not root.right:
        if sum==0:
            # ���гɹ�·���ĸ���
            res.append(cur_path[:])

    # ������ �ݹ�ı��������ǵ���  ���������  ����ԭ����
    fun1(root.left,sum)
    fun1(root.right,sum)
    cur_path.pop()

    # ��������Ѿ��ռ���·��  �����ؼ���
    return res

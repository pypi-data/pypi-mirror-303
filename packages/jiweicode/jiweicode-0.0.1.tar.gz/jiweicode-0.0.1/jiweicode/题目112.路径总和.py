

'''
    ��Ŀ��

        ����һ����������һ��Ŀ��ͣ��жϸ������Ƿ���ڸ��ڵ㵽Ҷ�ӽڵ��·��������·�������нڵ�ֵ��ӵ���Ŀ��͡�
        ˵��: Ҷ�ӽڵ���ָû���ӽڵ�Ľڵ㡣
        ʾ��:
                �������¶��������Լ�Ŀ��� sum = 22��

                              5
                             / \
                            4   8
                           /   / \
                          11  13  4
                         /  \      \
                        7    2      1
                ���� true, ��Ϊ����Ŀ���Ϊ 22 �ĸ��ڵ㵽Ҷ�ӽڵ��·�� 5->4->11->2��

'''
#  ����ֱ��ʹ�� �ݹ鷽���ɣ�һ�и㶨   ���ݹ鵽����ʱ����root.val==sum  ˵��Ѱ�ҳɹ�
#  ʱ�临�Ӷ� O(N)  �ռ临�Ӷ��ΪO(N)
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool

        ��������  ������
        """
        return False if not root else root.val==sum if not root.left and not root.right else self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)



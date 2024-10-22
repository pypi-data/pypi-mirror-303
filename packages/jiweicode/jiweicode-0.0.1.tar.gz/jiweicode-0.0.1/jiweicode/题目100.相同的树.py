

'''
     ��Ŀ��������������������дһ�����������������Ƿ���ͬ��
           ����������ڽṹ����ͬ�����ҽڵ������ͬ��ֵ������Ϊ��������ͬ�ġ�

     ˼·������ʹ�õݹ�ķ�ʽ�����Ͻ��� �����жϱȽϼ���

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#  ˼����Ϊ�򵥣� ֱ��ʹ�õݹ�ķ�ʽ�����Ͻ��� �����жϱȽϼ���
#   ʱ�临�Ӷ�ΪO(N)
#   �����������ȫƽ���������ʱΪ?O(log(N))�������£���ȫ��ƽ���������ʱΪO(N)������ά���ݹ�ջ��
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        #�ݹ�ֹͣ����
        if not p and not q:
            return True
        #ͨ���������б𣬵������õ�
        elif p is not None and q is not None:
            if p.val==q.val:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            else:
                return False
        #��Ч�� ���
        else:
            return False
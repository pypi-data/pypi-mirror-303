
'''

    ����һ�����������ж����Ƿ��Ǹ߶�ƽ��Ķ�������

    �����У�һ�ø߶�ƽ�����������Ϊ��һ��������ÿ���ڵ� ���������������ĸ߶Ȳ�ľ���ֵ������1��


'''


# һ������ʱ�� ˢ������ɣ� ֱ��ͨ��������������ĸ߶Ƚ��еݹ��б𼴿�
# ʱ�临�Ӷ�ΪO(NlogN)���ռ临�Ӷ�ΪO(log(N))
class Solution(object):
    #  ��ȡƽ���� �����Ľ��
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            # ����ƽ���������������һ��������� ������Ȳ�СЩ������������Ҷ���ƽ�������
            return abs(self.deep(root.left) - self.deep(root.right)) <= 1 and self.isBalanced(
                root.left) and self.isBalanced(root.right)

    def deep(self, root):
        if not root:
            return 0
        else:
            left = self.deep(root.left) + 1
            right = self.deep(root.right) + 1
            return max(left, right)
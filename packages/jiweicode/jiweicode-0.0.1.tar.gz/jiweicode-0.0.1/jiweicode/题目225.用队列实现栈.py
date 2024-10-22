
'''
ʹ�ö���ʵ��ջ�����в�����

push(x) -- Ԫ�� x ��ջ
pop() -- �Ƴ�ջ��Ԫ��
top() -- ��ȡջ��Ԫ��
empty() -- ����ջ�Ƿ�Ϊ��
ע��:

��ֻ��ʹ�ö��еĻ�������-- Ҳ����?push to back, peek/pop from front, size, ��?is empty?��Щ�����ǺϷ��ġ�
����ʹ�õ�����Ҳ��֧�ֶ��С�?�����ʹ�� list ���� deque��˫�˶��У���ģ��һ������?, ֻҪ�Ǳ�׼�Ķ��в������ɡ�
����Լ������в���������Ч�ģ�����, ��һ���յ�ջ������� pop ���� top ��������

'''

from collections import deque
'''
�������⣬ֻ��ʹ�ö��еĻ�������-- Ҳ���� push to back, peek/pop from front, size, �� is empty ��Щ�����ǺϷ��ġ�
'''


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # �����趨������  ���� ��ģ��ջ   ��  һ������ ���� һ��������
        # ��Ϊʹ�ö��У�����ֻ��ʹ�ö��е� append  �� popleft����[0]���Ƚ��ȳ���ͨ����������ʵ�� ջ��
        self.queue1 = deque()  # in
        self.queue2 = deque()  # out

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        #  ѹջ����ʱ��ֱ�ӷ��뼴��
        self.queue1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        ����ʵ��  pop����ջ����
        """
        #  ���Ƚ���Ϊ���б�
        assert not self.empty(), 'Empty stack!'

        # ��һ��  �����Ͻ�que1��Ԫ�ط��õ�  que2��ȥ����������һ��
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        # �ڶ�������Ϊ ��������Ҫ ���һ���ŵ����еģ� ����que1 �����һ��ʣ�µ� ���Ƿ�����˼�ġ�
        ret = self.queue1.popleft()
        # �����������ж��������ϵĹ�λ����queue1 ʼ����Ϊ���ĺ���
        self.queue1, self.queue2 = self.queue2, self.queue1

        # ����ȡ ����ֵ���㶨
        return ret

    def top(self):
        """
        Get the top element.
        :rtype: int

        ��ȡջ��Ԫ��

        ��ȡ�Ѷ����þ��� popʱ��Ĳ���һ�����ҵ��������Ǹ�
        """
        #  ��ȡ��������Ϣ������������Ϊ�Ƕ��У����Ա���ʹ�ö���ר�ŵĲ���
        assert not self.empty(), 'Empty stack!'

        # ����  �� ����
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        #  ��queue1�����һ������ʾ���һ��������е�Ԫ�أ�Ҳ����ջ��Ҫ�����ġ�  ��������ʵ�Ѿ������ Ŀ�꣩
        ret = self.queue1[0]

        # ����һЩ��ԭ������  ���Ȱѻ�ȡ����topҲ�÷ŵ�que2�У������������� ��ɱ���queue1.
        self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

        return ret

    def empty(self):
        """
        Returns whether the stack is empty.     ȫ��ʱΪ��
        :rtype: bool
        """
        #  ����ͬʱ û�ˣ��Ϳ���
        return len(self.queue1) == 0 and len(self.queue2) == 0


#___________________________________    ��ϰ1   ______________________________#
# ʹ��  �������� ��ʵ��һ��ջ��������Ҫ����������  ֻ��ʹ�ö����е�queue[0]  ��ȡ���Ƚ��ĺ�  append������   �Ƚ��鷳�Ļ���ģ�µ�pop��top����
class MyStack1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # �����趨������  ���� ��ģ��ջ   ��  һ������ ���� һ��������
        # ��Ϊʹ�ö��У�����ֻ��ʹ�ö��е� append  �� popleft����[0]���Ƚ��ȳ���ͨ����������ʵ�� ջ��
        self.queue1 = deque()  # in
        self.queue2 = deque()  # out

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        #  ѹջ����ʱ��ֱ�ӷ��뼴��
        self.queue1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        ����ʵ��  pop����ջ����
        """
        #  ���Ƚ���Ϊ���б�
        assert not self.empty(), 'Empty stack!'

        # ��һ��  �����Ͻ�que1��Ԫ�ط��õ�  que2��ȥ����������һ��
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        # �ڶ�������Ϊ ��������Ҫ ���һ���ŵ����еģ� ����que1 �����һ��ʣ�µ� ���Ƿ�����˼�ġ�
        ret = self.queue1.popleft()
        # �����������ж��������ϵĹ�λ����queue1 ʼ����Ϊ���ĺ���
        self.queue1, self.queue2 = self.queue2, self.queue1

        # ����ȡ ����ֵ���㶨
        return ret

    def top(self):
        """
        Get the top element.
        :rtype: int

        ��ȡջ��Ԫ��

        ��ȡ�Ѷ����þ��� popʱ��Ĳ���һ�����ҵ��������Ǹ���

        �������pop����Ҫ����һ������С������.....
        """
        #  ��ȡ��������Ϣ������������Ϊ�Ƕ��У����Ա���ʹ�ö���ר�ŵĲ���
        assert not self.empty(), 'Empty stack!'

        # 1.����  �� ����
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        #  2.��queue1�����һ������ʾ���һ��������е�Ԫ�أ�Ҳ����ջ��Ҫ�����ġ�  ��������ʵ�Ѿ������ Ŀ�꣩
        ret = self.queue1[0]

        # 3.����һЩ��ԭ������  ���Ȱѻ�ȡ����topҲ�÷ŵ�que2�У������������� ��ɱ���queue1.
        self.queue2.append(self.queue1.popleft())
        # 4.��ԭ����
        self.queue1, self.queue2 = self.queue2, self.queue1

        return ret

    def empty(self):
        """
        Returns whether the stack is empty.     ȫ��ʱΪ��
        :rtype: bool
        """
        #  ����ͬʱ û�ˣ��Ϳ���
        return len(self.queue1) == 0 and len(self.queue2) == 0


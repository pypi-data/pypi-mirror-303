'''

    ��Ŀ���ڸ����������У�ÿ����Ԫ���������������ֵ֮һ��

            ֵ?0?����յ�Ԫ��
            ֵ?1?�����������ӣ�
            ֵ?2?�����õ����ӡ�
            ÿ���ӣ��κ��븯�õ����ӣ��� 4 ���������ϣ����ڵ��������Ӷ��ḯ�á�

            ����ֱ����Ԫ����û����������Ϊֹ�����뾭������С����������������ܣ�����?-1��

                 ���룺[[2,1,1],[1,1,0],[0,1,1]]
                 �����4



'''

#  �ⷨһ�� �ǳ�ֱ�۵�˼·������ʱ���ܵ�̫����
#   ˼·�ǳ�ֱ�ӣ�  ����  ���б�� �ʹ��������������н����޸ĺ͵����������жನ�Ĵ�����ֱ�� û�����ӱ仵Ϊֹ��
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        bad_list = []
        good_list = []
        #   �ҵ����л����ӵ� ���꣬����Ǻ�����
        for l, item in enumerate(grid):
            # ��ÿ�����ӣ����ձ�ţ����и���
            for g, oringe in enumerate(item):
                # �����ǰ�  �����ӵ�   ���긽�ӹ�ȥ��
                if oringe == 2:
                    bad_list.append((l, g))
                elif oringe == 1:
                    good_list.append((l, g))

        # �趨�߽硣  �ֱ��ǳ��� �� ��������߽�
        max_l = l
        max_g = g
        step = 0
        # ����ͳ��      �������ڿ�ʼ���ж�δ������������ٴ��ܹ������еĺ����Ӷ��仵��
        while good_list:

            #  �Է����仯����Ϣ��ͳ��
            change_flag = False
            change_list = []

            # ������.   �����ռ������ܹ����� �ı�ļٶ�λ��
            for l, g in bad_list:
                if l - 1 >= 0:
                    change_list.append((l - 1, g))
                if l + 1 <= max_l:
                    change_list.append((l + 1, g))
                if g - 1 >= 0:
                    change_list.append((l, g - 1))
                if g + 1 <= max_g:
                    change_list.append((l, g + 1))
            # ���� Ԥ�ٶ���λ�ã�������ʽ�������ĵ�  ����
            for chang in change_list:
                if chang in good_list:
                    #  ���ӱ仵��,  �����趨
                    bad_list.append(chang)
                    good_list.remove(chang)
                    change_flag = True

            step += 1

            #   ��ֹ���������ᴫ��ʱ
            if not change_flag:
                break

        # ���ڻ��кõ��б�˵��������
        if good_list:
            return -1
        else:
            return step

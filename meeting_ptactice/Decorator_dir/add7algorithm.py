# encoding:utf-8
'''
题目：要求键盘输入两个七进制【0-6】数，以空格分开，计算两者之和输出，例如：
输入：16 1
输出：20
'''

def add7Opration(m_list,n_list):
    # 加数和被加数补齐，防止数组越界，短者高位补0
    if len(m_list) > len(n_list):
        result = [''] * (len(m_list) + 1)  # 保存和，多一位是防止最高位也有进一的情况
        n_list = n_list + [0] * (len(m_list) - len(n_list))
    else:
        result = [''] * (len(n_list) + 1)
        m_list = m_list + [0] * (len(n_list) - len(m_list))

    flag = False
    for i in range(max(len(m_list), len(n_list))):
        if flag:  # 如果上一位有进1，本位和需要加上上一位进的1
            plus = int(n_list[i]) + int(m_list[i]) + 1
        else:
            plus = int(n_list[i]) + int(m_list[i])

        if plus >= 7:  # 本位大于7，本位存本位和-7，并向前进一
            result[i] = str(plus - 7)
            flag = True
        else:
            result[i] = str(plus)
            flag = False
    if flag:  # 最高位最终向前进1，和也需要向前进1
        result[-1] = str(1)
    result.reverse()
    print(''.join(result).strip())
    return result



if __name__ == '__main__':
    m,n = map(str,input('请输入2个7进制数，用空格隔开：').strip().split(' '))
    m_list,n_list = list(m),list(n)
    m_list.reverse()    # 翻转，方便从个位开始加
    n_list.reverse()
    print('7进制运算结果是：',add7Opration(m_list,n_list))

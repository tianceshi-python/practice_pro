# encoding:utf-8

def count_subNum(str):
    #list1 = list(str)
    count = {}
    for i in str:
        count[i] = str.count(i)

    return count


if __name__ == '__main__':
    str = 'yuijhgtyyiijhgyyuuh'
    print(count_subNum(str))


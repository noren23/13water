import time


class Card:
    def __init__(self, f, n):
        self.flower = f
        self.num = n


poker_1 = [Card(0, 0) for i in range(14)]
poker_2 = [Card(0, 0) for j in range(14)]
poker_3 = [Card(0, 0) for k in range(14)]
ans_1 = [Card(0, 0) for l in range(20)]
ans_2 = [Card(0, 0) for m in range(20)]
ans_3 = [Card(0, 0) for n in range(20)]
temp_1 = [Card(0, 0) for o in range(20)]
temp_2 = [Card(0, 0) for p in range(20)]
temp_3 = [Card(0, 0) for q in range(20)]
end_1 = [Card(0, 0) for r in range(20)]
end_2 = [Card(0, 0) for s in range(20)]
end_3 = [Card(0, 0) for t in range(20)]
s1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
r1 = 5
r2 = 5
r3 = 3
end_ans = 0

hua = [0, 0, 0, 0, 0, 0]
number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def init_cnt():
    for i in range(0, 6):
        hua[i] = 0
    for i in range(0, 20):
        number[i] = 0


def bubble_sort(nums, a, b):
    for i in range(b - a):
        for j in range(b - a - 1):
            if nums[a + j].num > nums[a + j + 1].num:
                nums[a + j], nums[a + j + 1] = nums[a + j + 1], nums[a + j]
    return nums


def ShunZi3(start):
    for i in range(start, start + 3):
        if number[i] < 1:
            return 0
    else:
        return 1


def ShunZi5(start):
    for i in range(start, start + 5):
        if number[i] < 1:
            return 0
    else:
        return 1


def first():
    init_cnt()
    bubble_sort(ans_3, 1, 3)
    for i in range(1, 4):
        hua[ans_3[i].flower] = hua[ans_3[i].flower] + 1
        number[ans_3[i].num] = number[ans_3[i].num] + 1
    for i in range(1, 5):
        if hua[i] == 3:
            if ShunZi3(ans_3[1].num) == 1:
                return 10
    for i in range(1, 5):
        if hua[i] == 3:
            return 7
    if ShunZi3(ans_3[1].num) == 1:
        return 6
    for i in range(4, 1, -1):
        if number[ans_3[i].num] == 3:
            return 5
    for i in range(4, 1, -1):
        if number[ans_3[i].num] == 2:
            return 2
    else:
        return 1


def second():
    init_cnt()
    bubble_sort(ans_2, 1, 5)
    for i in range(1, 6):
        hua[ans_2[i].flower] = hua[ans_2[i].flower] + 1
        number[ans_2[i].num] = number[ans_2[i].num] + 1
    for i in range(1, 5):
        if hua[i] == 5:
            if ShunZi5(ans_2[1].num) == 1:
                return 10
    for i in range(6, 1, -1):
        if number[ans_2[i].num] == 4:
            return 9
    for i in range(6, 1, -1):
        if number[ans_2[i].num] == 3:
            for j in range(6, 1, -1):
                if number[ans_2[j].num] == 2:
                    return 8
    for i in range(1, 5):
        if hua[i] == 5:
            return 7
    if ShunZi5(ans_2[1].num) == 1:
        return 6
    for i in range(6, 1, -1):
        if number[ans_2[i].num] == 3:
            for j in range(6, 1, -1):
                if number[ans_2[j].num] == 1:
                    return 5
    for i in range(6, 1, -1):
        if number[ans_2[i].num] == 2:
            for j in range(6, 1, -1):
                if (ans_2[i].num != ans_2[j].num) and \
                        number[ans_2[j].num] == 2 and abs(ans_2[i].num - ans_2[j].num) == 1:
                    return 4
    for i in range(6, 1, -1):
        if number[ans_2[i].num] == 2:
            for j in range(6, 1, -1):
                if (ans_2[i].num != ans_2[j].num) and number[ans_2[j].num] == 2:
                    return 3
    for i in range(6, 1, -1):
        if number[ans_2[i].num] == 2:
            return 2
    else:
        return 1


def third():
    init_cnt()
    bubble_sort(ans_2, 1, 5)
    for i in range(1, 6):
        hua[ans_1[i].flower] = hua[ans_1[i].flower] + 1
        number[ans_1[i].num] = number[ans_1[i].num] + 1
    for i in range(1, 6):
        if hua[i] == 5:
            if ShunZi5(ans_1[1].num) == 1:
                return 10
    for i in range(6, 1, -1):
        if number[ans_1[i].num] == 4:
            return 9
    for i in range(6, 1, -1):
        if number[ans_1[i].num] == 3:
            for j in range(6, 1, -1):
                if number[ans_1[j].num] == 2:
                    return 8
    for i in range(1, 5):
        if hua[i] == 5:
            return 7
    if ShunZi5(ans_1[1].num) == 1:
        return 6
    for i in range(6, 1, -1):
        if number[ans_1[i].num] == 3:
            for j in range(6, 1, -1):
                if number[ans_1[j].num] == 1:
                    return 5
    for i in range(6, 1, -1):
        if number[ans_1[i].num] == 2:
            for j in range(6, 1, -1):
                if (ans_1[i].num != ans_1[j].num) and \
                        number[ans_1[j].num] == 2 and abs(ans_1[i].num - ans_2[j].num) == 1:
                    return 4
    for i in range(6, 1, -1):
        if number[ans_1[i].num] == 2:
            for j in range(6, 1, -1):
                if (ans_1[i].num != ans_1[j].num) and number[ans_1[j].num] == 2:
                    return 3
    for i in range(6, 1, -1):
        if number[ans_1[i].num] == 2:
            return 2
    else:
        return 1


def StandOf():
    for i in range(1, 4):
        end_3[i] = ans_3[i]
    for i in range(1, 6):
        end_2[i] = ans_2[i]
    for i in range(1, 6):
        end_1[i] = ans_1[i]


def TempoF():
    for i in range(1, 4):
        ans_3[i] = temp_3[i]
    for i in range(1, 6):
        ans_2[i] = temp_2[i]
    for i in range(1, 6):
        ans_1[i] = temp_1[i]


def Print():
    for i in range(1, 4):
        if i == 3:
            print(ans_3[i].num)
        else:
            print(ans_3[i].num, end=" ")
    for i in range(1, 6):
        if i == 5:
            print(ans_2[i].num)
        else:
            print(ans_2[i].num, end=" ")
    for i in range(1, 6):
        if i == 5:
            print(ans_1[i].num)
        else:
            print(ans_1[i].num, end=" ")


def contrast_ans():
    global end_ans
    TempoF()
    k1 = first()
    k2 = second()
    k3 = third()
    score = k1 + k2 + k3
    if k1 > k2 or k2 > k3 or k1 > k3:
        score = 0
    if score > end_ans:
        end_ans = score
        StandOf()


def init_2():
    index = 0
    for i in range(1, 9):
        if s2[i] == 0:
            index = index + 1
            temp_3[index] = poker_2[i]


def dfs_2(d, index_2):
    for i in range(d, 9):
        temp_2[index_2] = poker_2[i]
        s2[i] = 1
        if index_2 == r2:
            init_2()
            contrast_ans()
        else:
            dfs_2(i + 1, index_2 + 1)
        s2[i] = 0


def init_1():
    index = 0
    for i in range(1, 14):
        if s1[i] == 0:
            index = index+1
            poker_2[index] = poker_1[i]


def dfs_1(d, index_1):
    for i in range(d, 14):
        s1[i] = 1
        temp_1[index_1] = poker_1[i]
        if index_1 == r1:
            init_1()
            dfs_2(1, 1)
        else:
            dfs_1(i + 1, index_1 + 1)
        s1[i] = 0


def number_to_hua(x):
    if x == 1:
        return '&'
    if x == 2:
        return '$'
    if x == 3:
        return '#'
    if x == 4:
        return '*'


def hua_to_number(x):
    if x == '&':
        return 1
    if x == '$':
        return 2
    if x == '#':
        return 3
    if x == '*':
        return 4


def main():
    tic = time.time()
    poker_1[1] = Card(2, 2)
    poker_1[2] = Card(3, 2)
    poker_1[3] = Card(4, 2)
    poker_1[4] = Card(1, 3)
    poker_1[5] = Card(1, 4)
    poker_1[6] = Card(4, 5)
    poker_1[7] = Card(1, 6)
    poker_1[8] = Card(1, 7)
    poker_1[9] = Card(2, 9)
    poker_1[10] = Card(3, 8)
    poker_1[11] = Card(4, 4)
    poker_1[12] = Card(4, 8)
    poker_1[13] = Card(3, 5)
    dfs_1(1, 1)
    for i in range(1, 4):
        if i != 3:
            print(number_to_hua(end_3[i].flower), end="")
            print(end_3[i].num, end=" ")
        else:
            print(number_to_hua(end_3[i].flower), end="")
            print(end_3[i].num)
    for i in range(1, 6):
        if i != 5:
            print(number_to_hua(end_2[i].flower), end="")
            print(end_2[i].num, end=" ")
        else:
            print(number_to_hua(end_2[i].flower), end="")
            print(end_2[i].num)
    for i in range(1, 6):
        if i != 5:
            print(number_to_hua(end_1[i].flower), end="")
            print(end_1[i].num, end=" ")
        else:
            print(number_to_hua(end_1[i].flower), end="")
            print(end_1[i].num)
    toc = time.time()
    print(toc-tic)


if __name__ == '__main__':
    main()

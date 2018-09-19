import random
import matplotlib.pyplot as plt


def create_data():
    """创建数据
    """
    up_li = list()
    down_li = list()
    for i in range(10000):
        x = random.randrange(0, 100)
        y = random.randrange(0, 100)
        if x > y:
            up_li.append([x, y, 'up'])
        if x < y:
            down_li.append([x, y, 'down'])
    up_li = up_li[:1000]
    down_li = down_li[:1000]
    print(up_li)
    print(down_li)
    plt.scatter([i[0] for i in up_li], [i[1] for i in up_li], color='b')  # s为size，按每个点的坐标绘制，alpha为透明度
    plt.scatter([i[0] for i in down_li], [i[1] for i in down_li], color='r')  # s为size，按每个点的坐标绘制，alpha为透明度
    plt.plot([i / 10 for i in range(1000)], [i / 10 for i in range(1000)], color='g')
    # plt.show()
    return up_li, down_li


def split_data(a, b):
    """切分数据"""
    li = list()
    for i in a:
        li.append(i)
    for j in b:
        li.append(j)
    random.shuffle(li)
    train_data = li[:int(len(li) * 0.8)]
    test_data = li[int(len(li) * 0.8):]
    print(len(train_data))
    print(len(test_data))
    # for i in test_data:
    #     print(i)
    return train_data, test_data


def calculate_neighbor_precision(train_data, test_data, K=3):
    """计算20%的数据在80%的上面分类预测的精度有多少
    """
    num = len(test_data)
    right_num = 0
    # 计算测试集的数据分别于训练集的数据里的每个数据的距离
    for test in test_data:
        distance_li = list()
        label = test[2]
        # print(label)
        for train in train_data:
            distance = ((test[0] - train[0]) ** 2 + (test[1] - train[1]) ** 2) ** 0.5
            distance_li.append((distance, train))

        # 排序，获取最小的K个点，并判断其分类
        distance_li = sorted(distance_li, key=lambda x: x[0])

        predict_label = [i[1][2] for i in distance_li[:K]]
        # print(predict_label)

        k_num = predict_label.count(label)

        if k_num >= (int(K / 2) + 1):
            right_num += 1

    precision = right_num / num
    print(precision)


def simple_predict(train_data, predict_li):
    distance_li = list()
    for train in train_data:
        distance = ((predict_li[0] - train[0]) ** 2 + (predict_li[1] - train[1]) ** 2) ** 0.5
        distance_li.append((distance, train))

    # 排序，获取最小的K个点，并判断其分类
    distance_li = sorted(distance_li, key=lambda x: x[0])
    predict_label = [i[1][2] for i in distance_li[:K]]
    down_num = predict_label.count('down')
    up_num = predict_label.count('up')
    if down_num > up_num:
        print('down')
    else:
        print('up')


if __name__ == '__main__':
    # predict_li: 测试点
    predict_li = [12, 13]
    K = 5
    a, b = create_data()
    data_train, data_test = split_data(a, b)
    calculate_neighbor_precision(data_train, data_test, K)
    simple_predict(data_train, predict_li)

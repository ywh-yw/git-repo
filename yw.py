def fibonacci_loop(n):
    # 处理 n 为 0 的情况
    if n == 0:
        return []
    # 处理 n 为 1 的情况
    if n == 1:
        return [0]
    # 初始化前两项
    sequence = [0, 1]
    # 循环生成后续的项
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence

# 测试
n = 10
print(fibonacci_loop(n))
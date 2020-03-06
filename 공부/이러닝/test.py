# def max_profit(stock_list):
#     result = -1000000000
#     tmp = []
#     for i in range(1, 6):
#         tmp = stock_list
#         minV = min(tmp[:i-1])
#         if stock_list[i] - minV >= result:
#             result = stock_list[i] - minV
#     return result
tmp = [7, 2, 5, 3, 1, 0]
print(min(tmp[:3]))

# 테스트
# print(max_profit([7, 1, 5, 3, 6, 4]))
data = open('data.txt', 'r')
input_list = data.read().split(',')
data.close()

input_list = [int(x) for x in input_list]
day = 80
dp = [0 for i in range(0,9)]
for i in range(0, len(input_list)):
    dp[input_list[i]] += 1
while day > 0:
    new_dp = [0 for i in range(0,9)]
    for i in range(0,8):
        new_dp[i] = dp[i+1]
    
    count = dp[0]
    new_dp[6] += count
    new_dp[8] += count
    dp = new_dp
    ans = sum(x for x in new_dp)
    day -= 1
print(ans)


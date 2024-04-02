short_ipv6 = input()

# 0으로만 이루어진 그룹 생략 -> 1개만 생략하면 : 이 8개 (원래 7 +1)
if short_ipv6.count(":") == 8:
    changed_ipv6 = short_ipv6.replace("::", ":")
else:
    changed_ipv6 = short_ipv6.replace("::", (7 - short_ipv6.count(":")) * ":" + "::")

ipv6_list = changed_ipv6.split(":")

# 생략된 0 넣어주기
for i in range(len(ipv6_list)):
    if len(ipv6_list[i]) < 4:
        ipv6_list[i] = (4 - len(ipv6_list[i])) * "0" + ipv6_list[i]

print(":".join(ipv6_list))
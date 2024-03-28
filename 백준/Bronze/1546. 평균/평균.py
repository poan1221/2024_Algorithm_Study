N = int(input())

score_list = list(map(int, input().split()))
max_score = max(score_list)
    
print(sum(score_list) / max_score * 100 / N)
A, B = input().split()

def reverse(n):
    reverse_n = int(str(n)[::-1])
    return reverse_n

print (reverse(A) if reverse(A) > reverse(B) else reverse(B))
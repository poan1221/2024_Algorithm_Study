function solution(rank, attendance) {
    const ranked = rank.map((r,i) => [r, i])
    .filter(([_, i]) => attendance[i])
    .sort((a, b) => a[0] - b[0])
    .slice(0, 3);
    
    const [a, b, c] = ranked.map(([_, i]) => i);
    
    return 10000 * a + 100 * b + c
    
}
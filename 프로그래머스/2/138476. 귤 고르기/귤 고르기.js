function solution(k, tangerine) {
    const count = new Map();
    for (const size of tangerine) {
        count.set(size, (count.get(size)||0) + 1);
    }
    
    const freq = Array.from(count.values()).sort((a,b) => b-a);
    
    let used = 0;
    let kinds = 0;
    for (const c of freq){
        used += c;
        kinds++;
        if (used >= k) return kinds;
    }
    
    return kinds;
}
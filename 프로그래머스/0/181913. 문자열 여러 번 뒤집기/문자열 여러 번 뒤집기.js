function solution(my_string, queries) {
    const str = [...my_string];
    
    for (const [s,e] of queries){
        const reversed = str.slice(s,e+1).reverse();
        str.splice(s, e - s+1, ...reversed);
    }
    
    return str.join('');
}
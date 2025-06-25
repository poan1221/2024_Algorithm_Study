function solution(my_strings, parts) {
    const strs = my_strings.map((str, i) => {
        const [s, e] = parts[i];
        return str.slice(s, e+1);
    })
    
    return strs.join('');
}
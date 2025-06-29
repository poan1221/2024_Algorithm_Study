function solution(my_string, is_suffix) {
    const suffix = [];
    for (let i = 0; i < my_string.length; i++){
        suffix.push(my_string.slice(i));
    }
    
    return suffix.includes(is_suffix) ? 1 : 0;
}
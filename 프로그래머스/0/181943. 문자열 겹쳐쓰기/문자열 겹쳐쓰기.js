function solution(my_string, overwrite_string, s) {
    const strLength = overwrite_string.length
    const newString = my_string.slice(0, s) + overwrite_string + my_string.slice(s + strLength);
    return newString;
}
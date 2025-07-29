function solution(strArr) {
    return strArr.map((_, i) => i % 2 != 0 ? strArr[i].toUpperCase() : strArr[i].toLowerCase());
}
function solution(num_list) {
    const length = num_list.length;
    const last = num_list[length- 1];
    const prev = num_list[length - 2];
    
    const addNum = last > prev ? last - prev : last * 2;
    
    return [...num_list, addNum];
}
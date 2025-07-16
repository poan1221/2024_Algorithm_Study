function solution(num_list) {
    let odd = 0;
    let even = 0;
    
    num_list.forEach((num, i) => {
        i % 2 === 0 ? odd += num : even += num;
    });
    
    return Math.max(odd, even);
}
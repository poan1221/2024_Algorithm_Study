function solution(myStr) {
    const cutted = myStr.split(/[abc]/).filter(s => s !== "");
    return cutted.length > 0 ? cutted : ["EMPTY"];
}
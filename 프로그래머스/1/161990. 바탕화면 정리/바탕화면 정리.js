function solution(wallpaper) {
    // var answer = [];
    // return answer;
    let lux = Infinity, luy = Infinity;
    let rdx = 0, rdy = 0;
    
    for (let i = 0; i < wallpaper.length; i++){
        for (let j = 0; j < wallpaper[i].length; j++){
            // 파일이 있는 좌표를 찾기
            if (wallpaper[i][j] === '#') {
                // 맞으면 드래그 위치를 위해 최소최대값을 구하기 - 격자점S 최소, 격자점 E 최대
                lux = Math.min(lux, i);
                luy = Math.min(luy, j);
                rdx = Math.max(rdx, i+1);
                rdy = Math.max(rdy, j+1);
            }
        }
    }
    
    return [lux, luy, rdx, rdy];
}
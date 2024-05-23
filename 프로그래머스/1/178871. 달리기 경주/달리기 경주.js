function solution(players, callings) {
    let idx;
    let name1;
    let name2;
    const idxList = {}
    
    // 선수의 초기 인덱스를 idxList에 저장
    players.forEach((name,index) => idxList[name] = index)
    
    for(let call of callings){
        idx = idxList[call]
        
        // 맨 앞의 선수가 호출된 경우 이동을 수행하지 않음
        if (idx === 0) continue;
        
        name1 = players[idx]
        name2 = players[idx - 1]
        
        // 인덱스 업데이트
        idxList[call] -= 1
        idxList[name2] += 1
        
        // 선수 위치 스왑
        players[idx] = name2
        players[idx-1] = name1
    }    

    return players;
}
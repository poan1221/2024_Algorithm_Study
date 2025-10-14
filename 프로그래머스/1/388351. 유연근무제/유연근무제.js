function solution(schedules, timelogs, startday) {
    const worker = schedules.length;
    
    const toMinutes = (time) => {
        const h = Math.floor(time/100);
        const m = time % 100;
        return h*60 + m;
    }
    
    const isWeekend = (day) => day === 6 | day === 7;
    
    let count = 0;
    
    for (let i = 0; i < worker; i++){
        const want = toMinutes(schedules[i]);
        const cutoff = want + 10;
        
        let ok = true;
        for (let d = 0; d < 7; d++){
            const day = ((startday - 1) + d) % 7 + 1;
            if (isWeekend(day)) continue;
            
            const arrive = toMinutes(timelogs[i][d]);
            if (arrive > cutoff){
                ok = false;
                break;
            }
        }
        if (ok) count ++;
    }
    return count;
}
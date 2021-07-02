function categoryChange(e){
    var push = ['선택','가슴','어깨'];
    var pull = ['선택','수직 당기기', '수평 당기기'];
    var leg = ['선택','프론트', '백'];
    var core = ['선택','전면','허리'];
    var arms = ['선택','이두','삼두']
    var target = document.getElementById('middle');

    if(e.value =='push') var class_middle = push;
    else if(e.value == 'pull') var class_middle = pull;
    else if (e.value == 'legs') var class_middle = leg;
    else if (e.value == 'core') var class_middle = core;
    else if (e.value == 'arms') var class_middle = arms;

    target.options.length=0;
    for (x in class_middle) {
        var opt = document.createElement("option");
        opt.value = class_middle[x];
        opt.innerHTML = class_middle[x];
        target.appendChild(opt);
    }
}
function categoryChange2(e){
    var chest = ['플랫벤치 프레스','체스트 프레스','인클라인 머신프레스','체스트 플라이','딥스'];
    var shoulder = ['오버헤드프레스','사레레','후면삼각근'];
    var vertical_pull = ['풀업','랫풀다운','내로우 랫풀다운'];
    var horizontal_pull = ['바벨로우','머신 로우', '데드리프트(등)','케이블 로우'];
    var triceps = ['트라이셉스 익스텐션']
    var biceps = ['바이셉 컬']
    var leg_front = ['스쿼트'];
    var leg_back = ['데드리프트','런지','글루트햄'];
    var core = ['드래곤 플래그']
    var target = document.getElementById('small'); 
    
    if(e.value == '가슴') var class_small = chest;
    else if(e.value == '어깨') var class_small = shoulder;
    else if(e.value == '수직 당기기') var class_small = vertical_pull;
    else if(e.value == '수평 당기기') var class_small = horizontal_pull;
    else if(e.value == '프론트') var class_small = leg_front;
    else if(e.value == '백') var class_small = leg_back;
    else if(e.value == '전면') var class_small = core;
    else if(e.value == '이두') var class_small = biceps;
    else if(e.value == '삼두') var class_small = triceps;

    target.options.length=0;
    for (x in class_small) {
        var opt = document.createElement("option");
        opt.value = class_small[x];
        opt.innerHTML = class_small[x];
        target.appendChild(opt);
    }
}

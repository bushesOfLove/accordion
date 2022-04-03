// this used to be used until it's not
document.addEventListener('DOMContentLoaded', () => {
    var el = document.getElementById('sprite');
    var C = new Audio('static/accordion/audio/C.m4a');
    document.addEventListener('keydown', function(e) {
        el.style.animationPlayState = 'running';
        
        if (e.keyCode == 65) {
            C.play();
            C.loop = true;
        }
        if (e.keyCode == 83) {
            var D = new Audio('static/accordion/audio/D.m4a');
            D.play();
        }
        if (e.keyCode == 68) {
            var E = new Audio('static/accordion/audio/E.m4a');
            E.play();
        }
        if (e.keyCode == 70) {
            var F = new Audio('static/accordion/audio/F.m4a');
            F.play();
        }
        if (e.keyCode == 71) {
            var G = new Audio('static/accordion/audio/G.m4a');
            G.play();
        }
        if (e.keyCode == 72) {
            var A = new Audio('static/accordion/audio/A.m4a');
            A.play();
        }
        if (e.keyCode == 74) {
            var B = new Audio('static/accordion/audio/B.m4a');
            B.play();
        }
        if (e.keyCode == 75) {
            var C8 = new Audio('static/accordion/audio/C8.m4a');
            C8.play();
        }
        if (e.keyCode == 86) {
            var fB = new Audio('static/accordion/audio/fB.m4a');
            fB.play();
        }
        if (e.keyCode == 67) {
            var fA = new Audio('static/accordion/audio/fA.m4a');
            fA.play();
        }
        if (e.keyCode == 88) {
            var fG = new Audio('static/accordion/audio/fG.m4a');
            fG.play();
        }
        if (e.keyCode == 90) {
            var fF = new Audio('static/accordion/audio/fF.m4a');
            fF.play();
        }
    });

    document.addEventListener('keyup', function(e) {
        el.style.animationPlayState = 'paused';
        C.pause;
        // C.currentTime = 0;
    });
});
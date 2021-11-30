//环境，项目，模块公用的函数
function find(yuan) {
     document.querySelector(yuan).onclick= function () {
         addWin.style.display = 'none';
     }
}
find("#close-but");
find(".cancel-but");
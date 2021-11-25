//点击模块，切换并查询相关数据返回
project(projects);
function project(h) {
    //查询数据并返回创建一个临时table

    //变量可以从base.js继承过来
    selected(h);
}
//点击新增项目，弹出输入框
document.querySelector(".add-button").onclick =function () {
    addWin.style.display = "block";
}

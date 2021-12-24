//common function
var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
// titles选中效果并默认查询全部数据显示
function selected(url, h) {
    //查询数据并返回创建一个临时table
    allData(url);
    //变量可以从base.js继承过来
    s(h);
}
function s(h) {
    h.style.fontSize="21px";
    h.style.backgroundColor='blue';
}
// 非异步，fetch，get函数并且前端自动跳转到后台返回的url页面
function getNotAjaxJump(url) {
    fetch(url,{
            method:"GET",
            headers:{"X-CSRFToken":token}
    })
        .then(data =>{
            console.log(data)
            window.location.href = data["url"];
        })
}
// 退出登录
// console.log("6666")
document.querySelector("#logout-but").onclick = function () {
    var logoUrl = "/logout/";
    getNotAjaxJump(logoUrl);
}
//取消和关闭新增的输入弹框
var addWin = document.querySelector(".add-win");

<!-- 查询全部数据的函数-->
function allData(url){
    //console.log("77777-1",url)
    fetch(url,{method:"GET",
        headers:{"X-CSRFToken":token, "X-Requested-With":"XMLHttpRequest"},
            })
        .then(response => response.json())
        .then(data => {
            //console.log(data);
            createList(data);
    })
        .catch((error)=>{
            console.error('Error:', error);
        })
}
//查询全部数据并创建数据列表
function createList(data) {
    var innerHTML= '';
    var envData = data["data"];
    for (let envs in data["data"]){
        let ds = envData[parseInt(envs)];
        let t = temp; //这里的赋值要保证每次循环数据的时候，t都是空的
        for ( let d in ds){
            t = t.split('{' + d + '}').join(ds[d]);
        }
        innerHTML += t;
    }
    document.querySelector('tbody').innerHTML = innerHTML;
}
//新增点击保存按钮
function Save(url, pas) {
    //console.log(url, pas)
    fetch(url,{
        method:"POST",
        headers:{"X-CSRFToken":token,"X-Requested-With":"XMLHttpRequest"},
        body:pas,
    })
    .then(response => response.json())
        .then(data=>{
            //console.log(data["code"])
            if ( data["code"] === "20010" || data["code"] === "20020"){
                //console.log("6666")
                addWin.style.display = 'none';
                allData(url)
            }
        })
}
//数据显示列表-删除请求
function Del(id, url){
    fetch(url,{
        method:"DELETE",
        headers:{"X-CSRFToken":token,"X-Requested-With":"XMLHttpRequest"},
        body:JSON.stringify({id: id}),
    })
    .then(response => response.json())
    .then(data => {
      //console.log('Success:', data);
      allData(url);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

// env配置
var envB= document.querySelector(".setting span");
document.querySelector(".setting").onclick = function(){
    //切换到主页，同时改变tab的属性
    window.location.href = '/home/';
};


//project项目
var projects = document.querySelector(".project span");
document.querySelector(".project").onclick = function () {
    // getNotAjaxJump(pro);会导致多次请求
    window.location.href = "/home/autotest/projects/";
    //刷新了页面之后，页面的所有临时的效果都会被清空
};

//模块
var mokuai = document.querySelector(".mokuai span");
document.querySelector(".mokuai").onclick = function () {
    window.location.href = "/home/autotest/mokuai/";
};
//用例
var caseUrl = "/home/autotest/case/";
var cases = document.querySelector(".case-list span");
document.querySelector(".case-list").onclick = function () {
    window.location.href = caseUrl;
};
//用例保存函数
function caseSave(data) {
    fetch(caseUrl,{
        method:'POST',
        headers:{"X-CSRFToken": token},
        body: data
    })
        .then(response => response.json())
        .then(data => {console.log("Success",data);
        // 请求成功需要返回查询列表？？
        if (data['code'] == '20010'){
            window.location.href = caseUrl;
        }

        }).catch((error) => {console.error('Error:', error);
        });
}
//编辑xx，获取当前的xx的数据
function EditSave(data) {
    //1.先获取现有的值；2、赋值编辑窗口；3.获取到现有修改后的值，保存（调用base中的caseSave）
    return fetch(location.pathname,{
        method:"POST",
        headers:{"X-CSRFToken":token},
        body:JSON.stringify(data)
    })
    .then(response => response.json())
        .then(data => {
            console.log("Success");
            return data;
        }).catch((error) => {
            console.error('Error:', error);
        });

}
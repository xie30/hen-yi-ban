//点击模块，切换并查询相关数据返回
var proUrl = "/home/autotest/projects/";
<!-- 点击查询项目配置 -->
var temp = `<tr class="pro-list-data">
    <td name="list-pro-id">{id}</td>
    <td name="list-pro-name">{name}</td>
    <td name="list-dec">{p_description}</td>
    <td name="list-tester">{p_tester}</td>
    <td name="list-creator">{p_creator}</td>
    <td name="list-ctime">{create_time}</td>
    <td name="list-uptime">{update_time}</td>
    <td class="list-op">
        <button class="edit">编辑</button>
        <button class="delete">删除</button></td>
    </tr>`;
selected(proUrl, projects);
//点击新增项目，弹出输入框
let name = document.querySelector("#pro-name");
let Description=document.querySelector("#pro-description");
let tester = document.querySelector("#tester");
let creator = document.querySelector("#creator");
document.querySelector(".add-button").onclick =function () {
    name.value='';
    Description.value='';
    tester.value='';
    creator.value='';
    addWin.style.display = "block";
    document.querySelector(".save-but").onclick = function () {
        let pas = JSON.stringify({pro_name:name.value, pro_description:Description.value,
        tester:tester.value, creator:creator.value});
        //console.log(pas)
        Save(proUrl,pas);
    }
}
//点击编辑和删除
var t =document.querySelector(".set-contents")
t.addEventListener("click",(event)=> {
    if (event.target.classList.contains("delete")) {
        let deEnv = event.target.parentNode.parentNode;
        let id = deEnv.querySelector("[name='list-pro-id']").innerText;
        Del(id,proUrl);
    }
    if (event.target.classList.contains("edit")) {
        proEditSave(event);
    }
})
function proEditSave(event) {
    let edEnv = event.target.parentNode.parentNode;
    let proId = edEnv.querySelector("[name='list-pro-id']").innerText
    let proName = edEnv.querySelector("[name='list-pro-name']").innerText;
    let proDec = edEnv.querySelector("[name='list-dec']").innerText;
    let proTester = edEnv.querySelector("[name='list-tester']").innerText;
    let proCreator = edEnv.querySelector("[name='list-creator']").innerText;
    addWin.style.display = 'block';
    name.value = proName;
    Description.value = proDec;
    tester.value = proTester;
    creator.value = proCreator;
    //新增的时候的save按钮也从这里执行了？
    // 可以自定义弹框的类型，然后把类型值传给(".env-save-but").onclick函数内部判断执行哪个方法/又或者两个触发事件都放到弹框触发的函数中
    document.querySelector(".save-but").onclick=function () {
        proOldSave(proId);
    }
}
function proOldSave(id) {
    let newName = name.value;
    let newDec = Description.value;
    let newTester = tester.value;
    let newCreator = creator.value;
    let params = JSON.stringify({id: id, pro_name: newName,pro_description: newDec,creator:newCreator,tester:newTester})
    Save(proUrl, params);
}
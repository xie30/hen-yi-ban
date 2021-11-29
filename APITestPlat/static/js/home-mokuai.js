//点击模块，切换并查询相关数据返回
var moUrl = "/home/autotest/mokuai/";
<!-- 点击查询项目配置 -->
var temp = `<tr class="mo-list-data">
    <td name="list-mo-id">{id}</td>
    <td name="list-mo-name">{name}</td>
    <td name="list-dec">{m_description}</td>
    <td name="list-pro">{m_pro}</td>
    <td name="list-tester">{m_tester}</td>
    <td name="list-creator">{m_creator}</td>
    <td name="list-ctime">{create_time}</td>
    <td name="list-uptime">{update_time}</td>
    <td class="list-op">
        <button class="edit">编辑</button>
        <button class="delete">删除</button></td>
    </tr>`;
selected(moUrl, mokuai);
// s(mokuai)
//新增
let name = document.querySelector("#mo_name");
let Description = document.querySelector("#m_description");
let tester = document.querySelector("#m_tester");
let creator = document.querySelector("#m_creator");
let proName = document.querySelector(".p_selected")
document.querySelector(".add-button").onclick =function () {
    name.value='';
    Description.value='';
    tester.value='';
    creator.value='';
    proName.value= '';
    addWin.style.display = "block";
    document.querySelector(".save-but").onclick = function () {
        let pas = JSON.stringify({m_name:name.value, m_description:Description.value,
        m_tester:tester.value, m_creator:creator.value, m_pro:proName.value});
        //console.log(pas)
        Save(moUrl,pas);
    }
}

//点击编辑和删除
var t =document.querySelector(".set-contents")
t.addEventListener("click",(event)=> {
    if (event.target.classList.contains("delete")) {
        let deEnv = event.target.parentNode.parentNode;
        let id = deEnv.querySelector("[name='list-mo-id']").innerText;
        Del(id,moUrl);
    }
    if (event.target.classList.contains("edit")) {
        moEditSave(event);
    }
})
function moEditSave(event) {
    let edEnv = event.target.parentNode.parentNode;
    let moId = edEnv.querySelector("[name='list-mo-id']").innerText
    let moName = edEnv.querySelector("[name='list-mo-name']").innerText;
    let moDec = edEnv.querySelector("[name='list-dec']").innerText;
    let moTester = edEnv.querySelector("[name='list-tester']").innerText;
    let moCreator = edEnv.querySelector("[name='list-creator']").innerText;
    let pro = edEnv.querySelector("[name='list-pro']").innerText;
    addWin.style.display = 'block';
    name.value = moName;
    Description.value = moDec;
    tester.value = moTester;
    creator.value = moCreator;
    proName.value = pro;
    //新增的时候的save按钮也从这里执行了？
    // 可以自定义弹框的类型，然后把类型值传给(".env-save-but").onclick函数内部判断执行哪个方法/又或者两个触发事件都放到弹框触发的函数中
    document.querySelector(".save-but").onclick=function () {
        moOldSave(moId);
    }
}
function moOldSave(id) {
    let newName = name.value;
    let newDec = Description.value;
    let newTester = tester.value;
    let newCreator = creator.value;
    let newPro = proName.value;
    let params = JSON.stringify({id: id, m_name: newName,m_description: newDec,m_creator:newCreator,
        m_tester:newTester,m_pro:newPro})
    Save(moUrl, params);
}
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
        m_tester:tester.value, m_creator:creator.value, m_proName:proName});
        //console.log(pas)
        Save(moUrl,pas);
    }
}
<!-- 访问home页面,默认查询env数据返回-->
const envUrl = "/home/autotest/env/"
selected(envUrl, envB);
<!-- 点击查询项目配置 -->
var temp = `<tr class="env-list-data">
    <td name="list-env-id">{id}</td>
    <td name="list-env-name">{name}</td>
    <td name="list-host">{host_url}</td>
    <td name="list-dec">{env_description}</td>
    <td name="list-ctime">{create_time}</td>
    <td name="list-uptime">{update_time}</td>
    <td class="list-op">
        <button class="env-edit">编辑</button>
        <button class="env-delete">删除</button></td>
    </tr>`;
//项目配置被选中效果
<!-- 公用函数 -->
<!-- 新增测试环境 -->
document.getElementsByClassName("add-button")[0].onclick = function(){
    // document.querySelector("#list-env-id").value='';
    document.querySelector("#env-name").value='';
    document.querySelector("#env-host").value='';
    document.querySelector("#env-description").value='';
    addWin.style.display = 'block';
    document.querySelector(".save-new-but").onclick=function () {
    newSave();
}
};
<!-- 保存,同时向后台发送请求保存数据 关闭弹框 -->
function newSave(){
    let name = document.querySelector("#env-name");
    let host = document.querySelector("#env-host");
    let dec = document.querySelector("#env-description");
    let pas = JSON.stringify({name:name.value, host_url: host.value, env_description: dec.value});
    let xttp = new XMLHttpRequest();
    xttp.open("POST","./autotest/env_add/",true);
    xttp.setRequestHeader("X-CSRFToken",token);
    xttp.setRequestHeader("X-Requested-With","XMLHttpRequest");
    xttp.send(pas)
    xttp.onreadystatechange =function () {
        if (this.readyState==4 && this.status == 200){
            name.value='';
            host.value='';
            dec.value='';
            addWin.style.display = 'none';
            allData(envUrl);
        }
        else{
            addWin.style.display = 'none';
        }
    }
}
// <!-- 如果要放在标签的写法 -->
//var temp= document.querySelector('tbody').innerHTML
// {#console.log(temp)#}
<!-- 编辑环境 -->
<!-- 删除环境-->

var t =document.querySelector(".set-contents")
t.addEventListener("click",(event)=> {
    if (event.target.classList.contains("env-delete")) {
        let deEnv = event.target.parentNode.parentNode;
        let na = deEnv.querySelector("[name='list-env-name']").innerText;
        envDel(na);
    }
    if (event.target.classList.contains("env-edit")) {
        editSave(event);
    }
})
function editSave(event) {
    let edEnv = event.target.parentNode.parentNode;
    let ids = edEnv.querySelector("[name='list-env-id']").innerText
    let name = edEnv.querySelector("[name='list-env-name']").innerText;
    let host = edEnv.querySelector("[name='list-host']").innerText;
    let dec = edEnv.querySelector("[name='list-dec']").innerText;
    ne.style.display = 'block';
    document.querySelector("#env-name").value = name;
    document.querySelector("#env-host").value = host;
    document.querySelector("#env-description").value = dec;
    //新增的时候的save按钮也从这里执行了？
    // 可以自定义弹框的类型，然后把类型值传给(".env-save-but").onclick函数内部判断执行哪个方法/又或者两个触发事件都放到弹框触发的函数中
    document.querySelector(".env-save-but").onclick=function () {
        oldSave(ids);
}
}
function oldSave(ids) {
        let newName = document.querySelector("#env-name").value;
        let newHost = document.querySelector("#env-host").value;
        let newDecs = document.querySelector("#env-description").value;
        fetch("./autotest/env_modify/",
            {method: "POST", headers: {"X-CSRFToken": token, "X-Requested-With": "XMLHttpRequest"},
                body: JSON.stringify({id: ids, name: newName, host_url: newHost, env_description: newDecs})
        })
            .then(response => response.json())
            .then(data => {console.log("Success",data);
        addWin.style.display = 'none';
        allData(envUrl);
        }).catch((error) => {console.error('Error:', error);
        });
 }

function envDel(name){
    fetch("./autotest/env_delete/",{
        method:"DELETE",
        headers:{"X-CSRFToken":token,"X-Requested-With":"XMLHttpRequest"},
        body:JSON.stringify({name: name}),
    })
    .then(response => response.json())
    .then(data => {
      //console.log('Success:', data);
      allData(envUrl);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


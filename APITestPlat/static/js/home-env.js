
<!-- 访问home页面,默认查询env数据返回-->
reqEnv();
//项目配置被选中效果
<!-- 公用函数 -->
<!-- 新增册数环境 -->
var ne = document.querySelector(".add-env");
document.getElementsByClassName("add-button")[0].onclick = function(){
    // document.querySelector("#list-env-id").value='';
    document.querySelector("#env-name").value='';
    document.querySelector("#env-host").value='';
    document.querySelector("#env-description").value='';
    ne.style.display = 'block';
    document.querySelector(".env-save-but").onclick=function () {
    nawSave();
}

};
<!-- 取消和关闭新增的输入弹框 -->
 function find(yuan) {
     document.querySelector(yuan).onclick= function () {
         ne.style.display = 'none';
     }
 }
find("#close-but");
find("#env-cancel");
<!-- 保存,同时向后台发送请求保存数据 关闭弹框 -->
var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

function nawSave(){
    let name = document.querySelector("#env-name");
    let host = document.querySelector("#env-host");
    let dec = document.querySelector("#env-description");
    let pas = JSON.stringify({"name":name.value, "host_url": host.value, "env_description": dec.value});
    let xttp = new XMLHttpRequest();
    xttp.open("POST","./autotest/env_add/",true);
    xttp.setRequestHeader("X-CSRFToken",token);
    xttp.setRequestHeader("X-Requested-With","XMLHttpRequest");
    xttp.send(pas)
    xttp.onreadystatechange =function () {
        if (this.readyState==4 && this.status == 200){
            //console.log("新增成功")
            name.value='';
            host.value='';
            dec.value='';
            ne.style.display = 'none';
            reqEnv();
        }
        else{
            ne.style.display = 'none';
        }
    }
}
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
    </tr>`
// <!-- 如果要放在标签的写法 -->
//var temp= document.querySelector('tbody').innerHTML
// {#console.log(temp)#}
document.querySelector(".setting").onclick = function(){
    reqEnv();
}

<!-- 请求环境配置查询的函数-->
function reqEnv(){
    let envttp = new XMLHttpRequest();
    //每当 readyState 发生变化时就会调用 onreadystatechange 函数,所以判断条件需要this.readyState==4
    envttp.onreadystatechange=function () {
        if (this.readyState==4 && this.status==200){
            //console.log(envttp.responseText)
            var innerHTML= '';
            data = JSON.parse(envttp.responseText);
            envdata = data["data"];
            for (let envs in envdata){
                //console.log(envs,typeof envs);
                ds = envdata[parseInt(envs)];
                var t = temp; //这里的赋值要保证每次循环数据的时候，t都是空的
                    for (d in ds){
                        t = t.split('{' + d + '}').join(ds[d]);
                    }
                innerHTML += t;
                }
            }
            document.querySelector('tbody').innerHTML = innerHTML;
        };
    envttp.open("GET", "./autotest/env/", true);
    envttp.setRequestHeader("X-CSRFToken",token);
    envttp.setRequestHeader("X-Requested-With","XMLHttpRequest");
    envttp.send();
}
<!-- 编辑环境 -->
<!-- 删除环境-->

var t =document.querySelector(".set-contents")
t.addEventListener("click",(event)=> {
    if (event.target.classList.contains("env-delete")) {
        let deenv = event.target.parentNode.parentNode;
        let na = deenv.querySelector("[name='list-env-name']").innerText;
        envDel(na);
    }
    if (event.target.classList.contains("env-edit")) {
        console.log("1111")
        editSave(event);
    }
})
function editSave(event) {
    let deenv = event.target.parentNode.parentNode;
    let ids = deenv.querySelector("[name='list-env-id']").innerText
    // console.log("22222")
    let name = deenv.querySelector("[name='list-env-name']").innerText;
    let host = deenv.querySelector("[name='list-host']").innerText;
    let dec = deenv.querySelector("[name='list-dec']").innerText;
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
        let newname = document.querySelector("#env-name").value;
        let newhost = document.querySelector("#env-host").value;
        let newdecs = document.querySelector("#env-description").value;
        fetch("./autotest/env_modify/",
            {method: "POST", headers: {"X-CSRFToken": token, "X-Requested-With": "XMLHttpRequest"},
                body: JSON.stringify({id: ids, name: newname, host_url: newhost, env_description: newdecs})
        })
            .then(response => response.json())
            .then(data => {console.log("Success",data);
        ne.style.display = 'none';
        reqEnv();
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
      console.log('Success:', data);
      reqEnv();
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

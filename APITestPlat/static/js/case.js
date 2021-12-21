let editCaseUrl= "/home/autotest/edit_case/";
let runCaseUrl= "/home/autotest/runcase/";
//点击模块，切换并查询相关数据返回
var temp = `<tr class="pro-list-data">
    <td name="list-case-id">{id}</td>
    <td name="list-case-name">{name}</td>
    <td name="list-project">{pros}</td>
    <td name="list-mokuai">{mokuais}</td>
<!--    <td name="list-tester">{tester}</td>-->
    <td name="list-creator">{creator}</td>
    <td name="list-ctime">{create_time}</td>
    <td name="list-uptime">{update_time}</td>
    <td class="list-op">
        <button class="edit">编辑</button>
        <button class="delete">删除</button>
        <button class="run-case">运行</button>
        </td>
    </tr>`;
selected(caseUrl, cases);


//新增用例
document.querySelector(".add-button").onclick = function () {
    window.location.href = editCaseUrl;
}

//点击编辑、删除、运行按钮
// var run_but = document.querySelector(".run-case")
var case_but =document.querySelector(".set-contents")
case_but.addEventListener("click",(event)=> {
    if (event.target.classList.contains("delete")) {
        let deEnv = event.target.parentNode.parentNode;
        let id = deEnv.querySelector("[name='list-case-id']").innerText;
        Del(id, caseUrl);
    }
    if (event.target.classList.contains("edit")) {
        caseEditSave(event);
    }
    if (event.target.classList.contains("run-case")) {
        caseRun(event);
    }
})

function caseEditSave(event) {
    //1.先获取现有的值；2、赋值编辑窗口；3.获取到现有修改后的值，保存（调用base中的caseSave）
    window.location.href = editCaseUrl
}
//运行用例
function caseRun(event) {
    let deCase = event.target.parentNode.parentNode;
    let id = deCase.querySelector("[name='list-case-id']").innerText;
    fetch(runCaseUrl,{
        method:'POST',
        headers:{"X-CSRFToken":token,"X-Requested-With":"XMLHttpRequest"},
        body:JSON.stringify({id: id})
    })
       .then(response => response.json())
        .then(data => {console.log("Success",data);
        //
        }).catch((error) => {console.error('Error:', error);
        });

}


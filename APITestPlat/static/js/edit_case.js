//用例，点击保存按钮
case_url = ""
var save = document.querySelector("#ase-save")
save.onclick = function () {
    datas=JSON.stringify({})
    save(datas)
}

function save(datas) {
    fetch(case_url,{
        method:'GET',
        headers:{},
        body: datas

    })
}


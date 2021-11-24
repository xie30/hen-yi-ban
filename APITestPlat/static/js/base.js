// 相当于一个公用的js
// env配置
var envco= document.querySelector(".setting span")
document.querySelector(".setting").onclick = function(){
    //同时改变tab的属性
    envco.style.fontSize="21px";
    envco.style.backgroundColor='blue';
    reqEnv();
};
<!-- 请求环境配置查询的函数-->
function reqEnv(){
    //console.log("11111")
    fetch("/home/autotest/env/",{method:"GET",
        headers:{"X-CSRFToken":token, "X-Requested-With":"XMLHttpRequest"},
            })
        .then(response => response.json())
        .then(data => {
            //console.log(data)
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
        //window.location.href=data['url']
    })
        .catch((error)=>{
            console.error('Error:', error);
        })
}

//project项目
var project = document.querySelector(".project")
var projects = document.querySelector(".project span")
var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
project.onclick = function () {
    console.log('ppp')
    projects.style.fontSize="21px";
    projects.style.backgroundColor='blue';
    // window.location.href = "/home/autotest/project/";
    //console.log("333")
    reqP();
}
function reqP() {
    fetch("/home/autotest/project/",{
            method:"GET",
            headers:{"X-CSRFToken":token}
    })
        .then(data =>{
            console.log(data)
            window.location.href = data["url"];
        })
}
let caseList = {name:"", url:"", params:"",creator:"",check_key:"",check_value:"",pros:"",mokuais:""};
let caseListSelect = {include:"", method:"",param_types:"",assert_type:''};
let caseHeader = {header_selected:"", re_header:{header_key:"",header_value:""}};
// const fillData = async () => {
//     //判断是编辑还是新增，编辑需要请求后台查询数据填充，新增不需要
//     let params = new URLSearchParams(document.location.search);
//     let case_id = params.get("id");
//     if (case_id){
//     const data =  await caseEditSave(case_id)
//     console.log(data)
//     }
// }
// 需要return 整个fetch
// 下面这里等同于上面的处理promise的方式，需要return data
let params = new URLSearchParams(document.location.search);
let case_id = params.get("id");
if (case_id){
    EditSave({id:case_id}).then((data) => {
        console.log(data);
        //给编辑页面赋值
        setValue(data,caseList)
        setOptionValue(data,caseListSelect);
        // setFor(caseHeader["re_header"],data);
    })
}
function setValue(data,list) {
    for (let it in list) {
        console.log(it, data[it])
        if (it !== "pros" && it !=="mokuais"){
            document.querySelector('#'+it).value=data[it]
        }else{
            setOptionValues(data,it)
        }
    }
}
function setOptionValue(data, list){
    for (let it in list) {
        setOptionValues(data, it)
        }
}
function setOptionValues(data, it){
    // console.log(it, data[it])
    let option = document.querySelector('#'+it)
    option.options[option.selectedIndex].value = data[it]
}
//用例，点击保存按钮
let saveBut = document.querySelector("#case-save");
let cancelBut = document.querySelector("#case-cancled");
saveBut.onclick = function () {
    caseHeader["header_selected"]= document.querySelector("#header_selected").checked
    for (let he in caseHeader["re_header"]){
        let heValue = queryValue("#" + he);
        caseHeader["re_header"][he] = heValue;
    }
    for (let ca in caseList){
        let caValue = queryValue("#" + ca);
        caseList[ca]= caValue;
    }
    for (let se in caseListSelect){
        let selectValue = queryOptionValue("#" + se);
        caseListSelect[se] = selectValue;
    }
    let newCaseList ={...caseList,...caseListSelect,...caseHeader};
    // console.log(newCaseList);
    // console.log(caseHeader);
    let data = JSON.stringify(newCaseList);
    caseSave(data);
};
function queryValue(att) {
    // console.log(att);
    // console.log(document.querySelector(att).value);
    return document.querySelector(att).value;
}
function queryOptionValue(att) {
    console.log(att)
    let option = document.querySelector(att);
    console.log(option)
    // ?.方法
    return option.options[option.selectedIndex]?.value||'';
}

cancelBut.onclick = function () {
    window.location.href=caseUrl;
}
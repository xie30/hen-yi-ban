//用例，点击保存按钮
case_url = "";
var saveBut = document.querySelector("#case-save");
var edit_list= document.querySelector(".edit-case-list");
saveBut.onclick = function () {
    let caseList = {name:"", url:"", params:"",creator:"",check_key:"",check_value:""};
    let caseListSelect = {include:"", methods:"",param_types:"",assert_type:''};
    let caseHeader = {header_selected:"", re_header:{header_key:"",header_value:""}};
    for (let ca in caseList){
        let caValue = queryValue("#" + ca);
        caseList[ca]= caValue;
    }
    for (let se in caseListSelect){
        let selectValue = queryOptionValue("#" + se);
        caseListSelect[selectValue] = selectValue;
    }
    let newCaseList = caseList + caseListSelect;
    console.log(newCaseList);
    let data = JSON.stringify(newCaseList);
    save(data);
};
function queryValue(att) {
    // console.log(att);
    // console.log(document.querySelector(att).value);
    return document.querySelector(att).value;
}
function queryOptionValue(att) {
    console.log(att)
    let option = document.querySelector(att);
    return option.options[option.selectedIndex].value;
}
function save(data) {
    fetch(case_url,{
        method:'GET',
        headers:{},
        body: datas
    })
}


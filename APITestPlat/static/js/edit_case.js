//用例，点击保存按钮
let saveBut = document.querySelector("#case-save");
let cancelBut = document.querySelector("#case-cancled");
// let edit_list= document.querySelector(".edit-case-list");
saveBut.onclick = function () {
    let caseList = {name:"", url:"", params:"",creator:"",check_key:"",check_value:"",pros:"",mokuais:""};
    let caseListSelect = {include:"", methods:"",param_types:"",assert_type:''};
    let caseHeader = {header_selected:"", re_header:{header_key:"",header_value:""}};
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
    let option = document.querySelector(att);
    return option.options[option.selectedIndex].value;
}

cancelBut.onclick = function () {
    window.location.href=caseUrl;
}
let caseList = {name:"", url:"", params:"",creator:"",check_key:"",check_value:"",pros:"",mokuais:""};
let caseListSelect = {include:"", method:"",param_type:"",assert_type:''};
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
//用例，点击保存按钮
let saveBut = document.querySelector("#case-save");
let cancelBut = document.querySelector("#case-cancled");
// 需要return 整个fetch
// 下面这里等同于上面的处理promise的方式，需要return data
let params = new URLSearchParams(document.location.search);
let case_id = params.get("id");
if (case_id){
    EditGetData({id:case_id}).then((data) => {
        // console.log(data);
        //给编辑页面赋值
        setValue(data,caseList)
        setOptionValue(data,caseListSelect);
        setValue(data["re_header"],caseHeader["re_header"]);
        //点击保存，获取页面的新的只update
        saveBut.onclick = function (){
            let editCaseList = getData();
            // console.log(editCaseList);
            let newCaseLists = {...editCaseList, ...{id:case_id}};
            let editCaseData = JSON.stringify(newCaseLists);
            caseSave(editCaseData);
        }
    })
}else {
//新增用例，点击保存按钮
    saveBut.onclick = function () {
        let newCaseList = getData()
        let data = JSON.stringify(newCaseList);
        caseSave(data);
    };
}
function setValue(data,list) {
    for (let it in list) {
        // console.log(it, data[it])
        if (it !== "pros" && it !=="mokuais"){
            document.querySelector('#'+it).value=data[it];
        }else{setOptionValues(data,it);
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
    // console.log(option.options)
    for (let i=0; i<(option.options).length;i++){
        // console.log((option.options)[i])
        let text = (option.options)[i]
        // console.log(`"${text.innerText}"`, data[it],typeof (text.innerText),typeof (data[it]))
        // console.log(text.innerText == data[it])
        if(text.innerText == data[it]){
            (option.options)[i].selected = true;
        }
    }
}
function getData() {
    caseHeader["header_selected"] = document.querySelector("#header_selected").checked
    for (let he in caseHeader["re_header"]) {
        let heValue = queryValue("#" + he);
        caseHeader["re_header"][he] = heValue;
    }
    for (let ca in caseList) {
        let caValue = queryValue("#" + ca);
        caseList[ca] = caValue;
    }
    for (let se in caseListSelect) {
        let selectValue = queryOptionValue("#" + se);
        console.log(caseListSelect[se], selectValue)
        caseListSelect[se] = selectValue;
    }
    let newCaseList = {...caseList, ...caseListSelect, ...caseHeader};
    // console.log(newCaseList);
    // console.log(caseHeader);
    return newCaseList
}
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
    return option.options[option.selectedIndex]?.value||'None';
}

cancelBut.onclick = function () {
    window.location.href=caseUrl;
}
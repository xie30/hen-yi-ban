//点击模块，切换并查询相关数据返回
var cUrl = "/home/autotest/case/";
<!-- 点击查询项目配置 -->
var temp = `<tr class="pro-list-data">
    <td name="list-case-id">{id}</td>
    <td name="list-case-name">{name}</td>
    <td name="list-dec">{c_description}</td>
    <td name="list-project">{c_project}</td>
    <td name="list-mokuai">{c_mokuai}</td>
    <td name="list-tester">{c_tester}</td>
    <td name="list-creator">{c_creator}</td>
    <td name="list-ctime">{create_time}</td>
    <td name="list-uptime">{update_time}</td>
    <td class="list-op">
        <button class="edit">编辑</button>
        <button class="delete">删除</button>
        <button class="run-case">运行</button>
        </td>
        
    </tr>`;
selected(cUrl, cases);





import{d as V,h as c,o as r,b as m,e as t,i as l,w as u,f as o,t as _,c as B,u as L,j as T,k as w,p as A,l as P,_ as F,r as b,a as z,m as X,n as W,q as H,s as K,v as S,F as O,x as G,y as Q,z as j,A as Y,C as Z,g as ee,B as te}from"./index-xAnPWFJT.js";/* empty css                                                                          *//* empty css                                                                       */import{_ as ne}from"./IndexView.vue_vue_type_script_setup_true_lang-VVdkpyuI.js";const h=e=>(A("data-v-a0244981"),e=e(),P(),e),le={key:0,style:{"max-width":"560px"}},oe=h(()=>t("br",null,null,-1)),se=h(()=>t("br",null,null,-1)),ae=h(()=>t("br",null,null,-1)),re=h(()=>t("br",null,null,-1)),ue=h(()=>t("br",null,null,-1)),ie=h(()=>t("br",null,null,-1)),de=h(()=>t("br",null,null,-1)),ce=h(()=>t("br",null,null,-1)),_e=h(()=>t("br",null,null,-1)),xe=h(()=>t("br",null,null,-1)),fe=h(()=>t("br",null,null,-1)),pe=h(()=>t("br",null,null,-1)),me=h(()=>t("br",null,null,-1)),he=h(()=>t("br",null,null,-1)),we=h(()=>t("span",null,[o("朋友圈背景："),t("br")],-1)),ve={key:0},ye=h(()=>t("br",null,null,-1)),be=h(()=>t("span",null,[o("群成员："),t("br")],-1)),ge={key:1,style:{"max-width":"560px"}},Ee=h(()=>t("br",null,null,-1)),ke=h(()=>t("br",null,null,-1)),$e=h(()=>t("br",null,null,-1)),Be={key:0},Ve=h(()=>t("br",null,null,-1)),Ce={key:1},Ie=h(()=>t("br",null,null,-1)),Se={key:2},qe=h(()=>t("br",null,null,-1)),Le={key:3},Ue=h(()=>t("br",null,null,-1)),De={key:4},je=h(()=>t("br",null,null,-1)),Re={key:5},Me=h(()=>t("br",null,null,-1)),Ne={key:6},Te=h(()=>t("br",null,null,-1)),ze={key:7},Oe=h(()=>t("br",null,null,-1)),Fe={key:8},He=h(()=>t("br",null,null,-1)),Ae={key:9},Pe=h(()=>t("br",null,null,-1)),We={key:10},Ke=h(()=>t("br",null,null,-1)),Je={key:11},Xe=h(()=>t("br",null,null,-1)),Ge=V({__name:"UserInfoShow",props:{userinfo:{type:Object,default:()=>({})},show_all:{type:Boolean,default:!0,required:!1}},setup(e){const i=e,n=({row:d,rowIndex:s})=>(console.log(d.wxid,i.userinfo.extra.owner.wxid,d.wxid==i.userinfo.extra.owner.wxid),d.wxid==i.userinfo.extra.owner.wxid?(console.log("table-success-row"),"table-success-row"):"");return(d,s)=>{const a=c("el-divider"),f=c("el-image"),p=c("el-table-column"),x=c("el-table");return e.show_all?(r(),m("div",le,[t("div",null,[l(a,{"content-position":"center"},{default:u(()=>[o("基本信息")]),_:1}),t("span",null,[o("wxid："+_(e.userinfo.wxid),1),oe]),t("span",null,[o("账号："+_(e.userinfo.account),1),se]),t("span",null,[o("昵称："+_(e.userinfo.nickname),1),ae]),t("span",null,[o("备注："+_(e.userinfo.remark),1),re])]),t("div",null,[l(a,{"content-position":"center"},{default:u(()=>[o("账号信息")]),_:1}),t("span",null,[o("性别："+_(e.userinfo.ExtraBuf["性别[1男2女]"]==1?"男":e.userinfo.ExtraBuf["性别[1男2女]"]==2?"女":""),1),ue]),t("span",null,[o("手机："+_(e.userinfo.ExtraBuf.手机号),1),ie]),t("span",null,[o("标签："+_(e.userinfo.LabelIDList.join("/")),1),de]),t("span",null,[o("描述："+_(e.userinfo.describe),1),ce]),t("span",null,[o("个签："+_(e.userinfo.ExtraBuf.个性签名),1),_e]),t("span",null,[o("国家："+_(e.userinfo.ExtraBuf.国),1),xe]),t("span",null,[o("省份："+_(e.userinfo.ExtraBuf.省),1),fe]),t("span",null,[o("市名："+_(e.userinfo.ExtraBuf.市),1),pe])]),t("div",null,[l(a,{"content-position":"center"},{default:u(()=>[o("其他信息")]),_:1}),t("span",null,[o("公司："+_(e.userinfo.ExtraBuf.公司名称),1),me]),t("span",null,[o("企微："+_(e.userinfo.ExtraBuf.企微属性),1),he]),we,e.userinfo.ExtraBuf.朋友圈背景?(r(),B(f,{key:0,src:L(T)(e.userinfo.ExtraBuf.朋友圈背景),alt:"朋友圈背景",style:{"max-width":"200px","max-height":"200px"},"preview-src-list":[L(T)(e.userinfo.ExtraBuf.朋友圈背景)],"hide-on-click-modal":!0},null,8,["src","preview-src-list"])):w("",!0)]),e.userinfo.extra?(r(),m("div",ve,[l(a,{"content-position":"center"},{default:u(()=>[o("群聊信息")]),_:1}),t("span",null,[o("群主: "+_(e.userinfo.extra.owner.wxid),1),ye]),be,l(x,{data:Object.values(e.userinfo.extra.wxid2userinfo),style:{width:"100%"},"row-class-name":n},{default:u(()=>[l(p,{prop:"wxid",label:"wxid"}),l(p,{prop:"account",label:"账号"}),l(p,{prop:"nickname",label:"昵称"}),l(p,{prop:"remark",label:"备注"}),l(p,{prop:"roomNickname",label:"群昵称"})]),_:1},8,["data"])])):w("",!0)])):(r(),m("div",ge,[t("span",null,[o("wxid："+_(e.userinfo.wxid),1),Ee]),t("span",null,[o("账号："+_(e.userinfo.account),1),ke]),t("span",null,[o("昵称："+_(e.userinfo.nickname),1),$e]),e.userinfo.remark?(r(),m("span",Be,[o("备注："+_(e.userinfo.remark),1),Ve])):w("",!0),e.userinfo.ExtraBuf&&e.userinfo.ExtraBuf["性别[1男2女]"]?(r(),m("span",Ce,[o("性别："+_(e.userinfo.ExtraBuf["性别[1男2女]"]==1?"男":e.userinfo.ExtraBuf["性别[1男2女]"]==2?"女":""),1),Ie])):w("",!0),e.userinfo.ExtraBuf&&e.userinfo.ExtraBuf.手机号?(r(),m("span",Se,[o("手机："+_(e.userinfo.ExtraBuf.手机号),1),qe])):w("",!0),e.userinfo.LabelIDList&&e.userinfo.LabelIDList.length>0?(r(),m("span",Le,[o("标签："+_(e.userinfo.LabelIDList.join("/")),1),Ue])):w("",!0),e.userinfo.describe?(r(),m("span",De,[o("描述："+_(e.userinfo.describe),1),je])):w("",!0),e.userinfo.ExtraBuf&&e.userinfo.ExtraBuf.个性签名?(r(),m("span",Re,[o("个签："+_(e.userinfo.ExtraBuf.个性签名),1),Me])):w("",!0),e.userinfo.ExtraBuf&&e.userinfo.ExtraBuf.国?(r(),m("span",Ne,[o("国家："+_(e.userinfo.ExtraBuf.国),1),Te])):w("",!0),e.userinfo.ExtraBuf&&e.userinfo.ExtraBuf.省?(r(),m("span",ze,[o("省份："+_(e.userinfo.ExtraBuf.省),1),Oe])):w("",!0),e.userinfo.ExtraBuf&&e.userinfo.ExtraBuf.市?(r(),m("span",Fe,[o("市名："+_(e.userinfo.ExtraBuf.市),1),He])):w("",!0),e.userinfo.ExtraBuf&&e.userinfo.ExtraBuf.公司名称?(r(),m("span",Ae,[o("公司："+_(e.userinfo.ExtraBuf.公司名称),1),Pe])):w("",!0),e.userinfo.ExtraBuf&&e.userinfo.ExtraBuf.企微属性?(r(),m("span",We,[o("企微："+_(e.userinfo.ExtraBuf.企微属性),1),Ke])):w("",!0),e.userinfo.ExtraBuf&&e.userinfo.ExtraBuf.朋友圈背景?(r(),m("span",Je,[o("朋友圈背景："),Xe])):w("",!0),e.userinfo.ExtraBuf&&e.userinfo.ExtraBuf.朋友圈背景?(r(),B(f,{key:12,src:L(T)(e.userinfo.ExtraBuf.朋友圈背景),style:{"max-width":"200px","max-height":"200px"},alt:"朋友圈背景"},null,8,["src"])):w("",!0)]))}}}),J=F(Ge,[["__scopeId","data-v-a0244981"]]),Qe=e=>(A("data-v-0836fbf7"),e=e(),P(),e),Ye={style:{padding:"10px 10px"}},Ze={slot:"content",class:"tips"},et=Qe(()=>t("br",null,null,-1)),tt={key:0,style:{color:"#909399","font-size":"12px"}},nt=V({__name:"ContactsList",emits:["wxid"],setup(e,{emit:i}){const n=b([]);z(async()=>{try{n.value=await H()}catch(x){return console.error("Error fetching data:",x),[]}});const s=b(""),a=async()=>{try{if(s.value===""){n.value=await H();return}console.log(s.value),n.value=[];const x=await K(s.value);x!==null&&typeof x=="object"&&Object.entries(x).forEach(([v,E])=>{n.value.push(E)})}catch(x){return console.error("Error fetching data:",x),[]}},f=i,p=x=>{x!==void 0&&x.wxid!==void 0&&(console.log("wxid:",x.wxid),f("wxid",x.wxid))};return(x,v)=>{const E=c("el-input"),$=c("el-button"),R=c("el-avatar"),U=c("el-table-column"),g=c("el-tooltip"),k=c("el-table");return r(),m("div",null,[t("div",Ye,[l(E,{placeholder:"请输入关键字",modelValue:s.value,"onUpdate:modelValue":v[0]||(v[0]=y=>s.value=y),onKeyup:X(a,["enter"]),style:{width:"170px","margin-left":"15px"}},null,8,["modelValue"]),l($,{type:"primary",onClick:a,style:{width:"50px"}},{default:u(()=>[o("搜索")]),_:1})]),l(k,{data:n.value,stripe:"",style:{width:"100%"},"max-height":"100%",height:"100%","highlight-current-row":"",loading:"lazy",onCurrentChange:p},{default:u(()=>[l(U,{width:"57"},{default:u(({row:y})=>[y.headImgUrl!==""?(r(),B(R,{key:0,size:33,src:L(T)(y.headImgUrl)},null,8,["src"])):(r(),B(R,{key:1,size:33},{default:u(()=>[o("群")]),_:1}))]),_:1}),l(U,{width:"190"},{default:u(({row:y})=>[l(g,{class:"item",effect:"light",placement:"right"},{content:u(()=>[l(J,{userinfo:y,show_all:!1,style:{"max-width":"600px"}},null,8,["userinfo"])]),default:u(()=>[t("div",Ze,[t("span",null,_(L(W)(y)),1),o(),et,y.nTime?(r(),m("span",tt,_(y.nTime),1)):w("",!0)])]),_:2},1024)]),_:1})]),_:1},8,["data"])])}}}),lt=F(nt,[["__scopeId","data-v-0836fbf7"]]),ot=V({__name:"ChatRecprdsHeader",props:{wxid:{type:String,required:!0}},emits:["exporting"],setup(e,{emit:i}){const n=e,d=b(0),s=b({wxid:"",nOrder:0,nUnReadCount:0,strNickName:"",nStatus:0,nIsSend:0,strContent:"",nMsgLocalID:0,nMsgStatus:0,nTime:"",nMsgType:0,nMsgSubType:0,nickname:"",remark:"",account:"",describe:"",headImgUrl:"",ExtraBuf:{个性签名:"",企微属性:"",公司名称:"",国:"",备注图片:"",备注图片2:"",市:"","性别[1男2女]":0,手机号:"",朋友圈背景:"",省:""},LabelIDList:[],extra:null}),a=async()=>{var g,k,y,q,M,N,C,D;try{const I=await K("",[n.wxid]);return s.value.wxid=n.wxid,s.value.remark=(g=I[n.wxid])==null?void 0:g.remark,s.value.account=(k=I[n.wxid])==null?void 0:k.account,s.value.describe=(y=I[n.wxid])==null?void 0:y.describe,s.value.headImgUrl=(q=I[n.wxid])==null?void 0:q.headImgUrl,s.value.nickname=(M=I[n.wxid])==null?void 0:M.nickname,s.value.LabelIDList=(N=I[n.wxid])==null?void 0:N.LabelIDList,s.value.ExtraBuf=(C=I[n.wxid])==null?void 0:C.ExtraBuf,s.value.extra=(D=I[n.wxid])==null?void 0:D.extra,I}catch(I){return console.error("Error fetching data wxid2user :",I),[]}},f=async()=>{try{d.value=0;const g=await Q(n.wxid);return d.value=g||0,g}catch(g){return console.error("Error fetching data msg_count:",g),[]}},p=()=>{$.value=!1,a(),f()};z(()=>{console.log("ChatRecprdsHeader onMounted",n.wxid),p()}),S(()=>n.wxid,async(g,k)=>{g!==k&&p()});const x=b(!1),v=b(!1),E=async()=>{if(v.value){console.log("正在获取实时消息，请稍后再试!");return}v.value=!0;try{const g=await G();return v.value=!1,g}catch{return v.value=!1,[]}},$=b(!1),R=i,U=g=>{R("exporting",g),$.value=g};return(g,k)=>{const y=c("el-text"),q=c("el-col"),M=c("el-row"),N=c("el-dialog");return r(),m(O,null,[l(M,{gutter:5,style:{width:"100%"}},{default:u(()=>[l(q,{span:6,style:{"white-space":"nowrap"}},{default:u(()=>{var C;return[l(y,{class:"label_color mx-1",truncated:""},{default:u(()=>[o("wxid:")]),_:1}),o("  "),l(y,{class:"data_color mx-1",truncated:"",title:(C=s.value)==null?void 0:C.wxid},{default:u(()=>{var D;return[o(_((D=s.value)==null?void 0:D.wxid),1)]}),_:1},8,["title"])]}),_:1}),l(q,{span:6,style:{"white-space":"nowrap"}},{default:u(()=>[l(y,{class:"label_color mx-1",truncated:""},{default:u(()=>[o("名称:")]),_:1}),o("  "),l(y,{class:"data_color mx-1",truncated:"",title:"show_name"},{default:u(()=>[o(_(L(W)(s.value)),1)]),_:1})]),_:1}),l(q,{span:5,style:{"white-space":"nowrap"}},{default:u(()=>[l(y,{class:"label_color mx-1",truncated:""},{default:u(()=>[o("数量:")]),_:1}),o("  "),l(y,{class:"data_color mx-1",truncated:"",title:d.value},{default:u(()=>[o(_(d.value),1)]),_:1},8,["title"])]),_:1}),l(q,{span:2,style:{"white-space":"nowrap"}},{default:u(()=>[l(y,{class:"button_color mx-1 underline",truncated:"",onClick:k[0]||(k[0]=C=>x.value=!x.value)},{default:u(()=>[o(" 详细信息")]),_:1})]),_:1}),l(q,{span:2,style:{"white-space":"nowrap"}},{default:u(()=>[$.value?w("",!0):(r(),B(y,{key:0,class:"button_color mx-1 underline",truncated:"",onClick:k[1]||(k[1]=C=>{U(!0)})},{default:u(()=>[o("导出备份 ")]),_:1})),$.value?(r(),B(y,{key:1,class:"button_color mx-1 underline",truncated:"",onClick:k[2]||(k[2]=C=>{U(!1)})},{default:u(()=>[o("聊天查看 ")]),_:1})):w("",!0)]),_:1}),l(q,{span:3,style:{"white-space":"nowrap"}},{default:u(()=>[l(y,{class:"button_color mx-1 underline",truncated:"",onClick:k[3]||(k[3]=C=>{E()})},{default:u(()=>[o("实时消息 "),v.value?(r(),m(O,{key:0},[o("...")],64)):w("",!0)]),_:1})]),_:1})]),_:1}),l(N,{modelValue:x.value,"onUpdate:modelValue":k[4]||(k[4]=C=>x.value=C),title:"详细信息",width:"600",center:""},{default:u(()=>[l(J,{userinfo:s.value,show_all:!0},null,8,["userinfo"])]),_:1},8,["modelValue"])],64)}}}),st=F(ot,[["__scopeId","data-v-b3b47fb2"]]),at=t("br",null,null,-1),rt=t("br",null,null,-1),ut={style:{position:"relative"}},it=V({__name:"ExportENDB",props:{wxid:{type:String,required:!0}},setup(e){const i=e;S(()=>i.wxid,(a,f)=>{console.log(a)});const n=b(""),d=b(""),s=async()=>{d.value="请求中...";try{d.value=await j.post("/api/rs/export_endb",{wx_path:n.value})}catch(a){return console.error("Error fetching data msg_count:",a),d.value=`请求失败
`+a,[]}};return(a,f)=>{const p=c("el-input"),x=c("el-button"),v=c("el-divider");return r(),m("div",null,[o(" 微信文件夹路径(可选)： "),l(p,{placeholder:"微信文件夹路径[可为空,空表示使用默认的，无默认会报错](eg: C:\\****\\WeChat Files\\wxid_**** )",modelValue:n.value,"onUpdate:modelValue":f[0]||(f[0]=E=>n.value=E),style:{width:"70%"}},null,8,["modelValue"]),at,rt,t("div",ut,[l(x,{type:"primary",onClick:f[1]||(f[1]=E=>s())},{default:u(()=>[o("导出")]),_:1})]),l(v),l(p,{type:"textarea",rows:6,readonly:"",placeholder:"",modelValue:d.value,"onUpdate:modelValue":f[2]||(f[2]=E=>d.value=E),style:{width:"100%"}},null,8,["modelValue"])])}}}),dt=t("br",null,null,-1),ct=t("br",null,null,-1),_t=t("br",null,null,-1),xt=t("br",null,null,-1),ft={style:{position:"relative"}},pt=V({__name:"ExportDEDB",props:{wxid:{type:String,required:!0}},setup(e){const i=e;S(()=>i.wxid,(f,p)=>{console.log(f)});const n=b(""),d=b(""),s=b(""),a=async()=>{s.value="正在处理中...";try{s.value=await j.post("/api/rs/export_dedb",{key:d.value,wx_path:n.value})}catch(f){return console.error("Error fetching data msg_count:",f),s.value=`请求失败
`+f,[]}};return(f,p)=>{const x=c("el-input"),v=c("el-button"),E=c("el-divider");return r(),m("div",null,[o(" 密钥(可选)： "),l(x,{placeholder:"密钥[可为空,空表示使用默认的，无默认会报错]",modelValue:d.value,"onUpdate:modelValue":p[0]||(p[0]=$=>d.value=$),style:{width:"75%"}},null,8,["modelValue"]),dt,ct,o(" 微信文件夹路径(可选)： "),l(x,{placeholder:"微信文件夹路径[可为空,空表示使用默认的，无默认会报错](eg: C:\\****\\WeChat Files\\wxid_**** )",modelValue:n.value,"onUpdate:modelValue":p[1]||(p[1]=$=>n.value=$),style:{width:"70%"}},null,8,["modelValue"]),_t,xt,t("div",ft,[l(v,{type:"primary",onClick:p[2]||(p[2]=$=>a())},{default:u(()=>[o("导出")]),_:1})]),l(E),l(x,{type:"textarea",rows:6,readonly:"",placeholder:"",modelValue:s.value,"onUpdate:modelValue":p[3]||(p[3]=$=>s.value=$),style:{width:"100%"}},null,8,["modelValue"])])}}}),mt={style:{position:"relative"}},ht=V({__name:"ExportCSV",props:{wxid:{type:String,required:!0}},setup(e){const i=e;S(()=>i.wxid,(s,a)=>{console.log(s)});const n=b(""),d=async()=>{n.value="正在处理中...";try{n.value=await j.post("/api/rs/export_csv",{wxid:i.wxid})}catch(s){return console.error("Error fetching data msg_count:",s),n.value=`请求失败
`+s,[]}};return(s,a)=>{const f=c("el-button"),p=c("el-divider"),x=c("el-input");return r(),m("div",null,[t("div",mt,[l(f,{type:"primary",onClick:a[0]||(a[0]=v=>d())},{default:u(()=>[o("导出")]),_:1})]),l(p),l(x,{type:"textarea",rows:6,readonly:"",placeholder:"",modelValue:n.value,"onUpdate:modelValue":a[1]||(a[1]=v=>n.value=v),style:{width:"100%"}},null,8,["modelValue"])])}}}),wt={style:{position:"relative"}},vt=V({__name:"ExportJSON",props:{wxid:{type:String,required:!0}},setup(e){const i=e;S(()=>i.wxid,(s,a)=>{console.log(s)}),b([]);const n=b(""),d=async()=>{n.value="正在处理中...";try{n.value=await j.post("/api/rs/export_json",{wxid:i.wxid})}catch(s){return console.error("Error fetching data msg_count:",s),n.value=`请求失败
`+s,[]}};return(s,a)=>{const f=c("el-button"),p=c("el-divider"),x=c("el-input");return r(),m("div",null,[t("div",wt,[l(f,{type:"primary",onClick:a[0]||(a[0]=v=>d())},{default:u(()=>[o("导出")]),_:1})]),l(p),l(x,{type:"textarea",rows:6,readonly:"",placeholder:"",modelValue:n.value,"onUpdate:modelValue":a[1]||(a[1]=v=>n.value=v),style:{width:"100%"}},null,8,["modelValue"])])}}}),yt=t("span",null,"使用说明：（1）根据 https://blog.csdn.net/meser88/article/details/130229417 进行设置",-1),bt=t("br",null,null,-1),gt=t("span",null,"（2）打开导出的文件夹位置，使用（1）设置的浏览器打开 index.html 文件",-1),Et={style:{position:"relative"}},kt=V({__name:"ExportHTML",props:{wxid:{type:String,required:!0}},setup(e){const i=e;S(()=>i.wxid,(s,a)=>{console.log(s)}),b([]);const n=b(""),d=async()=>{n.value="正在处理中...";try{n.value=await j.post("/api/rs/export_html",{wxid:i.wxid})}catch(s){return console.error("Error fetching data msg_count:",s),n.value=`请求失败
`+s,[]}};return(s,a)=>{const f=c("el-button"),p=c("el-divider"),x=c("el-input");return r(),m("div",null,[yt,bt,gt,t("div",Et,[l(f,{type:"primary",onClick:a[0]||(a[0]=v=>d())},{default:u(()=>[o("导出")]),_:1})]),l(p),l(x,{type:"textarea",rows:6,readonly:"",placeholder:"",modelValue:n.value,"onUpdate:modelValue":a[1]||(a[1]=v=>n.value=v),style:{width:"100%"}},null,8,["modelValue"])])}}}),$t=t("br",null,null,-1),Bt=V({__name:"ExportPDF",props:{wxid:{type:String,required:!0}},setup(e){const i=e;S(()=>i.wxid,(d,s)=>{console.log(d)});const n=()=>{console.log("requestExport")};return(d,s)=>{const a=c("el-button");return r(),m("div",null,[t("span",null,_(i.wxid),1),$t,l(a,{type:"primary",onClick:s[0]||(s[0]=f=>n())},{default:u(()=>[o("导出")]),_:1})])}}}),Vt=t("br",null,null,-1),Ct=V({__name:"ExportDOCX",props:{wxid:{type:String,required:!0}},setup(e){const i=e;S(()=>i.wxid,(d,s)=>{console.log(d)});const n=()=>{console.log("requestExport")};return(d,s)=>{const a=c("el-button");return r(),m("div",null,[t("span",null,_(i.wxid),1),Vt,l(a,{type:"primary",onClick:s[0]||(s[0]=f=>n())},{default:u(()=>[o("导出")]),_:1})])}}}),It={id:"chat_export",style:{"background-color":"#d2d2fa",padding:"0"}},St={style:{"background-color":"#d2d2fa",height:"calc(100vh - 65px)",display:"grid","place-items":"center"}},qt={style:{"background-color":"#fff",width:"70%",height:"70%","border-radius":"10px",padding:"20px",overflow:"auto"}},Lt=t("div",{style:{display:"flex","justify-content":"space-between","align-items":"center"}},[t("div",{style:{"font-size":"20px","font-weight":"bold"}},"导出与备份(未完待续...）"),t("div",{style:{display:"flex","justify-content":"space-between","align-items":"center"}})],-1),Ut={style:{"margin-top":"20px"}},Dt=t("br",null,null,-1),jt=t("br",null,null,-1),Rt={key:0},Mt=V({__name:"ChatExportMain",props:{wxid:{type:String,required:!0}},setup(e){const i=e;S(()=>i.wxid,(s,a)=>{console.log(s)});const n=b("");b("");const d={endb:{brief:"加密文件",detail:"导出的内容为微信加密数据库。可还原回微信,但会覆盖微信后续消息。(全程不解密，所以数据安全)"},dedb:{brief:"解密文件",detail:"导出的文件为解密后的sqlite数据库，并且会自动合并msg和media数据库为同一个，但是无法还原回微信。"},csv:{brief:"csv",detail:"只包含文本，但是可以用excel软件（wps，office）打开。"},json:{brief:"json",detail:"只包含文本，可用于数据分析，情感分析等方面。"},html:{brief:"html-测试中",detail:"主要用于浏览器可视化查看。"},pdf:{brief:"pdf-开发中",detail:"pdf版本。"},docx:{brief:"docx-开发中",detail:"docx版本。"}};return(s,a)=>{const f=c("el-option"),p=c("el-select"),x=c("el-divider"),v=c("el-main");return r(),m("div",It,[l(v,{style:{"overflow-y":"auto",height:"calc(100vh - 65px)",padding:"0"}},{default:u(()=>[t("div",St,[t("div",qt,[Lt,t("div",Ut,[o(" 导出类型: "),l(p,{placeholder:"请选择导出类型",style:{width:"50%"},modelValue:n.value,"onUpdate:modelValue":a[0]||(a[0]=E=>n.value=E)},{default:u(()=>[(r(),m(O,null,Y(d,(E,$)=>l(f,{label:E.brief,value:$,key:$},{default:u(()=>[o(_(E.brief),1)]),_:2},1032,["label","value"])),64))]),_:1},8,["modelValue"]),Dt,jt,n.value?(r(),m("span",Rt,_(d[n.value].detail),1)):w("",!0)]),l(x),n.value=="endb"?(r(),B(it,{key:0,wxid:i.wxid},null,8,["wxid"])):w("",!0),n.value=="dedb"?(r(),B(pt,{key:1,wxid:i.wxid},null,8,["wxid"])):w("",!0),n.value=="csv"?(r(),B(ht,{key:2,wxid:i.wxid},null,8,["wxid"])):w("",!0),n.value=="json"?(r(),B(vt,{key:3,wxid:i.wxid},null,8,["wxid"])):w("",!0),n.value=="html"?(r(),B(kt,{key:4,wxid:i.wxid},null,8,["wxid"])):w("",!0),n.value=="pdf"?(r(),B(Bt,{key:5,wxid:i.wxid},null,8,["wxid"])):w("",!0),n.value=="docx"?(r(),B(Ct,{key:6,wxid:i.wxid},null,8,["wxid"])):w("",!0)])])]),_:1})])}}}),Nt=V({__name:"ChatRecords",props:{wxid:{type:String,required:!0}},setup(e){const i=e,n=b(!1),d=a=>{n.value=a},s=()=>{n.value=!1};return S(()=>i.wxid,async(a,f)=>{a!==f&&s()}),z(()=>{s()}),(a,f)=>{const p=c("el-header"),x=c("el-main"),v=c("el-container");return r(),B(v,null,{default:u(()=>[l(p,{style:{height:"40px","max-height":"40px",width:"100%","background-color":"#d2d2fa","padding-top":"5px"}},{default:u(()=>[l(st,{wxid:e.wxid,onExporting:d},null,8,["wxid"])]),_:1}),l(x,{style:{height:"calc(100vh - 40px)",padding:"0",margin:"0","background-color":"#f5f5f5"}},{default:u(()=>[n.value?(r(),B(Mt,{key:0,wxid:e.wxid},null,8,["wxid"])):(r(),B(Z,{key:1,wxid:e.wxid},null,8,["wxid"]))]),_:1})]),_:1})}}}),Tt={id:"chat_view",class:"common-layout"},zt={key:0,style:{height:"calc(100vh)",width:"100%"}},Ot={key:1,style:{width:"100%",height:"100%"}},Wt=V({__name:"ChatView",setup(e){const i=b("");return z(()=>{ee().then(n=>{console.log("API version: "+n)}).catch(n=>{console.error("Error fetching API version:",n)}),te()}),(n,d)=>{const s=c("el-aside"),a=c("el-container");return r(),m("div",Tt,[t("div",null,[l(a,null,{default:u(()=>[l(s,{width:"auto",style:{"overflow-y":"auto",height:"calc(100vh)"}},{default:u(()=>[l(lt,{onWxid:d[0]||(d[0]=f=>{i.value=f})})]),_:1}),i.value!=""?(r(),m("div",zt,[l(Nt,{wxid:i.value},null,8,["wxid"])])):(r(),m("div",Ot,[l(ne)]))]),_:1})])])}}});export{Wt as default};

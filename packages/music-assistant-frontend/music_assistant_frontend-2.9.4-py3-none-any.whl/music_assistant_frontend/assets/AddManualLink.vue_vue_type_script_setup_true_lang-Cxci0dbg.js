import{d as M,ai as $,aj as C,r,K as b,c as D,e as U,w as m,s as A,f as t,g,W as y,t as c,M as I,b as v,aa as h}from"./index-CLKg64ON.js";import{T as w}from"./Toolbar-BaIn3BvJ.js";import{V as N}from"./VDialog-BpGrcp5y.js";import{V as L}from"./VList-BvG6-yh2.js";import{V as f}from"./VTextField-C1QkMZRy.js";import{a as R,V as S}from"./VCard-BaRPabiE.js";import{V as W}from"./VSpacer-CqqJVVs3.js";import{s as T}from"./VListItem-B_TSjQ1y.js";const j={style:{padding:"15px"}},z=M({__name:"AddManualLink",props:$({type:{}},{modelValue:{type:Boolean},modelModifiers:{}}),emits:["update:modelValue"],setup(p){const d=C(p,"modelValue"),k=p,u=r(""),n=r(""),s=r(""),i=r(!1),l=r();b(()=>d.value,e=>{e!=null&&(A.dialogActive=e),e==!1&&(u.value="",n.value="",s.value="",l.value=void 0)},{immediate:!0}),b(()=>l.value,e=>{if(e){n.value||(n.value=e.name);for(const a of e.metadata.images||[])if(a.type=="thumb"){s.value=a.path;break}}});const V=()=>{!u.value||!u.value.startsWith("http")||(i.value=!0,k.type==I.RADIO?v.getRadio(u.value,"builtin").then(e=>{l.value=e}).catch(e=>{console.error(e),l.value=void 0}).finally(()=>{i.value=!1}):v.getTrack(u.value,"builtin").then(e=>{l.value=e}).catch(e=>{console.error(e),l.value=void 0}).finally(()=>{i.value=!1}))},B=function(){V(),l.value&&(l.value.name=n.value||l.value.name,delete l.value.sort_name,s.value&&(l.value.metadata.images=[{type:h.THUMB,path:s.value,provider:"builtin",remotely_accessible:!0}]),v.addItemToLibrary(l.value,!0).then(()=>{d.value=!1}))};return(e,a)=>(D(),U(N,{modelValue:d.value,"onUpdate:modelValue":a[4]||(a[4]=o=>d.value=o),transition:"dialog-bottom-transition"},{default:m(()=>[t(S,null,{default:m(()=>[t(w,{icon:"mdi-playlist-plus",title:e.$t("add_url_item")},null,8,["title"]),t(L),a[5]||(a[5]=g("br",null,null,-1)),g("div",j,[t(f,{modelValue:u.value,"onUpdate:modelValue":a[0]||(a[0]=o=>u.value=o),variant:"outlined",label:e.$t("enter_url"),disabled:i.value,onBlur:V},null,8,["modelValue","label","disabled"]),t(f,{modelValue:n.value,"onUpdate:modelValue":a[1]||(a[1]=o=>n.value=o),variant:"outlined",label:e.$t("enter_name"),disabled:i.value},null,8,["modelValue","label","disabled"]),t(f,{modelValue:s.value,"onUpdate:modelValue":a[2]||(a[2]=o=>s.value=o),variant:"outlined",label:e.$t("image_url"),disabled:i.value},null,8,["modelValue","label","disabled"]),t(R,null,{default:m(()=>[t(W),t(T,{variant:"outlined",onClick:a[3]||(a[3]=o=>d.value=!1)},{default:m(()=>[y(c(e.$t("cancel")),1)]),_:1}),t(T,{variant:"flat",color:"primary",disabled:i.value,onClick:B},{default:m(()=>[y(c(e.$t("save")),1)]),_:1},8,["disabled"])]),_:1})])]),_:1})]),_:1},8,["modelValue"]))}});export{z as _};

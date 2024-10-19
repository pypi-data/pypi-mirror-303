import{p as X,ay as j,n as E,k as W,v as z,I as Y,q,az as G,f as l,N as H,R as J,D as V,d as K,c as n,e as s,X as w,w as o,g as Q,W as U,t as Z,u as c,V as B,j as g,b as y,h as b,i as $,F as N}from"./index-b2T7whGP.js";import{V as x}from"./VToolbar-DuWNnIZ4.js";import{m as I,E as ee,g as te,b as ae,N as oe,j as le,n as ie,r as ne,O as re,c as se,M as de,w as u,s as h,z as M,V as R}from"./VListItem-C1lr_U2J.js";import{V as _}from"./VMenu-BWs87hpq.js";import{a as O}from"./VList-BoTr11ox.js";import{_ as ce}from"./_plugin-vue_export-helper-DlAUqK2U.js";const ue=X({bordered:Boolean,color:String,content:[Number,String],dot:Boolean,floating:Boolean,icon:j,inline:Boolean,label:{type:String,default:"$vuetify.badge"},max:[Number,String],modelValue:{type:Boolean,default:!0},offsetX:[Number,String],offsetY:[Number,String],textColor:String,...I(),...ee({location:"top end"}),...te(),...ae(),...E(),...oe({transition:"scale-rotate-transition"})},"VBadge"),C=W()({name:"VBadge",inheritAttrs:!1,props:ue(),setup(t,f){const{backgroundColorClasses:k,backgroundColorStyles:a}=le(z(t,"color")),{roundedClasses:v}=ie(t),{t:m}=Y(),{textColorClasses:e,textColorStyles:r}=ne(z(t,"textColor")),{themeClasses:i}=q(),{locationStyles:p}=re(t,!0,d=>(t.floating?t.dot?2:4:t.dot?8:12)+(["top","bottom"].includes(d)?+(t.offsetY??0):["left","right"].includes(d)?+(t.offsetX??0):0));return se(()=>{const d=Number(t.content),S=!t.max||isNaN(d)?t.content:d<=+t.max?d:`${t.max}+`,[D,F]=G(f.attrs,["aria-atomic","aria-label","aria-live","role","title"]);return l(t.tag,V({class:["v-badge",{"v-badge--bordered":t.bordered,"v-badge--dot":t.dot,"v-badge--floating":t.floating,"v-badge--inline":t.inline},t.class]},F,{style:t.style}),{default:()=>{var T,P;return[l("div",{class:"v-badge__wrapper"},[(P=(T=f.slots).default)==null?void 0:P.call(T),l(de,{transition:t.transition},{default:()=>{var A,L;return[H(l("span",V({class:["v-badge__badge",i.value,k.value,v.value,e.value],style:[a.value,r.value,t.inline?{}:p.value],"aria-atomic":"true","aria-label":m(t.label,d),"aria-live":"polite",role:"status"},D),[t.dot?void 0:f.slots.badge?(L=(A=f.slots).badge)==null?void 0:L.call(A):t.icon?l(u,{icon:t.icon},null):S]),[[J,t.modelValue]])]}})])]}})}),{}}}),fe={key:1},ve=K({__name:"Toolbar",props:{color:{default:"transparent"},icon:{default:void 0},title:{default:void 0},count:{default:void 0},menuItems:{default:void 0},enforceOverflowMenu:{type:Boolean,default:!1},showLoading:{type:Boolean,default:void 0}},emits:["iconClicked","titleClicked"],setup(t,{emit:f}){const k=f;return(a,v)=>{var m;return n(),s(x,{color:a.color,class:"header"},w({_:2},[a.icon?{name:"prepend",fn:o(()=>[l(h,{icon:a.icon,size:"large",onClick:v[0]||(v[0]=e=>k("iconClicked"))},null,8,["icon"])]),key:"0"}:void 0,a.title?{name:"title",fn:o(()=>[Q("div",{onClick:v[1]||(v[1]=e=>k("titleClicked"))},[U(Z(a.title)+" ",1),a.count&&c(B)("bp4")?(n(),s(C,{key:0,color:"grey",content:a.count,inline:""},null,8,["content"])):g("",!0)])]),key:"1"}:void 0,(m=a.menuItems)!=null&&m.length?{name:"append",fn:o(()=>[a.showLoading&&(c(y).fetchesInProgress.value.length>0||c(y).syncTasks.value.length>0)?(n(),s(M,{key:0,color:"primary",indeterminate:"",title:a.$t("tooltip.loading")},null,8,["title"])):g("",!0),(n(!0),b(N,null,$(a.menuItems.filter(e=>!e.hide),e=>{var r;return n(),b("div",{key:e.label},[(r=e.subItems)!=null&&r.length?(n(),s(_,{key:0,location:"bottom end",scrim:"",density:"compact",slim:"",tile:""},{activator:o(({props:i})=>[l(h,V({variant:"text",style:{width:"40px"},ref_for:!0},i,{title:a.$t(e.label,e.labelArgs||[]),disabled:e.disabled==!0}),{default:o(()=>[l(C,{"model-value":e.active==!0,color:"error",dot:""},{default:o(()=>[l(u,{icon:e.icon,color:a.$vuetify.theme.current.dark?"#fff":"#000",size:"22px"},null,8,["icon","color"])]),_:2},1032,["model-value"])]),_:2},1040,["title","disabled"])]),default:o(()=>[l(O,null,{default:o(()=>[(n(!0),b(N,null,$(e.subItems.filter(i=>i.hide!=!0),(i,p)=>(n(),s(R,{key:p,title:a.$t(i.label,i.labelArgs||[]),disabled:i.disabled==!0,onClick:d=>i.action?i.action():""},w({append:o(()=>[i.selected?(n(),s(u,{key:0,icon:"mdi-check"})):g("",!0)]),_:2},[i.icon?{name:"prepend",fn:o(()=>[l(u,{icon:i.icon},null,8,["icon"])]),key:"0"}:void 0]),1032,["title","disabled","onClick"]))),128))]),_:2},1024)]),_:2},1024)):!a.enforceOverflowMenu&&(c(B)("bp5")||e.overflowAllowed==!1)?(n(),s(h,{key:1,variant:"text",style:{width:"40px"},title:a.$t(e.label,e.labelArgs||[]),disabled:e.disabled==!0,onClick:e.action},{default:o(()=>[l(C,{"model-value":e.active==!0,color:"error",dot:""},{default:o(()=>[l(u,{icon:e.icon,color:a.$vuetify.theme.current.dark?"#fff":"#000",size:"22px"},null,8,["icon","color"])]),_:2},1032,["model-value"])]),_:2},1032,["title","disabled","onClick"])):g("",!0)])}),128)),(!c(B)("bp5")||a.enforceOverflowMenu)&&a.menuItems.filter(e=>{var r;return e.hide!=!0&&!((r=e.subItems)!=null&&r.length)&&e.overflowAllowed!==!1}).length?(n(),b("div",fe,[l(_,{location:"bottom end",scrim:""},{activator:o(({props:e})=>[l(h,V({variant:"plain",style:{width:"15px","margin-left":"-10px"}},e),{default:o(()=>[l(u,{icon:"mdi-dots-vertical",color:a.$vuetify.theme.current.dark?"#fff":"#000",size:"22",style:{"margin-right":"-5px",width:"15px"}},null,8,["color"])]),_:2},1040)]),default:o(()=>[l(O,{density:"compact",slim:"",tile:""},{default:o(()=>[(n(!0),b(N,null,$(a.menuItems.filter(e=>{var r;return e.hide!=!0&&!((r=e.subItems)!=null&&r.length)&&e.overflowAllowed!==!1}),(e,r)=>(n(),s(R,{key:r,title:a.$t(e.label,e.labelArgs||[]),disabled:e.disabled==!0,onClick:i=>e.action?e.action():""},w({_:2},[e.icon?{name:"prepend",fn:o(()=>[l(C,{"model-value":e.active==!0,color:"error",dot:""},{default:o(()=>[l(u,{icon:e.icon,color:a.$vuetify.theme.current.dark?"#fff":"#000",size:"22px"},null,8,["icon","color"])]),_:2},1032,["model-value"])]),key:"0"}:void 0]),1032,["title","disabled","onClick"]))),128))]),_:1})]),_:1})])):g("",!0)]),key:"2"}:a.showLoading?{name:"append",fn:o(()=>[c(y).fetchesInProgress.value.length>0||c(y).syncTasks.value.length>0?(n(),s(M,{key:0,color:"primary",indeterminate:""})):g("",!0)]),key:"3"}:void 0]),1032,["color"])}}}),Ce=ce(ve,[["__scopeId","data-v-2564e8da"]]);export{Ce as T,C as V};

import{d as D,ak as R,r as Y,x as j,b as i,a7 as z,a as F,K as O,c as s,h as v,i as C,u as a,F as M,f as d,w as o,W as f,t as u,$ as l,e as m,D as X,j as g,aA as _,g as b}from"./index-CLKg64ON.js";import{_ as x,e as K}from"./eventbus-D-xzWv8v.js";import{B as y}from"./Button-F8l3l_P8.js";import{L as W}from"./ListItem-f79Nhqh7.js";import{C as q}from"./Container-ZPskS02H.js";import{s as G,V as H,w as k}from"./VListItem-B_TSjQ1y.js";import{V as J}from"./VCard-BaRPabiE.js";import{V as Q}from"./VMenu-CLSWQG_U.js";import{V as T}from"./VToolbar-DSn0RyUD.js";import{V as A}from"./VAlert-CCGDAWu2.js";import{_ as Z}from"./_plugin-vue_export-helper-DlAUqK2U.js";/* empty css              */import"./VCardText-BAUfdzDA.js";const ee={class:"line-clamp-1"},ne={class:"line-clamp-1"},te=D({__name:"Providers",setup(ie){const P=R(),p=Y([]),V=j(()=>Object.values(i.providerManifests).filter(t=>t.multi_instance||!p.value.find(n=>n.domain==t.domain)).sort((t,n)=>(t.name||i.providerManifests[t.domain].name).toUpperCase()>(n.name||i.providerManifests[n.domain].name).toUpperCase()?1:-1)),I=i.subscribe(z.PROVIDERS_UPDATED,()=>{w()});F(I);const w=async function(){p.value=await i.getProviderConfigs()},$=function(t){i.removeProviderConfig(t),p.value=p.value.filter(n=>n.instance_id!=t)},h=function(t){P.push(`/settings/editprovider/${t}`)},B=function(t){if(t.depends_on&&!i.getProvider(t.depends_on)){const n=i.getProviderName(t.depends_on);confirm(l("settings.provider_depends_on_confirm",[t.name,n]))&&P.push(`/settings/addprovider/${t.depends_on}`);return}P.push(`/settings/addprovider/${t.domain}`)},N=function(t){t.enabled=!t.enabled,i.saveProviderConfig(t.domain,{enabled:t.enabled},t.instance_id)},E=function(t){i.sendCommand("config/providers/reload",{instance_id:t}).catch(n=>alert(n))},L=function(t){window.open(t,"_blank")},U=function(t,n){var e;const r=[{label:"settings.configure",labelArgs:[],action:()=>{h(n.instance_id)},icon:"mdi-cog"},{label:n.enabled?"settings.disable":"settings.enable",labelArgs:[],action:()=>{N(n)},icon:"mdi-cancel",disabled:!i.providerManifests[n.domain].allow_disable},{label:"settings.documentation",labelArgs:[],action:()=>{L(i.providerManifests[n.domain].documentation)},icon:"mdi-bookshelf",disabled:!i.providerManifests[n.domain].documentation},{label:"settings.sync",labelArgs:[],action:()=>{i.startSync(void 0,[n.instance_id])},icon:"mdi-sync",hide:!((e=i.providers[n.instance_id])!=null&&e.available)||n.type!=_.MUSIC},{label:"settings.delete",labelArgs:[],action:()=>{$(n.instance_id)},icon:"mdi-delete",hide:i.providerManifests[n.domain].builtin},{label:"settings.reload",labelArgs:[],action:()=>{E(n.instance_id)},icon:"mdi-refresh"}];K.emit("contextmenu",{items:r,posX:t.clientX,posY:t.clientY})};return O(()=>i.providers,t=>{t&&w()},{immediate:!0}),(t,n)=>(s(!0),v(M,null,C(a(_),r=>(s(),v("div",{key:r,style:{"margin-bottom":"10px"}},[d(T,{color:"transparent",density:"compact",class:"titlebar"},{title:o(()=>[f(u(a(l)(`settings.${r}providers`)),1)]),append:o(()=>[V.value.filter(e=>e.type==r).length?(s(),m(Q,{key:0,scrim:""},{activator:o(({props:e})=>[d(G,X({ref_for:!0},e,{color:"accent",variant:"outlined"}),{default:o(()=>[f(u(a(l)("settings.add_new_provider_button",[r])),1)]),_:2},1040)]),default:o(()=>[d(J,{density:"compact"},{default:o(()=>[(s(!0),v(M,null,C(V.value.filter(e=>e.type==r),e=>(s(),m(H,{key:e.domain,style:{"padding-top":"0","padding-bottom":"0","margin-bottom":"0"},title:e.name,onClick:c=>B(e)},{prepend:o(()=>[d(x,{domain:e.domain,size:26,class:"media-thumb",style:{"margin-left":"10px"}},null,8,["domain"])]),_:2},1032,["title","onClick"]))),128))]),_:2},1024)]),_:2},1024)):g("",!0)]),_:2},1024),r==a(_).MUSIC&&p.value.filter(e=>e.type==a(_).MUSIC&&e.domain in a(i).providerManifests&&e.domain!=="builtin").length==0?(s(),m(A,{key:0,border:"top","border-color":"warning",style:{margin:"20px"},icon:"mdi-alert-box-outline"},{default:o(()=>[b("b",null,u(a(l)("settings.no_music_providers_detail")),1),n[0]||(n[0]=b("br",null,null,-1)),f(" "+u(a(l)("settings.no_music_providers_detail")),1)]),_:1})):g("",!0),r==a(_).PLAYER&&p.value.filter(e=>e.type==a(_).PLAYER&&e.domain in a(i).providerManifests).length==0?(s(),m(A,{key:1,border:"top","border-color":"warning",style:{margin:"20px"},icon:"mdi-alert-box-outline"},{default:o(()=>[b("b",null,u(a(l)("settings.no_player_providers_detail")),1),n[1]||(n[1]=b("br",null,null,-1)),f(" "+u(a(l)("settings.no_player_providers_detail")),1)]),_:1})):g("",!0),d(q,null,{default:o(()=>[(s(!0),v(M,null,C(p.value.filter(e=>e.type==r),e=>(s(),m(W,{key:e.instance_id,"show-menu-btn":"",link:"",onMenu:c=>U(c,e),onClick:c=>h(e.instance_id)},{prepend:o(()=>[d(x,{domain:e.domain,size:50,class:"listitem-media-thumb",style:{"margin-top":"5px","margin-bottom":"5px"}},null,8,["domain"])]),title:o(()=>{var c;return[b("div",ee,u(e.name||((c=a(i).getProvider(e.instance_id))==null?void 0:c.name)||a(i).getProviderName(e.domain)),1)]}),subtitle:o(()=>[b("div",ne,u(a(i).providerManifests[e.domain].description),1)]),append:o(()=>{var c;return[a(i).syncTasks.value.filter(S=>S.provider_instance==e.instance_id).length>0?(s(),m(y,{key:0,icon:"",title:a(l)("settings.sync_running")},{default:o(()=>[d(k,{color:"grey"},{default:o(()=>n[2]||(n[2]=[f(" mdi-sync ")])),_:1})]),_:1},8,["title"])):g("",!0),e.enabled?e.last_error?(s(),m(y,{key:2,icon:"",title:e.last_error},{default:o(()=>[d(k,{color:"red"},{default:o(()=>n[4]||(n[4]=[f(" mdi-alert-circle ")])),_:1})]),_:2},1032,["title"])):(c=a(i).providers[e.instance_id])!=null&&c.available?g("",!0):(s(),m(y,{key:3,icon:"",title:a(l)("settings.not_loaded")},{default:o(()=>[d(k,{icon:"mdi-timer-sand"})]),_:1},8,["title"])):(s(),m(y,{key:1,icon:"",title:a(l)("settings.provider_disabled")},{default:o(()=>[d(k,{color:"grey"},{default:o(()=>n[3]||(n[3]=[f(" mdi-cancel ")])),_:1})]),_:1},8,["title"]))]}),_:2},1032,["onMenu","onClick"]))),128))]),_:2},1024)]))),128))}}),ge=Z(te,[["__scopeId","data-v-b7d87755"]]);export{ge as default};

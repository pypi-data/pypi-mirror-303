import{I as c}from"./ItemsListing-DDCqwz98.js";import{I as f,_ as v}from"./ProviderDetails.vue_vue_type_script_setup_true_lang-CKbr_gtC.js";import{d as h,r as y,K as I,c as a,h as g,f as w,e as m,j as n,g as V,b as s}from"./index-b2T7whGP.js";import{n as k}from"./VCheckbox-DqSGvg8-.js";import"./eventbus-COybQTbN.js";import"./VListItem-C1lr_U2J.js";import"./ListItem-WUZ7WMK6.js";import"./Button-ClofhSF-.js";import"./_plugin-vue_export-helper-DlAUqK2U.js";import"./VMenu-BWs87hpq.js";import"./VCard-BTd3uzfN.js";import"./VCardText-4hVjYKDN.js";import"./VSpacer-CC6R_IB-.js";/* empty css              */import"./PanelviewItemCompact-CbkeOszV.js";import"./VAlert-CoSmLIOG.js";import"./Container-B3nrNIr_.js";import"./Toolbar-CVekkGxc.js";import"./VToolbar-DuWNnIZ4.js";import"./VList-BoTr11ox.js";import"./VTextField-DZEZBcCw.js";import"./VCheckboxBtn-mlHCPMnc.js";import"./VInfiniteScroll-B2vaKHiY.js";import"./layout-BouSS8WH.js";import"./VVirtualScroll-Bg4-ObcJ.js";import"./VDialog-B9RfxB64.js";const W=h({__name:"RadioDetails",props:{itemId:{},provider:{}},setup(p){const t=p,e=y(),l=async function(){e.value=await s.getRadio(t.itemId,t.provider)};I(()=>t.itemId,i=>{i&&l()},{immediate:!0});const d=async function(i){const r=[];if(t.provider=="library"){const o=await s.getRadioVersions(t.itemId,t.provider);r.push(...o)}for(const o of k(e.value)){const u=await s.getRadioVersions(o.item_id,o.provider_instance);r.push(...u)}return r};return(i,r)=>(a(),g("section",null,[w(f,{item:e.value},null,8,["item"]),e.value?(a(),m(c,{key:0,itemtype:"radioversions","parent-item":e.value,"show-provider":!0,"show-favorites-only-filter":!1,"show-library":!1,"show-radio-number":!1,"show-duration":!1,"load-items":d,"sort-keys":["provider","sort_name"],title:i.$t("other_versions"),"hide-on-empty":!0,checksum:i.provider+i.itemId},null,8,["parent-item","title","checksum"])):n("",!0),r[0]||(r[0]=V("br",null,null,-1)),e.value?(a(),m(v,{key:1,"item-details":e.value},null,8,["item-details"])):n("",!0)]))}});export{W as default};

import{I as v}from"./ItemsListing-DDCqwz98.js";import{I as y,_ as h}from"./ProviderDetails.vue_vue_type_script_setup_true_lang-CKbr_gtC.js";import{d as k,r as m,K as I,o as _,b as r,a7 as b,a as w,c as i,h as D,f as g,e as p,j as n,F as E}from"./index-b2T7whGP.js";import"./VCheckbox-DqSGvg8-.js";import"./eventbus-COybQTbN.js";import"./VListItem-C1lr_U2J.js";import"./VCheckboxBtn-mlHCPMnc.js";import"./VList-BoTr11ox.js";import"./VCardText-4hVjYKDN.js";import"./VCard-BTd3uzfN.js";import"./VMenu-BWs87hpq.js";import"./_plugin-vue_export-helper-DlAUqK2U.js";import"./ListItem-WUZ7WMK6.js";import"./Button-ClofhSF-.js";import"./VSpacer-CC6R_IB-.js";/* empty css              */import"./PanelviewItemCompact-CbkeOszV.js";import"./VAlert-CoSmLIOG.js";import"./Container-B3nrNIr_.js";import"./Toolbar-CVekkGxc.js";import"./VToolbar-DuWNnIZ4.js";import"./VTextField-DZEZBcCw.js";import"./VInfiniteScroll-B2vaKHiY.js";import"./layout-BouSS8WH.js";import"./VVirtualScroll-Bg4-ObcJ.js";import"./VDialog-B9RfxB64.js";const Y=k({__name:"PlaylistDetails",props:{itemId:{},provider:{}},setup(u){const t=u,o=m(!1),e=m(),d=async function(){e.value=await r.getPlaylist(t.itemId,t.provider)};I(()=>t.itemId,a=>{a&&d()},{immediate:!0}),_(()=>{const a=r.subscribe(b.MEDIA_ITEM_UPDATED,s=>{var l;const f=s.data;((l=e.value)==null?void 0:l.uri)==f.uri&&(o.value=!0)});w(a)});const c=async function(a){return await r.getPlaylistTracks(t.itemId,t.provider,a.refresh)};return(a,s)=>(i(),D(E,null,[g(y,{item:e.value},null,8,["item"]),e.value?(i(),p(v,{key:0,itemtype:"playlisttracks","parent-item":e.value,"show-provider":!1,"show-library":!1,"show-favorites-only-filter":!1,"show-track-number":!1,"show-refresh-button":!0,"load-items":c,"sort-keys":["position","position_desc","name","artist","album","duration","duration_desc"],"update-available":o.value,title:a.$t("playlist_tracks"),"allow-key-hooks":!0,path:`playlist.${t.itemId}.${t.provider}`,"restore-state":!0,"no-server-side-sorting":!0},null,8,["parent-item","update-available","title","path"])):n("",!0),e.value?(i(),p(h,{key:1,"item-details":e.value},null,8,["item-details"])):n("",!0)],64))}});export{Y as default};

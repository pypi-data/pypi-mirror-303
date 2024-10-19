import{I as d}from"./ItemsListing-BwjD1tmq.js";import{I as k,_ as g}from"./ProviderDetails.vue_vue_type_script_setup_true_lang-B-vwm4W9.js";import{d as A,r as h,K as D,o as V,b as i,a7 as B,a as E,c as s,h as M,f as T,e as m,u as v,j as n,g as u}from"./index-CLKg64ON.js";import{M as U}from"./MediaItemImages-BexLeDzA.js";import"./VCheckbox-CpTv3BhW.js";import"./eventbus-D-xzWv8v.js";import"./VListItem-B_TSjQ1y.js";import"./VCheckboxBtn-DXJHHMHd.js";import"./VList-BvG6-yh2.js";import"./VCardText-BAUfdzDA.js";import"./VCard-BaRPabiE.js";import"./VMenu-CLSWQG_U.js";import"./_plugin-vue_export-helper-DlAUqK2U.js";import"./ListItem-f79Nhqh7.js";import"./Button-F8l3l_P8.js";import"./VSpacer-CqqJVVs3.js";/* empty css              */import"./PanelviewItemCompact-CM48-dMH.js";import"./VAlert-CCGDAWu2.js";import"./Container-ZPskS02H.js";import"./Toolbar-BaIn3BvJ.js";import"./VToolbar-DSn0RyUD.js";import"./VTextField-C1QkMZRy.js";import"./VInfiniteScroll-pn5EaZ8a.js";import"./layout-CYdR31l5.js";import"./VVirtualScroll-DKBgr9yN.js";import"./VDialog-BpGrcp5y.js";const it=A({__name:"ArtistDetails",props:{itemId:{},provider:{}},setup(f){const a=f,t=h(),y=async function(){t.value=await i.getArtist(a.itemId,a.provider)};D(()=>a.itemId,r=>{r&&y()},{immediate:!0}),V(()=>{const r=i.subscribe(B.MEDIA_ITEM_UPDATED,e=>{var l;const o=e.data;((l=t.value)==null?void 0:l.uri)==o.uri&&(t.value=o)});E(r)});const b=async function(r){return await i.getArtistAlbums(a.itemId,a.provider,r.libraryOnly)},c=async function(r){return await i.getArtistTracks(a.itemId,a.provider,r.libraryOnly)},w=async function(){t.value&&(t.value=await i.sendCommand("music/artists/update",{item_id:t.value.item_id,update:t.value,overwrite:!0}))};return(r,e)=>{var o,l,p;return s(),M("section",null,[T(k,{item:t.value},null,8,["item"]),t.value?(s(),m(d,{key:0,itemtype:"artistalbums","parent-item":t.value,"show-provider":!0,"show-favorites-only-filter":!0,"show-library-only-filter":t.value.provider=="library"&&v(i).hasStreamingProviders.value,"show-album-type-filter":!0,"show-refresh-button":!1,"load-items":b,"sort-keys":["name","sort_name","year"],title:r.$t("albums"),"allow-collapse":!0},null,8,["parent-item","show-library-only-filter","title"])):n("",!0),e[1]||(e[1]=u("br",null,null,-1)),t.value?(s(),m(d,{key:1,itemtype:"artisttracks","parent-item":t.value,"show-provider":!0,"show-favorites-only-filter":!0,"show-library-only-filter":t.value.provider=="library"&&v(i).hasStreamingProviders.value,"show-refresh-button":!1,"show-track-number":!1,"load-items":c,"sort-keys":["name","sort_name","album"],title:r.$t("tracks"),"allow-collapse":!0},null,8,["parent-item","show-library-only-filter","title"])):n("",!0),e[2]||(e[2]=u("br",null,null,-1)),((o=t.value)==null?void 0:o.provider)=="library"&&((p=(l=t.value)==null?void 0:l.metadata)!=null&&p.images)?(s(),m(U,{key:2,modelValue:t.value.metadata.images,"onUpdate:modelValue":[e[0]||(e[0]=I=>t.value.metadata.images=I),w]},null,8,["modelValue"])):n("",!0),e[3]||(e[3]=u("br",null,null,-1)),t.value?(s(),m(g,{key:3,"item-details":t.value},null,8,["item-details"])):n("",!0),e[4]||(e[4]=u("br",null,null,-1))])}}});export{it as default};

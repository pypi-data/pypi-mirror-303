import{I as y}from"./ItemsListing-BwjD1tmq.js";import{d as v,r as l,s as c,o as b,b as a,a7 as n,a as k,c as T,h,f as d,u as E,F as w,M as u}from"./index-CLKg64ON.js";import{_ as D}from"./AddManualLink.vue_vue_type_script_setup_true_lang-Cxci0dbg.js";import{s as m}from"./VCheckbox-CpTv3BhW.js";import"./eventbus-D-xzWv8v.js";import"./VListItem-B_TSjQ1y.js";import"./ListItem-f79Nhqh7.js";import"./Button-F8l3l_P8.js";import"./_plugin-vue_export-helper-DlAUqK2U.js";import"./VMenu-CLSWQG_U.js";import"./VCard-BaRPabiE.js";import"./VCardText-BAUfdzDA.js";import"./VSpacer-CqqJVVs3.js";/* empty css              */import"./PanelviewItemCompact-CM48-dMH.js";import"./VAlert-CCGDAWu2.js";import"./Container-ZPskS02H.js";import"./Toolbar-BaIn3BvJ.js";import"./VToolbar-DSn0RyUD.js";import"./VList-BvG6-yh2.js";import"./VTextField-C1QkMZRy.js";import"./VCheckboxBtn-DXJHHMHd.js";import"./VInfiniteScroll-pn5EaZ8a.js";import"./layout-CYdR31l5.js";import"./VVirtualScroll-DKBgr9yN.js";import"./VDialog-BpGrcp5y.js";const Y=v({name:"Tracks",__name:"LibraryTracks",setup(A){const o=l(!1),r=l(c.libraryTracksCount),i=l(!1),p=["name","name_desc","sort_name","sort_name_desc","duration","duration_desc","timestamp_added","timestamp_added_desc","last_played","last_played_desc","play_count","play_count_desc"];b(()=>{const t=a.subscribe_multi([n.MEDIA_ITEM_ADDED,n.MEDIA_ITEM_UPDATED,n.MEDIA_ITEM_DELETED],e=>{var s;(s=e.object_id)!=null&&s.startsWith("library://track")&&(o.value=!0)});k(t)});const f=async function(t){if(t.favoritesOnly=t.favoritesOnly||void 0,t.refresh&&!o.value){for(a.startSync([u.TRACK]),await m(250);a.syncTasks.value.length>0&&a.syncTasks.value.filter(e=>e.media_types.includes(u.TRACK)).length!=0;)await m(500);await m(500)}return o.value=!1,_(t),await a.getLibraryTracks(t.favoritesOnly,t.search,t.limit,t.offset,t.sortBy)},_=async function(t){if(!t.favoritesOnly){r.value=c.libraryTracksCount;return}r.value=await a.getLibraryTracksCount(t.favoritesOnly||!1)};return(t,e)=>(T(),h(w,null,[d(y,{itemtype:"tracks","show-provider":!1,"show-favorites-only-filter":!0,"show-track-number":!1,"load-paged-data":f,"sort-keys":p,"show-album":!0,"update-available":o.value,title:t.$t("tracks"),"show-search-button":!0,"allow-key-hooks":!0,"extra-menu-items":[{label:"add_url_item",labelArgs:[],action:()=>{i.value=!0},icon:"mdi-playlist-plus"}],icon:"mdi-music-note","restore-state":!0,total:r.value},null,8,["update-available","title","extra-menu-items","total"]),d(D,{modelValue:i.value,"onUpdate:modelValue":e[0]||(e[0]=s=>i.value=s),type:E(u).RADIO},null,8,["modelValue","type"])],64))}});export{Y as default};

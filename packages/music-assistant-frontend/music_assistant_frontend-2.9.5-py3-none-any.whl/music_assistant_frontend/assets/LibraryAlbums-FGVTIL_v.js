import{I as y}from"./ItemsListing-DDCqwz98.js";import{d as _,r as n,s as m,o as b,b as e,a7 as i,a as f,c as v,e as A,M as u}from"./index-b2T7whGP.js";import{s as r}from"./VCheckbox-DqSGvg8-.js";import"./eventbus-COybQTbN.js";import"./VListItem-C1lr_U2J.js";import"./ListItem-WUZ7WMK6.js";import"./Button-ClofhSF-.js";import"./_plugin-vue_export-helper-DlAUqK2U.js";import"./VMenu-BWs87hpq.js";import"./VCard-BTd3uzfN.js";import"./VCardText-4hVjYKDN.js";import"./VSpacer-CC6R_IB-.js";/* empty css              */import"./PanelviewItemCompact-CbkeOszV.js";import"./VAlert-CoSmLIOG.js";import"./Container-B3nrNIr_.js";import"./Toolbar-CVekkGxc.js";import"./VToolbar-DuWNnIZ4.js";import"./VList-BoTr11ox.js";import"./VTextField-DZEZBcCw.js";import"./VCheckboxBtn-mlHCPMnc.js";import"./VInfiniteScroll-B2vaKHiY.js";import"./layout-BouSS8WH.js";import"./VVirtualScroll-Bg4-ObcJ.js";const H=_({name:"Albums",__name:"LibraryAlbums",setup(h){const o=n(!1),s=n(m.libraryAlbumsCount),p=["name","name_desc","sort_name","sort_name_desc","year","year_desc","timestamp_added","timestamp_added_desc","last_played","last_played_desc","play_count","play_count_desc","artist_name","artist_name_desc"];b(()=>{const t=e.subscribe_multi([i.MEDIA_ITEM_ADDED,i.MEDIA_ITEM_UPDATED,i.MEDIA_ITEM_DELETED],a=>{var l;(l=a.object_id)!=null&&l.startsWith("library://artist")&&(o.value=!0)});f(t)});const c=async function(t){if(t.refresh){for(e.startSync([u.ALBUM]),await r(250);e.syncTasks.value.length>0&&e.syncTasks.value.filter(a=>a.media_types.includes(u.ALBUM)).length!=0;)await r(500);await r(500)}return o.value=!1,d(t),await e.getLibraryAlbums(t.favoritesOnly||void 0,t.search,t.limit,t.offset,t.sortBy,t.albumType)},d=async function(t){if(!t.favoritesOnly&&!t.albumType){s.value=m.libraryAlbumsCount;return}s.value=await e.getLibraryAlbumsCount(t.favoritesOnly||void 0,t.albumType||void 0)};return(t,a)=>(v(),A(y,{itemtype:"albums","show-provider":!1,"show-favorites-only-filter":!0,"load-paged-data":c,"sort-keys":p,"update-available":o.value,title:t.$t("albums"),"allow-key-hooks":!0,"show-search-button":!0,icon:"mdi-album","restore-state":!0,total:s.value,"show-album-type-filter":!0},null,8,["update-available","title","total"]))}});export{H as default};

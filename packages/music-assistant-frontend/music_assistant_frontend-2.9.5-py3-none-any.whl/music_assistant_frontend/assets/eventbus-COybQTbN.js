import{d as p,x as m,b as r,c as s,h as l,e as d,u as a,_ as u}from"./index-b2T7whGP.js";import{w as v}from"./VListItem-C1lr_U2J.js";const c=["title","innerHTML"],f=["title","innerHTML"],h=p({__name:"ProviderIcon",props:{domain:{},size:{},dark:{type:Boolean}},setup(t){const n=t,i=m(()=>{if(n.domain in r.providers)return r.providers[n.domain].domain;if(n.domain in r.providerManifests)return n.domain});return(e,o)=>(s(),l("div",{style:u(`width:${e.size}px;margin-left:10px;margin-right:10px;content-align:center`)},[e.domain&&e.domain=="library"?(s(),d(v,{key:0,size:e.size,icon:"mdi-bookshelf",title:e.$t("item_in_library")},null,8,["size","title"])):e.$vuetify.theme.current.dark&&i.value&&a(r).providerManifests[i.value].icon_svg_dark?(s(),l("div",{key:1,style:u(`width: ${e.size}px;align-content: center;`),title:a(r).providerManifests[i.value].name,innerHTML:a(r).providerManifests[i.value].icon_svg_dark},null,12,c)):i.value&&a(r).providerManifests[i.value].icon_svg?(s(),l("div",{key:2,style:u(`width: ${e.size}px;height: ${e.size}px;align-content: center;`),title:a(r).providerManifests[i.value].name,innerHTML:a(r).providerManifests[i.value].icon_svg},null,12,f)):i.value&&a(r).providerManifests[i.value].icon?(s(),d(v,{key:3,size:e.size,icon:"mdi-"+a(r).providerManifests[i.value].icon,title:a(r).providerManifests[i.value].name,dark:e.$vuetify.theme.current.dark},null,8,["size","icon","title","dark"])):(s(),d(v,{key:4,size:e.size,dark:e.$vuetify.theme.current.dark,icon:"mdi-playlist-play"},null,8,["size","dark"]))],4))}});function k(t){return{all:t=t||new Map,on:function(n,i){var e=t.get(n);e?e.push(i):t.set(n,[i])},off:function(n,i){var e=t.get(n);e&&(i?e.splice(e.indexOf(i)>>>0,1):t.set(n,[]))},emit:function(n,i){var e=t.get(n);e&&e.slice().map(function(o){o(i)}),(e=t.get("*"))&&e.slice().map(function(o){o(n,i)})}}}const z=k();export{h as _,z as e};

import{d as D,h,b as L,c as m,f as A}from"./VMenu-CLSWQG_U.js";import{p as S,k as x,y as w,r as B,aL as F,K as g,S as I,D as f,f as p,aW as R}from"./index-CLKg64ON.js";import{c as T,K as O}from"./VListItem-B_TSjQ1y.js";const k=S({fullscreen:Boolean,retainFocus:{type:Boolean,default:!0},scrollable:Boolean,...D({origin:"center center",scrollStrategy:"block",transition:{component:h},zIndex:2400})},"VDialog"),W=x()({name:"VDialog",props:k(),emits:{"update:modelValue":a=>!0,afterEnter:()=>!0,afterLeave:()=>!0},setup(a,E){let{emit:v,slots:u}=E;const i=w(a,"modelValue"),{scopeId:V}=L(),e=B();function d(t){var r,s;const n=t.relatedTarget,l=t.target;if(n!==l&&((r=e.value)!=null&&r.contentEl)&&((s=e.value)!=null&&s.globalTop)&&![document,e.value.contentEl].includes(l)&&!e.value.contentEl.contains(l)){const o=R(e.value.contentEl);if(!o.length)return;const c=o[0],y=o[o.length-1];n===c?y.focus():c.focus()}}F&&g(()=>i.value&&a.retainFocus,t=>{t?document.addEventListener("focusin",d):document.removeEventListener("focusin",d)},{immediate:!0});function P(){var t;v("afterEnter"),(t=e.value)!=null&&t.contentEl&&!e.value.contentEl.contains(document.activeElement)&&e.value.contentEl.focus({preventScroll:!0})}function b(){v("afterLeave")}return g(i,async t=>{var n;t||(await I(),(n=e.value.activatorEl)==null||n.focus({preventScroll:!0}))}),T(()=>{const t=m.filterProps(a),n=f({"aria-haspopup":"dialog"},a.activatorProps),l=f({tabindex:-1},a.contentProps);return p(m,f({ref:e,class:["v-dialog",{"v-dialog--fullscreen":a.fullscreen,"v-dialog--scrollable":a.scrollable},a.class],style:a.style},t,{modelValue:i.value,"onUpdate:modelValue":r=>i.value=r,"aria-modal":"true",activatorProps:n,contentProps:l,role:"dialog",onAfterEnter:P,onAfterLeave:b},V),{activator:u.activator,default:function(){for(var r=arguments.length,s=new Array(r),o=0;o<r;o++)s[o]=arguments[o];return p(O,{root:"VDialog"},{default:()=>{var c;return[(c=u.default)==null?void 0:c.call(u,...s)]}})}})}),A({},e)}});export{W as V};

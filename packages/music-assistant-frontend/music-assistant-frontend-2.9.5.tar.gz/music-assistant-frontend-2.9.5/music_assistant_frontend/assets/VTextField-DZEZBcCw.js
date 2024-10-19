import{p as O,k as U,x as u,f as l,N as Z,R as le,ay as H,aY as X,n as ue,G as de,H as ce,ap as fe,r as T,v as ve,K as me,B as ye,F as M,D as N,aZ as ge,aV as be,y as xe,ax as Ce,O as ke,a_ as Ve,S as p,a$ as he}from"./index-b2T7whGP.js";import{m as J,N as _e,$ as Ie,c as K,M as Pe,Y as Fe,g as Se,S as Be,n as we,j as Re,r as Te,U as Le,a0 as $e,K as Ae,a1 as De}from"./VListItem-C1lr_U2J.js";import{i as Ee,j as Me,u as te,n as Ne,b as Oe,d as ee}from"./VCheckboxBtn-mlHCPMnc.js";import{n as Ue,a as Ke,s as je,f as Ye}from"./VMenu-BWs87hpq.js";const We=O({active:Boolean,disabled:Boolean,max:[Number,String],value:{type:[Number,String],default:0},...J(),..._e({transition:{component:Ie}})},"VCounter"),qe=U()({name:"VCounter",functional:!0,props:We(),setup(e,y){let{slots:i}=y;const P=u(()=>e.max?`${e.value} / ${e.max}`:String(e.value));return K(()=>l(Pe,{transition:e.transition},{default:()=>[Z(l("div",{class:["v-counter",{"text-error":e.max&&!e.disabled&&parseFloat(e.value)>parseFloat(e.max)},e.class],style:e.style},[i.default?i.default({counter:P.value,max:e.max,value:e.value}):P.value]),[[le,e.active]])]})),{}}}),ze=O({floating:Boolean,...J()},"VFieldLabel"),E=U()({name:"VFieldLabel",props:ze(),setup(e,y){let{slots:i}=y;return K(()=>l(Ee,{class:["v-field-label",{"v-field-label--floating":e.floating},e.class],style:e.style,"aria-hidden":e.floating||void 0},i)),{}}}),Ge=["underlined","outlined","filled","solo","solo-inverted","solo-filled","plain"],ne=O({appendInnerIcon:H,bgColor:String,clearable:Boolean,clearIcon:{type:H,default:"$clear"},active:Boolean,centerAffix:{type:Boolean,default:void 0},color:String,baseColor:String,dirty:Boolean,disabled:{type:Boolean,default:null},error:Boolean,flat:Boolean,label:String,persistentClear:Boolean,prependInnerIcon:H,reverse:Boolean,singleLine:Boolean,variant:{type:String,default:"filled",validator:e=>Ge.includes(e)},"onClick:clear":X(),"onClick:appendInner":X(),"onClick:prependInner":X(),...J(),...Fe(),...Se(),...ue()},"VField"),ae=U()({name:"VField",inheritAttrs:!1,props:{id:String,...Me(),...ne()},emits:{"update:focused":e=>!0,"update:modelValue":e=>!0},setup(e,y){let{attrs:i,emit:P,slots:t}=y;const{themeClasses:g}=de(e),{loaderClasses:C}=Be(e),{focusClasses:j,isFocused:L,focus:F,blur:S}=te(e),{InputIcon:B}=Ne(e),{roundedClasses:Y}=we(e),{rtlClasses:$}=ce(),k=u(()=>e.dirty||e.active),f=u(()=>!e.singleLine&&!!(e.label||t.label)),W=fe(),s=u(()=>e.id||`input-${W}`),q=u(()=>`${s.value}-messages`),A=T(),w=T(),D=T(),n=u(()=>["plain","underlined"].includes(e.variant)),{backgroundColorClasses:d,backgroundColorStyles:c}=Re(ve(e,"bgColor")),{textColorClasses:v,textColorStyles:z}=Te(u(()=>e.error||e.disabled?void 0:k.value&&L.value?e.color:e.baseColor));me(k,a=>{if(f.value){const o=A.value.$el,m=w.value.$el;requestAnimationFrame(()=>{const b=Ue(o),r=m.getBoundingClientRect(),R=r.x-b.x,h=r.y-b.y-(b.height/2-r.height/2),_=r.width/.75,I=Math.abs(_-b.width)>1?{maxWidth:ye(_)}:void 0,ie=getComputedStyle(o),Q=getComputedStyle(m),oe=parseFloat(ie.transitionDuration)*1e3||150,se=parseFloat(Q.getPropertyValue("--v-field-label-scale")),re=Q.getPropertyValue("color");o.style.visibility="visible",m.style.visibility="hidden",Ke(o,{transform:`translate(${R}px, ${h}px) scale(${se})`,color:re,...I},{duration:oe,easing:je,direction:a?"normal":"reverse"}).finished.then(()=>{o.style.removeProperty("visibility"),m.style.removeProperty("visibility")})})}},{flush:"post"});const V=u(()=>({isActive:k,isFocused:L,controlRef:D,blur:S,focus:F}));function G(a){a.target!==document.activeElement&&a.preventDefault()}function x(a){var o;a.key!=="Enter"&&a.key!==" "||(a.preventDefault(),a.stopPropagation(),(o=e["onClick:clear"])==null||o.call(e,new MouseEvent("click")))}return K(()=>{var R,h,_;const a=e.variant==="outlined",o=!!(t["prepend-inner"]||e.prependInnerIcon),m=!!(e.clearable||t.clear),b=!!(t["append-inner"]||e.appendInnerIcon||m),r=()=>t.label?t.label({...V.value,label:e.label,props:{for:s.value}}):e.label;return l("div",N({class:["v-field",{"v-field--active":k.value,"v-field--appended":b,"v-field--center-affix":e.centerAffix??!n.value,"v-field--disabled":e.disabled,"v-field--dirty":e.dirty,"v-field--error":e.error,"v-field--flat":e.flat,"v-field--has-background":!!e.bgColor,"v-field--persistent-clear":e.persistentClear,"v-field--prepended":o,"v-field--reverse":e.reverse,"v-field--single-line":e.singleLine,"v-field--no-label":!r(),[`v-field--variant-${e.variant}`]:!0},g.value,d.value,j.value,C.value,Y.value,$.value,e.class],style:[c.value,e.style],onClick:G},i),[l("div",{class:"v-field__overlay"},null),l(Le,{name:"v-field",active:!!e.loading,color:e.error?"error":typeof e.loading=="string"?e.loading:e.color},{default:t.loader}),o&&l("div",{key:"prepend",class:"v-field__prepend-inner"},[e.prependInnerIcon&&l(B,{key:"prepend-icon",name:"prependInner"},null),(R=t["prepend-inner"])==null?void 0:R.call(t,V.value)]),l("div",{class:"v-field__field","data-no-activator":""},[["filled","solo","solo-inverted","solo-filled"].includes(e.variant)&&f.value&&l(E,{key:"floating-label",ref:w,class:[v.value],floating:!0,for:s.value,style:z.value},{default:()=>[r()]}),l(E,{ref:A,for:s.value},{default:()=>[r()]}),(h=t.default)==null?void 0:h.call(t,{...V.value,props:{id:s.value,class:"v-field__input","aria-describedby":q.value},focus:F,blur:S})]),m&&l($e,{key:"clear"},{default:()=>[Z(l("div",{class:"v-field__clearable",onMousedown:I=>{I.preventDefault(),I.stopPropagation()}},[l(Ae,{defaults:{VIcon:{icon:e.clearIcon}}},{default:()=>[t.clear?t.clear({...V.value,props:{onKeydown:x,onFocus:F,onBlur:S,onClick:e["onClick:clear"]}}):l(B,{name:"clear",onKeydown:x,onFocus:F,onBlur:S},null)]})]),[[le,e.dirty]])]}),b&&l("div",{key:"append",class:"v-field__append-inner"},[(_=t["append-inner"])==null?void 0:_.call(t,V.value),e.appendInnerIcon&&l(B,{key:"append-icon",name:"appendInner"},null)]),l("div",{class:["v-field__outline",v.value],style:z.value},[a&&l(M,null,[l("div",{class:"v-field__outline__start"},null),f.value&&l("div",{class:"v-field__outline__notch"},[l(E,{ref:w,floating:!0,for:s.value},{default:()=>[r()]})]),l("div",{class:"v-field__outline__end"},null)]),n.value&&f.value&&l(E,{ref:w,floating:!0,for:s.value},{default:()=>[r()]})])])}),{controlRef:D}}});function He(e){const y=Object.keys(ae.props).filter(i=>!ge(i)&&i!=="class"&&i!=="style");return be(e,y)}const Xe=["color","file","time","date","datetime-local","week","month"],Ze=O({autofocus:Boolean,counter:[Boolean,Number,String],counterValue:[Number,Function],prefix:String,placeholder:String,persistentPlaceholder:Boolean,persistentCounter:Boolean,suffix:String,role:String,type:{type:String,default:"text"},modelModifiers:Object,...Oe(),...ne()},"VTextField"),ll=U()({name:"VTextField",directives:{Intersect:De},inheritAttrs:!1,props:Ze(),emits:{"click:control":e=>!0,"mousedown:control":e=>!0,"update:focused":e=>!0,"update:modelValue":e=>!0},setup(e,y){let{attrs:i,emit:P,slots:t}=y;const g=xe(e,"modelValue"),{isFocused:C,focus:j,blur:L}=te(e),F=u(()=>typeof e.counterValue=="function"?e.counterValue(g.value):typeof e.counterValue=="number"?e.counterValue:(g.value??"").toString().length),S=u(()=>{if(i.maxlength)return i.maxlength;if(!(!e.counter||typeof e.counter!="number"&&typeof e.counter!="string"))return e.counter}),B=u(()=>["plain","underlined"].includes(e.variant));function Y(n,d){var c,v;!e.autofocus||!n||(v=(c=d[0].target)==null?void 0:c.focus)==null||v.call(c)}const $=T(),k=T(),f=T(),W=u(()=>Xe.includes(e.type)||e.persistentPlaceholder||C.value||e.active);function s(){var n;f.value!==document.activeElement&&((n=f.value)==null||n.focus()),C.value||j()}function q(n){P("mousedown:control",n),n.target!==f.value&&(s(),n.preventDefault())}function A(n){s(),P("click:control",n)}function w(n){n.stopPropagation(),s(),p(()=>{g.value=null,he(e["onClick:clear"],n)})}function D(n){var c;const d=n.target;if(g.value=d.value,(c=e.modelModifiers)!=null&&c.trim&&["text","search","password","tel","url"].includes(e.type)){const v=[d.selectionStart,d.selectionEnd];p(()=>{d.selectionStart=v[0],d.selectionEnd=v[1]})}}return K(()=>{const n=!!(t.counter||e.counter!==!1&&e.counter!=null),d=!!(n||t.details),[c,v]=Ce(i),{modelValue:z,...V}=ee.filterProps(e),G=He(e);return l(ee,N({ref:$,modelValue:g.value,"onUpdate:modelValue":x=>g.value=x,class:["v-text-field",{"v-text-field--prefixed":e.prefix,"v-text-field--suffixed":e.suffix,"v-input--plain-underlined":B.value},e.class],style:e.style},c,V,{centerAffix:!B.value,focused:C.value}),{...t,default:x=>{let{id:a,isDisabled:o,isDirty:m,isReadonly:b,isValid:r}=x;return l(ae,N({ref:k,onMousedown:q,onClick:A,"onClick:clear":w,"onClick:prependInner":e["onClick:prependInner"],"onClick:appendInner":e["onClick:appendInner"],role:e.role},G,{id:a.value,active:W.value||m.value,dirty:m.value||e.dirty,disabled:o.value,focused:C.value,error:r.value===!1}),{...t,default:R=>{let{props:{class:h,..._}}=R;const I=Z(l("input",N({ref:f,value:g.value,onInput:D,autofocus:e.autofocus,readonly:b.value,disabled:o.value,name:e.name,placeholder:e.placeholder,size:1,type:e.type,onFocus:s,onBlur:L},_,v),null),[[ke("intersect"),{handler:Y},null,{once:!0}]]);return l(M,null,[e.prefix&&l("span",{class:"v-text-field__prefix"},[l("span",{class:"v-text-field__prefix__text"},[e.prefix])]),t.default?l("div",{class:h,"data-no-activator":""},[t.default(),I]):Ve(I,{class:h}),e.suffix&&l("span",{class:"v-text-field__suffix"},[l("span",{class:"v-text-field__suffix__text"},[e.suffix])])])}})},details:d?x=>{var a;return l(M,null,[(a=t.details)==null?void 0:a.call(t,x),n&&l(M,null,[l("span",null,null),l(qe,{active:e.persistentCounter||C.value,value:F.value,max:S.value,disabled:e.disabled},t.counter)])])}:void 0})}),Ye({},$,k,f)}});export{ll as V,Ze as m};

webpackJsonp([1],{Akd7:function(t,a){},AqYs:function(t,a,e){t.exports=e.p+"static/img/logo.18b1b86.svg"},"FrR/":function(t,a){},"KOQ+":function(t,a){},Mqeg:function(t,a){},NHnr:function(t,a,e){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var s=e("7+uW"),o={render:function(){var t=this.$createElement,a=this._self._c||t;return a("nav",[a("router-link",{staticClass:"smallLogo",attrs:{to:"/"}},[a("img",{attrs:{src:e("AqYs"),alt:"TUV Logo"}})])],1)},staticRenderFns:[]};var n=e("VU/8")({name:"Topnav"},o,!1,function(t){e("Akd7")},"data-v-25f1df9a",null).exports,i=e("mtWM"),r=e.n(i),c={name:"Sidenav",methods:{fileOpen:function(t){t.preventDefault(),r.a.post("http://localhost:5000/submit/fileopen")}}},l={render:function(){var t=this.$createElement,a=this._self._c||t;return a("nav",[a("router-link",{attrs:{to:"/reports"}},[a("div",{staticClass:"sideNavButton"},[a("i",[a("font-awesome-icon",{attrs:{icon:"file-alt"}})],1)])]),this._v(" "),a("router-link",{attrs:{to:"/verifications"}},[a("div",{staticClass:"sideNavButton"},[a("i",[a("font-awesome-icon",{attrs:{icon:"clipboard-check"}})],1)])]),this._v(" "),a("router-link",{attrs:{to:"/environmental"}},[a("div",{staticClass:"sideNavButton"},[a("i",[a("font-awesome-icon",{attrs:{icon:"thermometer-half"}})],1)])]),this._v(" "),a("form",{staticClass:"sideNavButton bottomButton",attrs:{method:"POST"},on:{submit:this.fileOpen}},[a("button",[a("i",[a("font-awesome-icon",{attrs:{icon:"folder-open"}})],1)])]),this._v(" "),a("div",{staticClass:"sideNavButton"},[a("i",[a("font-awesome-icon",{attrs:{icon:"angle-right"}})],1)])],1)},staticRenderFns:[]};var v={name:"App",components:{Topnav:n,Sidenav:e("VU/8")(c,l,!1,function(t){e("KOQ+")},"data-v-db9732ca",null).exports}},m={render:function(){var t=this.$createElement,a=this._self._c||t;return a("div",{attrs:{id:"app"}},[a("div",[a("Topnav")],1),this._v(" "),a("div",[a("Sidenav")],1),this._v(" "),a("div",[a("transition",{attrs:{name:"show"}},[a("router-view")],1)],1)])},staticRenderFns:[]};var u=e("VU/8")(v,m,!1,function(t){e("QDHz")},null,null).exports,d=e("/ocq"),p={render:function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("div",{staticClass:"sectionContainer"},[e("div",{staticClass:"colContainer"},[t._m(0),t._v(" "),e("hr"),t._v(" "),e("div",{staticClass:"homeButtonContainer"},[e("router-link",{staticClass:"homeButton",attrs:{to:"/reports"}},[e("font-awesome-icon",{staticClass:"bigIcon",attrs:{icon:"file-alt"}}),t._v(" "),e("div",{staticClass:"startContainer"},[e("h3",{staticClass:"startSubtitle"},[e("strong",[t._v("Report Creation")])]),t._v(" "),e("hr"),t._v(" "),e("div",{staticClass:"startContent"},[e("p",[t._v("\n                            Automated Data Processing for:\n                        ")]),t._v(" "),e("ul",[e("li",[t._v("EMC Reports")]),t._v(" "),e("li",[t._v("Findings Letters")]),t._v(" "),e("li",[t._v("Prescan Data")])])])])],1),t._v(" "),e("router-link",{staticClass:"homeButton",attrs:{to:"/verifications"}},[e("font-awesome-icon",{staticClass:"bigIcon",attrs:{icon:"clipboard-check"}}),t._v(" "),e("div",{staticClass:"startContainer"},[e("h3",{staticClass:"startSubtitle"},[e("strong",[t._v("Equipment Verification")])]),t._v(" "),e("hr"),t._v(" "),e("div",{staticClass:"startContent"},[e("p",[t._v("\n                            Automated Generation of:\n                        ")]),t._v(" "),e("ul",[e("li",[t._v("Equipment Verification Forms")]),t._v(" "),e("li",[t._v("Test Setup Verification Trends")]),t._v(" "),e("li",[t._v("Verification Procedures")])])])])],1),t._v(" "),e("router-link",{staticClass:"homeButton",attrs:{to:"/environmental"}},[e("font-awesome-icon",{staticClass:"bigIcon",attrs:{icon:"thermometer-half"}}),t._v(" "),e("div",{staticClass:"startContainer"},[e("h3",{staticClass:"startSubtitle"},[e("strong",[t._v("Environmental Conditions")])]),t._v(" "),e("hr"),t._v(" "),e("div",{staticClass:"startContent"},[e("p",[t._v("\n                            Automated Database for Use in:\n                        ")]),t._v(" "),e("ul",[e("li",[t._v("EMC Reports")]),t._v(" "),e("li",[t._v("Verification Records")]),t._v(" "),e("li",[t._v("Laboratory Regulation")])])])])],1)],1)])])},staticRenderFns:[function(){var t=this.$createElement,a=this._self._c||t;return a("div",{staticClass:"title"},[a("img",{staticClass:"bigLogo",attrs:{src:e("oBrg"),alt:"TUV Logo"}}),this._v(" "),a("h1",[this._v("EMC Hub")])])}]};var f=e("VU/8")({name:"Home"},p,!1,function(t){e("j7bV")},"data-v-0ddc8f36",null).exports,_={render:function(){var t=this.$createElement,a=this._self._c||t;return a("div",{staticClass:"sectionContainer"},[a("router-link",{staticClass:"colContainer plusIconContainer",attrs:{to:"/reports/create"}},[a("i",[a("font-awesome-icon",{staticClass:"plusIcon",attrs:{icon:"plus"}})],1)]),this._v(" "),this._m(0),this._v(" "),this._m(1),this._v(" "),this._m(2)],1)},staticRenderFns:[function(){var t=this.$createElement,a=this._self._c||t;return a("div",{staticClass:"colContainer widgetOne"},[a("div",{staticClass:"subtitle"},[this._v("\n            Report Widget 1\n        ")]),this._v(" "),a("hr")])},function(){var t=this.$createElement,a=this._self._c||t;return a("div",{staticClass:"colContainer widgetTwo"},[a("div",{staticClass:"subtitle"},[this._v("\n            Report Widget 2\n        ")]),this._v(" "),a("hr")])},function(){var t=this.$createElement,a=this._self._c||t;return a("div",{staticClass:"colContainer widgetThree"},[a("div",{staticClass:"subtitle"},[this._v("\n            Report Widget 3\n        ")]),this._v(" "),a("hr")])}]};var C=e("VU/8")({name:"ReportLanding"},_,!1,function(t){e("FrR/")},"data-v-54f42eea",null).exports,h={render:function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("div",{staticClass:"sectionContainer"},[e("div",{staticClass:"colContainer optionOne"},[e("div",{staticClass:"subtitle"},[t._v("\n            EMC Report\n        ")]),t._v(" "),e("hr"),t._v(" "),e("router-link",{staticClass:"optionButtonContainer",attrs:{to:"/reports/create/report"}},[e("button",{attrs:{type:"button"}},[t._v("Create")])])],1),t._v(" "),e("div",{staticClass:"colContainer optionTwo"},[e("div",{staticClass:"subtitle"},[t._v("\n            Findings Letter\n        ")]),t._v(" "),e("hr"),t._v(" "),e("router-link",{staticClass:"optionButtonContainer",attrs:{to:"/reports/create/findings"}},[e("button",{attrs:{type:"button"}},[t._v("Create")])])],1),t._v(" "),e("div",{staticClass:"colContainer optionThree"},[e("div",{staticClass:"subtitle"},[t._v("\n            Raw Data\n        ")]),t._v(" "),e("hr"),t._v(" "),e("router-link",{staticClass:"optionButtonContainer",attrs:{to:"/reports/create/data"}},[e("button",{attrs:{type:"button"}},[t._v("Create")])])],1)])},staticRenderFns:[]};var b=e("VU/8")({name:"ReportCreation"},h,!1,function(t){e("Mqeg")},"data-v-3aa2810a",null).exports,g={name:"ReportForm",data:function(){return{formData:{productName:"",companyName:"",data:""},standard:"Select...",currentWindow:0,buttonPrevious:!1,buttonSubmit:!1,buttonNext:!0,windows:[{id:0,show:!0,isActive:!0,isFinished:!1},{id:1,show:!1,isActive:!1,isFinished:!1},{id:2,show:!1,isActive:!1,isFinished:!1}]}},methods:{nextPrev:function(t){this.windows[this.currentWindow].show=!1,this.windows[this.currentWindow].isFinished=!0,this.windows[this.currentWindow].isActive=!1,this.currentWindow+=t,this.windows[this.currentWindow].show=!0,this.windows[this.currentWindow].isActive=!0,console.log(this.currentWindow),console.log(this.windows.length),this.currentWindow==this.windows.length-1?(this.buttonPrevious=!0,this.buttonNext=!1,this.buttonSubmit=!0):0==this.currentWindow?(this.buttonPrevious=!1,this.buttonNext=!0,this.buttonSubmit=!1):(this.buttonPrevious=!0,this.buttonNext=!0,this.buttonSubmit=!1)},formSubmit:function(t){t.preventDefault(),r.a.post("http://localhost:5000/submit/report",{productName:this.formData.productName,companyName:this.formData.companyName,data:this.formData.data})}}},w={render:function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("form",{staticClass:"sectionContainer",attrs:{autocomplete:"off",method:"POST"},on:{submit:t.formSubmit}},[e("div",{staticClass:"colContainer"},[e("div",{staticClass:"subtitle"},[t._v("\n            Project Information\n        ")]),t._v(" "),e("hr"),t._v(" "),e("div",{staticClass:"formContainer"},[t.windows[0].show?e("div",{staticClass:"formContentContainer"},[e("p",[e("label",{staticClass:"formLabel",attrs:{for:"productName"}},[t._v("Product Name")]),t._v(" "),e("input",{directives:[{name:"model",rawName:"v-model",value:t.formData.productName,expression:"formData.productName"}],staticClass:"formField",attrs:{type:"text",name:"productName"},domProps:{value:t.formData.productName},on:{input:function(a){a.target.composing||t.$set(t.formData,"productName",a.target.value)}}})]),t._v(" "),e("p",[e("label",{staticClass:"formLabel",attrs:{for:"companyName"}},[t._v("Company Name")]),t._v(" "),e("input",{directives:[{name:"model",rawName:"v-model",value:t.formData.companyName,expression:"formData.companyName"}],staticClass:"formField",attrs:{type:"text",name:"companyName"},domProps:{value:t.formData.companyName},on:{input:function(a){a.target.composing||t.$set(t.formData,"companyName",a.target.value)}}})]),t._v(" "),e("p",[e("label",{staticClass:"formLabel",attrs:{for:"data"}},[t._v("Data Location")]),t._v(" "),e("input",{directives:[{name:"model",rawName:"v-model",value:t.formData.data,expression:"formData.data"}],staticClass:"formField",attrs:{type:"text",name:"dataLocation"},domProps:{value:t.formData.data},on:{input:function(a){a.target.composing||t.$set(t.formData,"data",a.target.value)}}})])]):t._e(),t._v(" "),t.windows[1].show?e("div",{staticClass:"formContentContainer"},[e("p",[e("label",{staticClass:"formLabel",attrs:{for:"standard"}},[t._v("Product Standard")]),t._v(" "),e("select",{directives:[{name:"model",rawName:"v-model",value:t.standard,expression:"standard"}],on:{change:function(a){var e=Array.prototype.filter.call(a.target.options,function(t){return t.selected}).map(function(t){return"_value"in t?t._value:t.value});t.standard=a.target.multiple?e:e[0]}}},[e("option",{attrs:{value:"",selected:"",disabled:""}},[t._v(" Select... ")]),t._v(" "),e("option",{attrs:{value:"CISPR 11"}},[t._v("CISPR 11")]),t._v(" "),e("option",{attrs:{value:"CISPR 32"}},[t._v("CISPR 32")]),t._v(" "),e("option",{attrs:{value:"FCC"}},[t._v("FCC")])])]),e("p",[e("label",{staticClass:"formLabel",attrs:{for:"companyName"}},[t._v("Company Name")]),t._v(" "),e("input",{directives:[{name:"model",rawName:"v-model",value:t.formData.companyName,expression:"formData.companyName"}],staticClass:"formField",attrs:{type:"text",name:"companyName"},domProps:{value:t.formData.companyName},on:{input:function(a){a.target.composing||t.$set(t.formData,"companyName",a.target.value)}}})]),t._v(" "),e("p",[e("label",{staticClass:"formLabel",attrs:{for:"data"}},[t._v("Data Location")]),t._v(" "),e("input",{directives:[{name:"model",rawName:"v-model",value:t.formData.data,expression:"formData.data"}],staticClass:"formField",attrs:{type:"text",name:"dataLocation"},domProps:{value:t.formData.data},on:{input:function(a){a.target.composing||t.$set(t.formData,"data",a.target.value)}}})])]):t._e(),t._v(" "),t.windows[2].show?e("div",{staticClass:"formContentContainer"},[e("p",[e("label",{staticClass:"formLabel",attrs:{for:"productName"}},[t._v("Page3")]),t._v(" "),e("input",{directives:[{name:"model",rawName:"v-model",value:t.formData.productName,expression:"formData.productName"}],staticClass:"formField",attrs:{type:"text",name:"productName"},domProps:{value:t.formData.productName},on:{input:function(a){a.target.composing||t.$set(t.formData,"productName",a.target.value)}}})]),t._v(" "),e("p",[e("label",{staticClass:"formLabel",attrs:{for:"companyName"}},[t._v("Company Name")]),t._v(" "),e("input",{directives:[{name:"model",rawName:"v-model",value:t.formData.companyName,expression:"formData.companyName"}],staticClass:"formField",attrs:{type:"text",name:"companyName"},domProps:{value:t.formData.companyName},on:{input:function(a){a.target.composing||t.$set(t.formData,"companyName",a.target.value)}}})]),t._v(" "),e("p",[e("label",{staticClass:"formLabel",attrs:{for:"data"}},[t._v("Data Location")]),t._v(" "),e("input",{directives:[{name:"model",rawName:"v-model",value:t.formData.data,expression:"formData.data"}],staticClass:"formField",attrs:{type:"text",name:"dataLocation"},domProps:{value:t.formData.data},on:{input:function(a){a.target.composing||t.$set(t.formData,"data",a.target.value)}}})])]):t._e(),t._v(" "),e("div",{staticClass:"navButtonContainer"},[t.buttonPrevious?e("button",{attrs:{type:"button"},on:{click:function(a){return t.nextPrev(-1)}}},[t._v("Previous")]):t._e(),t._v(" "),t.buttonNext?e("button",{attrs:{type:"button"},on:{click:function(a){return t.nextPrev(1)}}},[t._v("Next")]):t._e(),t._v(" "),e("router-link",{attrs:{to:"/reports/success"}},[t.buttonSubmit?e("button",[t._v("Submit")]):t._e()])],1),t._v(" "),e("div",{staticClass:"stepContainer"},[e("span",{staticClass:"step",class:{active:t.windows[0].isActive,finish:t.windows[0].isFinished}}),t._v(" "),e("span",{staticClass:"step",class:{active:t.windows[1].isActive,finish:t.windows[1].isFinished}}),t._v(" "),e("span",{staticClass:"step",class:{active:t.windows[2].isActive,finish:t.windows[2].isFinished}})])]),t._v(" "),t._m(0)])])},staticRenderFns:[function(){var t=this.$createElement,a=this._self._c||t;return a("div",{staticClass:"formContainer",attrs:{id:"loadingScreen"}},[a("span",{staticClass:"loading",attrs:{id:"loadingOne"}}),this._v(" "),a("span",{staticClass:"loading",attrs:{id:"loadingTwo"}}),this._v(" "),a("span",{staticClass:"loading",attrs:{id:"loadingThree"}})])}]};var N=e("VU/8")(g,w,!1,function(t){e("dYau")},"data-v-00d8b1b9",null).exports,D={name:"ReportSuccess",methods:{fileOpen:function(t){t.preventDefault(),r.a.post("http://localhost:5000/submit/fileopen")}}},y={render:function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"sectionContainer"},[s("div",{staticClass:"colContainer"},[t._m(0),t._v(" "),s("hr"),t._v(" "),s("div",{staticClass:"successButtonContainer"},[s("form",{staticClass:"homeButton",attrs:{method:"POST"},on:{submit:t.fileOpen}},[s("button",[s("font-awesome-icon",{staticClass:"bigIcon",attrs:{icon:"folder-open"}}),t._v(" "),t._m(1)],1)]),t._v(" "),s("router-link",{staticClass:"homeButton",attrs:{to:"/reports"}},[s("font-awesome-icon",{staticClass:"bigIcon",attrs:{icon:"file-alt"}}),t._v(" "),s("div",{staticClass:"startContainer"},[s("h3",{staticClass:"startSubtitle"},[s("strong",[t._v("Create Another Report")])])])],1),t._v(" "),s("router-link",{staticClass:"homeButton",attrs:{to:"/"}},[s("img",{staticClass:"bigLogo",attrs:{src:e("U4IG"),alt:"TUV Logo"}}),t._v(" "),s("div",{staticClass:"startContainer"},[s("h3",{staticClass:"startSubtitle"},[s("strong",[t._v("Return to Home")])])])])],1)])])},staticRenderFns:[function(){var t=this.$createElement,a=this._self._c||t;return a("div",{staticClass:"title"},[a("h1",[this._v("Report Created")])])},function(){var t=this.$createElement,a=this._self._c||t;return a("div",{staticClass:"startContainer"},[a("h3",{staticClass:"startSubtitle"},[a("strong",[this._v("Open Output Directory")])])])}]};var x=e("VU/8")(D,y,!1,function(t){e("oOHa")},"data-v-6b306485",null).exports;s.a.use(d.a);var R=new d.a({mode:"history",routes:[{path:"/",name:"Home",component:f},{path:"/reports",name:"ReportLanding",component:C},{path:"/reports/create",name:"ReportCreation",component:b},{path:"/reports/create/report",name:"ReportForm",component:N},{path:"/reports/success",name:"ReportSuccess",component:x}]}),F=e("C/JF"),P=e("fhbW"),S=e("1e6/");s.a.config.productionTip=!1,F.c.add(P.d,P.c,P.b,P.f,P.a,P.e),s.a.component("font-awesome-icon",S.a),new s.a({el:"#app",router:R,components:{App:u},template:"<App/>"})},QDHz:function(t,a){},U4IG:function(t,a,e){t.exports=e.p+"static/img/successlogo.310365b.svg"},dYau:function(t,a){},j7bV:function(t,a){},oBrg:function(t,a,e){t.exports=e.p+"static/img/biglogo.8e96b18.svg"},oOHa:function(t,a){}},["NHnr"]);
//# sourceMappingURL=app.19c5fbaa8e1760aee3c8.js.map
(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-55d4e541"],{"728d":function(t,e,s){"use strict";s.r(e);var a=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"panel"},[s("panel-title",{attrs:{title:t.$lang.objects.tasks}},[s("router-link",{attrs:{to:{name:"taskCreate"},tag:"span"}},[s("el-button",{attrs:{type:"success",size:"mini"}},[s("i",{staticClass:"fa fa-plus"}),t._v("\n        "+t._s(t.$lang.buttons.create)+"\n      ")])],1)],1),s("div",{staticClass:"panel-body"},[s("el-table",{directives:[{name:"loading",rawName:"v-loading",value:t.loading,expression:"loading"}],attrs:{"empty-text":t.$lang.messages.noData,data:t.tasks,"element-loading-text":t.$lang.messages.loading}},[s("el-table-column",{attrs:{align:"center",prop:"id",label:t.$lang.columns.id,width:"60"}}),s("el-table-column",{attrs:{align:"center",prop:"name",label:t.$lang.columns.name,width:"200"}}),s("el-table-column",{attrs:{align:"center",prop:"project",label:t.$lang.columns.project,width:"200"}}),s("el-table-column",{attrs:{align:"center",prop:"spider",width:"200",label:t.$lang.columns.spider}}),s("el-table-column",{attrs:{align:"center",label:t.$lang.columns.operations},scopedSlots:t._u([{key:"default",fn:function(e){return[s("router-link",{attrs:{to:{name:"taskStatus",params:{id:e.row.id}},tag:"span"}},[s("el-button",{attrs:{type:"success",size:"mini"}},[s("i",{staticClass:"fa fa-sitemap"}),t._v("\n              "+t._s(t.$lang.buttons.status)+"\n            ")])],1),s("router-link",{attrs:{to:{name:"taskEdit",params:{id:e.row.id}},tag:"span"}},[s("el-button",{attrs:{type:"info",size:"mini"}},[s("i",{staticClass:"fa fa-edit"}),t._v("\n              "+t._s(t.$lang.buttons.edit)+"\n            ")])],1),s("el-button",{attrs:{type:"danger",size:"mini"},on:{click:function(s){return t.onSingleDelete(e.row.id)}}},[s("i",{staticClass:"fa fa-remove"}),t._v("\n            "+t._s(t.$lang.buttons.delete)+"\n          ")])]}}])})],1)],1)],1)},n=[],l=s("eee4"),i={data:function(){return{tasks:null,loading:!0,statusText:{1:this.$store.getters.$lang.buttons.normal,0:this.$store.getters.$lang.buttons.connecting,"-1":this.$store.getters.$lang.buttons.error}}},components:{PanelTitle:l["a"]},created:function(){this.getTaskData()},methods:{onRefresh:function(){this.getTaskData()},changeFilter:function(){this.lastIds={},this.getTaskData()},getTaskData:function(){var t=this;this.loading=!0,this.$http.get(this.$store.state.url.task.index).then((function(e){var s=e.data.data;t.tasks=s,t.loading=!1})).catch((function(){t.loading=!1}))},deleteTask:function(t){var e=this;this.$http.post(this.formatString(this.$store.state.url.task.remove,{id:t})).then((function(){e.$message.success(e.$store.getters.$lang.messages.successDelete),e.loading=!1,e.getTaskData()})).catch((function(){e.$message.error(e.$store.getters.$lang.messages.errorDelete),e.loading=!1}))},onSingleDelete:function(t){var e=this;this.$confirm(this.$store.getters.$lang.messages.confirm,this.$store.getters.$lang.buttons.confirm,{confirmButtonText:this.$store.getters.$lang.buttons.yes,cancelButtonText:this.$store.getters.$lang.buttons.no,type:"warning"}).then((function(){e.deleteTask(t)}))}}},o=i,r=s("2877"),c=Object(r["a"])(o,a,n,!1,null,null,null);e["default"]=c.exports},eee4:function(t,e,s){"use strict";var a=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"panel-title"},[t.title?s("span",{domProps:{textContent:t._s(t.title)}}):t._e(),s("div",{staticClass:"fr"},[t._t("default")],2)])},n=[],l={name:"PanelTitle",props:{title:{type:String}}},i=l,o=s("2877"),r=Object(o["a"])(i,a,n,!1,null,null,null);e["a"]=r.exports}}]);
//# sourceMappingURL=chunk-55d4e541.dfd42f49.js.map
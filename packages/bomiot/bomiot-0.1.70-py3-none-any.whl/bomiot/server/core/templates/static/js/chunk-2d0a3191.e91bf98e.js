(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0a3191"],{"0171":function(t,a,e){"use strict";e.r(a);var s=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("div",{staticClass:"panel"},[e("panel-title",{attrs:{title:t.$lang.titles.createTask}}),e("div",{directives:[{name:"loading",rawName:"v-loading",value:t.loadData,expression:"loadData"}],staticClass:"panel-body",attrs:{"element-loading-text":t.$lang.messages.loading}},[e("el-row",[e("el-col",{attrs:{span:10}},[e("substance",{ref:"substance"},[e("template",{slot:"submit"},[e("el-button",{attrs:{type:"primary",size:"small",loading:t.onSubmitLoading},on:{click:t.onSubmitForm}},[e("i",{staticClass:"fa fa-check"}),t._v("\n              "+t._s(t.$lang.buttons.create)+"\n            ")])],1)],2)],1)],1)],1)],1)},n=[],o=e("eee4"),i=e("80bd"),l={data:function(){return{onSubmitLoading:!1,loadData:!1,routeId:this.$route.params.id}},methods:{onSubmitForm:function(){var t=this;this.$refs.substance.$refs.form.validate((function(a){if(!a)return!1;var e=t.$refs.substance.formData;t.onSubmitLoading=!0,t.$http.post(t.$store.state.url.task.create,e).then((function(){t.$message.success(t.$store.getters.$lang.messages.successSave),t.onSubmitLoading=!1,t.$router.push({name:"taskIndex"})})).catch((function(){t.onSubmitLoading=!1}))}))}},components:{PanelTitle:o["a"],Substance:i["a"]}},r=l,u=e("2877"),c=Object(u["a"])(r,s,n,!1,null,null,null);a["default"]=c.exports}}]);
//# sourceMappingURL=chunk-2d0a3191.e91bf98e.js.map
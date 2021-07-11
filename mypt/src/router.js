import Vue from "vue";
import VueRouter from "vue-router";
import Home from "./views/Home";
import About from "./views/About";


// Vuerouter 사용하기
Vue.use(VueRouter);

const router = new VueRouter({
    mode: "history",
    routes: [
        {path:"/", component: Home, name:"Home"}, 
        {path:"/about", component: About, name:"About"}
    ]
});

export default router;
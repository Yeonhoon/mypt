import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
// import Main from './components/main'
// import HelloWorld from './components/HelloWorld'
import Todo from './components/Todo'
import TodoList from './components/TodoList'
import router from './router'
import Home from './views/Home'
import 'material-design-icons-iconfont/dist/material-design-icons.css'

// 연습
import Todo2 from './components/Todo2'



Vue.config.productionTip = false
// Vue.component('HelloWorld',HelloWorld)
Vue.component('Todo', Todo)
Vue.component("Home",Home)
Vue.component('TodoList', TodoList)

// 연습
Vue.component('Todo2',Todo2)

export const eventBus = new Vue({
  methods:{
    listEdit(memo, index){
      this.$emit('listEdit',memo, index)
    }
  }
})


new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')

<template>
  <Todo2
    @addTodo = "addTodo"
  ></Todo2>
</template>
<script>
export default {
  name:'Home2',
  components:{},
  data() {
    return {
      todoList=[]
    };
  }, 
  beforeCreate() {},
  created() {}, 
  beforeMount() {},
  mounted() {}, 
  beforeUpdate() {}, 
  updated() {}, 
  beforeUnmount(){}, 
  unmounted(){},
  methods:{
    addTodo(Todo){
      this.todoList.push(Todo)
      console.log(todoList)
    }


  }
}
</script>
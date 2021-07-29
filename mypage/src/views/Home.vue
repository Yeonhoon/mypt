<template>
  <v-container>
    <v-layout row wrap>
      <v-row xs-8 align-center>
        <Todo
        @addTodo="addTodo"
        @editTodo="editTodo"
        ></Todo>
      </v-row>
    </v-layout>
    <v-layout>
      <v-flex xs6>
        <TodoList
          :todoList = "todoList"
          @statusControl="statusControl"
          @listDelete="listDelete"
        ></TodoList>
      </v-flex>
    </v-layout>
  </v-container>
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  data(){
    return {
      todoList: []
    }
  },
  methods:{
    addTodo(memo){
      console.log('Todo를 받음')
      this.todoList.push({memo:memo, status: "created"})
      // console.log(todoList)
    },
    editTodo(memo, index){
      console.log('수정된 Todo를 받음')
      this.todoList[index].memo = memo
    },
    statusControl(index, status){
      this.todoList[index].status = status
    },
    listDelete(index){
      // todolist에서 index를 찾은 뒤, 1개를 지워줘
      this.todoList.splice(index, 1)
    }
  }

}
</script>

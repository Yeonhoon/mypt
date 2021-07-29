<template>
<v-app>
  <v-form>
    <v-container>
      <v-row>
        <h2>{{temp}}</h2>
        <v-col cols="12">

          <!-- v-model: vue 인스턴스와 연결s -->
          <v-text-field
              label="TODO"
              outlined
              v-model = "memo" 
          ></v-text-field>
          <v-btn x-large elevation="5"
              @click="toList()"
          >할일 추가</v-btn>
          <v-btn x-large elevation="5"
            v-if ="index !== null"
              @click="editList()"
          >할일 수정</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</v-app>
</template>

<script>
import {eventBus} from '../main'
export default {
    data(){
        return{
            temp: "TODO List",
            memo: null,
            index: null
        }
    },
    created(){
      // eventbus가 생성될 때 듣고 있어야함.
      eventBus.$on('listEdit', (memo, index) => {
        this.memo = memo
        this.index = index
        // console.log(memo, index)
      })
    },
    methods:{
        toList(){
          if(this.memo === null){
            alert('오늘의 할일을 입력하세요!')
          }
          else{
            console.log('할일 추가')
            this.$emit("addTodo",this.memo)
            this.memo = null //메모 추가하고 기록 지워주기
          }
        },
        editList(){
          if(this.memo === null){
            alert('오늘의 할일을 입력하세요!')
          }
          else{
            console.log('할일 수정')
            this.$emit('editTodo',this.memo, this.index)
            this.memo = null
          }
        }
    }
}
</script>
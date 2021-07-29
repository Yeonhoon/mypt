<template>
  <v-app>
    <v-form>
      <v-card
        class="pa-3 mb-3"
        :class="{'done': list.status==='done'}"
        v-for="(list, index) in todoList"
        :key="index"
      >
      <p>오늘의 할일 #{{index+1}}</p>
      <p>{{list.memo}}</p>
      <v-btn fab text small color="green"
        v-if="list.status === 'created'" 
        @click="$emit('statusControl',index, 'done')"><v-icon color="green">mdi-check</v-icon></v-btn>
      <v-btn fab text small color="blue"
        v-else 
         @click="$emit('statusControl',index, 'created')"><v-icon color="blue">mdi-refresh</v-icon></v-btn>
      <v-btn fab text small color="yellow"
        v-if ="list.status === 'created'"
        @click="listEdit(list.memo, index)"
      ><v-icon color="yellow">mdi-clipboard-edit</v-icon>
      </v-btn>
      <v-btn fab text small color="red"
        @click="$emit('listDelete', index)"><v-icon color="red">mdi-delete</v-icon></v-btn>
    
    </v-card >
      
    </v-form>
  </v-app>
</template>
<script>
import {eventBus} from '../main'
export default {
  props: ['todoList'],
  data(){
    return{
      lists:{},
    }
  },
  created(){
    this.lists.memo = this.memo
    this.lists.status = this.status

  },
  methods:{
    listEdit(memo, index){
      eventBus.listEdit(memo, index)
    }
  }
  
}
</script>
<style scoped>
  /* scoped: 해당 .vue 파일에서만 작동하게 함 */
  .done {
    background-color: rgb(0,0,0);
  }
  .done p {
    text-decoration:  line-through;
    color: rgba(0,0,0,0.5);
  }
</style>
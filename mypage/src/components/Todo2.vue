<template>
    <v-app>
        <v-form>
            <v-container color="black">
                <v-col
                    >
                    <v-row 
                        class="d-flex justify-center ml-15 mr-15 mt-5">

                        <v-text-field
                            label="Todo"
                            outlined
                            v-model="Todo">
                            
                        </v-text-field> 
                    </v-row>
                    <v-btn @click="addTodo()">오늘의 할일 추가</v-btn>                       
                </v-col>
            </v-container>
        </v-form>

    </v-app>
</template>
<script>
export default {
    name:'',
    components:{},
    data() {
        return {
            sampleData: '',
            Todo: null
        };
    }, 
    beforeCreate() {},
    created() {}, 
    beforeMount() {},
    mounted() {
        
    }, 
    beforeUpdate() {}, 
    updated() {}, 
    beforeUnmount(){}, 
    unmounted(){},
    methods:{
        addTodo(){
            if(this.Todo === null){
                alert('할일을 입력해라!')
            }
            else{
                this.$emit('addTodo',this.Todo)  
                console.log('Todo를 내보냄')

            }
        }
    }
}
</script>
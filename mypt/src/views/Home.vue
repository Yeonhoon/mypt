<template>
    <div>
        <h1>Welcome to {{title2}}!</h1>
        <!-- data binding -->
        <input type='text' v-model="input1"/>
        <button type="button" @click="getData">Get</button> <!-- click: onclick -->
        <button type="button" @click="setData">Set</button>

        <select class='form-control' v-model="regions"> <!--  @change="changeRegion" 이벤트 관리-->
            <option :key="index" :value="data.v" v-for="(data, index) in options">{{data.t}}</option>
        </select>

        <table class="table table-bordered" v-if="tableShow"> 
            <!-- v-show:조건을 만족하지 않아도 렌더링은 함, 자원관리 유용 -->
            <tr :key="i" :value="data.v" v-for="(data,i) in options">
                <td>{{data.v}}</td>
                <td>{{data.t}}</td>
            </tr>
        </table>

    </div>
</template>
<script>
export default {
    // 데이터 내보내기
    data(){
        return{
            title:"개발자의 품격",
            title2: "Seoul",
            input1: "abc",
            options: [
                {v:"S", t:"Seoul"},
                {v:"J", t:"Jeju"},
                {v:"B", t:"Busan"},
            ],
            regions: "S",
            tableShow: true
        };
    },
    watch:{
        // 데이터를 관찰하고 있음. 데이터가 변경되면 알려줌.
        input1(){
            console.log(this.input1);
        },
        title1(){
            console.log(this.title);
        }
    },
    // 데이터 받아오기
    methods: {
        getData(){
            alert(this.input1);
        },
        setData(){
            this.input1 = "sdfgsdgwetw";
        },
        changeRegion(){
            alert(this.regions);
        }
    },
    beforeCreate(){
        console.log("befreCreate")
    },
    created(){
        console.log("created")
    },
    beforeMount(){
        console.log("beforeMount")
    },
    mounted(){
        console.log("mounted")
    },
    beforeUpdate(){
        // console.log("befreUpdated")
    },
    updated(){
        // console.log("updated")
    },
    beforeDestroy(){
        console.log("befreDestroy")
    },
    destroyed(){
        console.log("destroyed")
    }
};
</script>
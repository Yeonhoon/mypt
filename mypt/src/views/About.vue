<template>
    <div>
        <h1>About {{b}}</h1>
        <input v-model="input1"/>
        <button @click="getData">GET</button>
        <button @click="setData">SET</button>
        <select name="" id="" class="form-control">
            <option :key="index" :value="data.k" v-for="(data,index) in arr">{{data.v}}</option>
        </select>
        <table class="table table-bordered">
            <tr :key="index" :value="data.k" v-for="(data, index) in arr">
                <td>{{data.v}}</td>
            </tr>
        </table>
    </div>

</template>
<script>
    export default {
        data(){
            return{
                input1: "input1",
                a:"aa",
                b:"bb",
                c:"cc",
                arr: [
                    {k:"x1", v:"value-1"},
                    {k:"x2", v:"value-2"},
                    {k:"x3", v:"value-3"},
                    {k:"x4", v:"value-4"}
                ]
            }
        },
        watch(){

        },
        methods:{
            getData(){
                alert(this.input1);
            },
            setData(){
                this.input1 = "change124124";
            }
        }
    };
</script>
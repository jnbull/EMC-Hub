<template>
    <div class = 'sectionContainer'>
        <div class = 'colContainer'>
            <div class = 'subtitle'>
                Loading...
            </div>
            <hr>
            <div class = 'formContainer'>
                <span id = 'loadingOne' class="loading"></span>
                <span id = 'loadingTwo' class="loading"></span>
                <span id = 'loadingThree' class="loading"></span>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return{
            loading: null
        }
    },

    created(){
        this.formSuccess()
        // this.$router.push({ path: 'ReportSuccess' })
    },

    methods: {
        formSuccess(){
            this.loading = true;
            return axios({
                method: 'get',
                url: 'http://localhost:5000/submit/report',
                timeout: 10000,
            })
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error){
                console.log(error);
            })
        }
    },
}
</script>

<style scoped>

.subtitle{
    color: black;
    margin-left: 10px;
    padding: 15px;
    font-size: 1.17em;
    font-weight: normal;
    font-stretch: normal;
}

.sectionContainer{
    display: grid;
    grid-template-rows: repeat(3, 1fr);
    grid-template-columns: repeat(3, 1fr);
    grid-column-gap: 20px;
    grid-row-gap: 20px;
    padding: 40px;
    position: fixed;
    top: 65px;
    left: 65px;
    right: 0;
    bottom: 0;
}

.colContainer{
    display: flex;
    flex-direction: column;
    background-color: white;
    border-radius: 5px;
    box-shadow: 0px 5px 2px -2px rgba(0,0,0,.2);
    grid-column-start: 1;
    grid-column-end: 9;
    grid-row-start: 1;
    grid-row-end: 5;
}

.formContainer{
    margin: auto;
    width: 90%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.loading{
    animation-duration: 3s;
    animation-name: loading;
    animation-iteration-count: infinite;
    height:50px;
    width: 50px;
    margin: 0 5px;
    background-color: #34495e;
    border: none;
    border-radius: 50%;
    display: inline-block;
    opacity: 0.5;
}

#loadingTwo{
    animation-delay: 1s;
}

#loadingThree{
    animation-delay: 2s;
}

@keyframes loading{
    0%{
        opacity: 0.5;
    }
    16%{
        opacity: 1;
    }
    33%{
        opacity: 0.5;
    }
    100%{
        opacity: 0.5;
    }
}

</style>



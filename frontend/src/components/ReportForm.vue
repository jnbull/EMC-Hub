<template>
        <!-- EMC Report Creation Form -->
        <form @submit = 'formSubmit' autocomplete = 'off' class = 'sectionContainer' method = 'POST'>
        <!-- {{ reportForm.hidden_tag() }} -->

            <!-- Step 1 - Project Information -->
            <div class = 'colContainer'>

                <!-- Subtitle -->
                <div class = 'subtitle'>
                    Project Information
                </div>
                <hr>

                <!-- Form Layout Tab -->
                <div class = 'formContainer'>

                    <!-- Form Content -->
                    <div class = 'formContentContainer'>
                        <label for="productName">Product Name</label>
                        <input v-model = 'formData.productName' class = 'formField' type="text" name = 'productName'>

                        <label for="companyName">Company Name</label>
                        <input v-model = 'formData.companyName' class = 'formField' type="text" name = 'companyName'>

                        <label for="data">Data Location</label>
                        <input v-model = 'formData.data' class = 'formField' type="text" name = 'dataLocation'>


                        <button>Submit</button>

                    </div>
                </div>
            </div>
        </form>
</template>

<script>
import axios from 'axios'

export default {
    name: 'ReportForm',
    data() {
        return{
            formData: {
                productName: "",
                companyName: "",
                data: "",
                // equipment: {
                //     SpecA: '',
                //     LISN: ''
                // },
                // standard: '',
                // class_:'',
                // setup: ;
            }
            
        }
    },
    methods: {
        formSubmit(e){
            e.preventDefault();
            axios.post('http://localhost:5000/submit/report', {productName: this.formData.productName, companyName: this.formData.companyName, data: this.formData.data})
            // .then(res => {
            //     this.productName = ''
            // })
            // .catch(err => {
            //     console.log(err)
            // })
        }
    }
}
</script>

<style scoped>
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

 .subtitle{
    color: black;
    margin-left: 10px;
    padding: 15px;
    font-size: 1.17em;
    font-weight: normal;
    font-stretch: normal;
}

.formContainer{
    position: relative;
    margin: 0px auto;
    width: 70%;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}

.formContentContainer{
    display: flex;
    padding: 20px 0px;
    width: 100%;
    align-self: flex-start;
}

 .formLabel{
    display: block;
    margin: 10px 0px;
}

.formField{
    font-size: 14px;
    display: block;
    margin-right: auto;
    width: 100%;
    padding:10px;
}

.navButtonContainer{
    align-self: flex-end;
}

button{
    background-color: #34495e;
    padding: 10px;
    color: whitesmoke;
    border-radius: 5px; 
    width: 100px;
    height: 100%;
    font-size: 12pt;
    text-align: center;
    cursor: pointer;
}


.stepContainer{
    text-align: center;
    margin: auto 0px 40px 0px;
}

.step{
    height: 15px;
    width: 15px;
    margin: 0 2px;
    background-color: #34495e;
    border: none; 
    border-radius: 50%;
    display: inline-block;
    opacity: 0.5;
}

.step.active {
    opacity: 1;
}

.step.finish {
    background-color: #0bab64;
}

#loadingScreen{
    display: none;
    flex-direction: row;
    justify-content: center;
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

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
                <div v-if = 'windows[0].show' class = 'formContentContainer'>
                    <div>
                        <label v-bind:class = '{invalid: windows[0].formData[0].validated == false}' class = 'formLabel' for="productName">Product Name</label>
                        <input v-model = 'windows[0].formData[0].content' class = 'formField' type="text" name = 'productName'>
                        <p class = 'errorText' v-if = 'windows[0].formData[0].validated == false'>{{windows[0].formData[0].error}}</p>
                    </div>
                    
                    <div>
                        <label v-bind:class = '{invalid: windows[0].formData[1].validated == false}' class = 'formLabel' for="companyName">Company Name</label>
                        <input v-model = 'windows[0].formData[1].content' class = 'formField' type="text" name = 'companyName'>
                        <p class = 'errorText' v-if = 'windows[0].formData[1].validated == false'>{{windows[0].formData[1].error}}</p>
                    </div>
                    
                    <div>
                        <label v-bind:class = '{invalid: windows[0].formData[2].validated == false}' class = 'formLabel' for="data">Data Location</label>
                        <input v-model = 'windows[0].formData[2].content' class = 'formField' type="text" name = 'dataLocation'>
                        <p class = 'errorText' v-if = 'windows[0].formData[2].validated == false'>{{windows[0].formData[2].error}}</p>
                    </div>

                </div>

                 <div v-if = 'windows[1].show' class = 'formContentContainer'>
                    <p>
                        <label class = 'formLabel' for="standard">Product Standard</label>
            
                        <select name = 'standard' class = 'customSelect' v-model= "formData.standard">
                            <option disabled value="">Select: </option>
                            <option>CISPR 11</option>
                            <option>CISPR 32</option>
                            <option>FCC</option>
                        </select>
                        
                    <p>
                        <label class = 'formLabel' for="class_">Product Class</label>

                        <select name = 'class_' class = 'customSelect' v-model= "formData.class_">
                            <option disabled value="">Select: </option>
                            <option>Class A</option>
                            <option>Class B</option>
                        </select>
                    </p>
                    
                    <p>
                        <label class = 'formLabel' for="power">Input Power</label>
                        
                        <select name = 'power' class = 'customSelect' v-model= "formData.power">
                            <option disabled value="">Select: </option>
                            <option>Single-Phase</option>
                            <option>Three-Phase</option>
                        </select>
                    </p>
                </div>

                 <div v-if = 'windows[2].show' class = 'formContentContainer'>
                    <p>
                        <label class = 'formLabel' for="productName">Page3</label>
                        <input v-model = 'formData.productName' class = 'formField' type="text" name = 'productName'>
                    </p>
                    
                    <p>
                        <label class = 'formLabel' for="companyName">Company Name</label>
                        <input v-model = 'formData.companyName' class = 'formField' type="text" name = 'companyName'>
                    </p>
                    
                    <p>
                        <label class = 'formLabel' for="data">Data Location</label>
                        <input v-model = 'formData.data' class = 'formField' type="text" name = 'dataLocation'>
                    </p>
                </div>

                <!-- Form Navigation -->
                <div class = 'navButtonContainer'>
                    <button type = 'button' v-on:click = "nextPrev(-1)" v-if = 'buttonPrevious'>Previous</button>
                    <button type = 'button' v-on:click = "nextPrev(1)" v-if = 'buttonNext'>Next</button>
                    <router-link to = '/reports/success'><button v-if = 'buttonSubmit'>Submit</button></router-link>
                </div>

                <!-- Form Step Bubbles -->
                <div class = 'stepContainer'>
                    <span v-bind:class = "{active: windows[0].isActive, finish: windows[0].isFinished}" class="step"></span>
                    <span v-bind:class = "{active: windows[1].isActive, finish: windows[1].isFinished}" class="step"></span>
                    <span v-bind:class = "{active: windows[2].isActive, finish: windows[2].isFinished}" class="step"></span>
                </div>

            </div>

            <div id = 'loadingScreen' class = 'formContainer'>
                <span id = 'loadingOne' class="loading"></span>
                <span id = 'loadingTwo' class="loading"></span>
                <span id = 'loadingThree' class="loading"></span>
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
                
                standard: "",
                class_: "",
                power: "",
                // equipment: {
                //     SpecA: '',
                //     LISN: ''
                // },
                // standard: '',
                // class_:'',
                // setup: ;
            },
            currentWindow: 0,
            counter: 0,
            buttonPrevious: false,
            buttonSubmit: false,
            buttonNext: true,
            windows: [
                {
                    id: 0,
                    show: true,
                    isActive: true,
                    isFinished: false,
                    formData: [
                        {
                            type: 'dataRequired',
                            validated: null,
                            content: '',
                            error: 'Please enter a Product Name'
                        },
                        {
                            type: 'dataRequired',
                            validated: null,
                            content: '',
                            error: 'Please enter a Company Name'
                        },
                        {
                            type: 'dataRequired',
                            validated: null,
                            content: '',
                            error: 'Please enter a Data Location'
                        }
                    ],
                    validated: false,
                },
                {
                    id: 1,
                    show: false,
                    isActive: false,
                    isFinished: false,
                    validated: false,
                },
                {
                    id: 2,
                    show:false,
                    isActive: false,
                    isFinished: false,
                    validated: false,
                },
            ]
            
        }
    },
    methods: {
        
        nextPrev(n){

            if (n == 1){
                this.validateWindow(this.windows[this.currentWindow]);
            }

            if (n == -1 || this.windows[this.currentWindow].validated == true){
                this.windows[this.currentWindow].show = false;
                if (n != -1){
                    this.windows[this.currentWindow].isFinished = true;
                }
                this.windows[this.currentWindow].isActive = false;
                this.currentWindow += n;
                this.windows[this.currentWindow].show = true;
                this.windows[this.currentWindow].isActive = true;

                if (this.currentWindow == this.windows.length - 1){
                    this.buttonPrevious = true;
                    this.buttonNext = false;
                    this.buttonSubmit = true;
                }
                else if(this.currentWindow == 0){
                    this.buttonPrevious = false;
                    this.buttonNext = true;
                    this.buttonSubmit = false;
                }
                else{
                    this.buttonPrevious = true;
                    this.buttonNext = true;
                    this.buttonSubmit = false;
                }
            }
            

        },

        validateWindow(window){
            window.validated = false;

            var counter = 0;
            for (const field of window.formData){
                if (field.type == 'dataRequired'){
                    if (field.content != ''){
                        field.validated = true;
                        counter += 1;
                    }
                    else{
                        field.validated = false;
                    }
                }
                // other types here
            }

            if (counter == window.formData.length){
                window.validated = true;
            }
        },

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

@import url('https://fonts.googleapis.com/css?family=Oswald|Roboto&display=swap');

.errorText{
    font-style: italic;
    color: grey;
    font-size: 10pt;
}
.customSelect{
    background-color:#34495e;
    font-family: 'Roboto';
    color: whitesmoke;
    width: 150px;
    height: 39px;
    font-size: 11pt;
    border-radius: 5px;
    box-shadow: 0px 5px 2px -2px rgba(0,0,0,.2);
    cursor: pointer;
    transition: transform .2s;
    text-align: center;
}

.customSelect:hover{
    transform: scale(1.05);
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
    flex-direction: column;
    padding: 20px 0px;
    width: 100%;
    align-self: flex-start;
}

 .formLabel{
    display: block;
    margin: 10px 0px 2px 0px;
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
    /* margin-top: auto; */
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
    transition: transform .2s;
}


.stepContainer{
    text-align: center;
    margin: auto 0px 40px 0px;
}

.formLabel.invalid{
    color: red;
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

<template>
    <!-- EMC Report Creation Form -->
    <form v-on:submit.prevent autocomplete = 'off' class = 'sectionContainer' method = 'POST'>
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
                    <div class = 'formFieldContainer'>
                        <label v-bind:class = '{invalid: windows[0].formData[0].validated == false}' class = 'formLabel' for="productName">Product Name</label>
                        <input v-model = 'windows[0].formData[0].content' class = 'formField' type="text" name = 'productName'>
                        <p class = 'errorText' v-if = 'windows[0].formData[0].validated == false'>{{windows[0].formData[0].error}}</p>
                    </div>
                    
                    <div class = 'formFieldContainer'>
                        <label v-bind:class = '{invalid: windows[0].formData[1].validated == false}' class = 'formLabel' for="companyName">Company Name</label>
                        <input v-model = 'windows[0].formData[1].content' class = 'formField' type="text" name = 'companyName'>
                        <p class = 'errorText' v-if = 'windows[0].formData[1].validated == false'>{{windows[0].formData[1].error}}</p>
                    </div>
                    
                    <div class = 'formFieldContainer'>
                        <label v-bind:class = '{invalid: windows[0].formData[2].validated == false}' class = 'formLabel' for="data">Data Location</label>
                        <input v-model = 'windows[0].formData[2].content' class = 'formField' type="text" name = 'dataLocation'>
                        <p class = 'errorText' v-if = 'windows[0].formData[2].validated == false'>{{windows[0].formData[2].error}}</p>
                    </div>

                </div>

                <div v-if = 'windows[1].show' class = 'formContentContainer'>
                    <div class = 'formFieldContainer'>
                        <label v-bind:class = '{invalid: windows[1].formData[0].validated == false}' class = 'formLabel' for="standard">Product Standard</label>
            
                        <select name = 'standard' class = 'customSelect' v-model= "windows[1].formData[0].content">
                            <option disabled value="">Select: </option>
                            <option value = './assets/reports/CISPR11.docx'>CISPR 11</option>
                            <option value = './assets/reports/CISPR11-FCC.docx'>CISPR 11 & FCC</option>
                            <option value = './assets/reports/CISPR32.docx'>CISPR 32</option>
                            <option value = './assets/reports/CISPR32-FCC.docx'>CISPR 32 & FCC</option>
                            <option value = './assets/reports/FCC.docx'>FCC</option>
                        </select>

                        <p class = 'errorText' v-if = 'windows[1].formData[0].validated == false'>{{windows[1].formData[0].error}}</p>
                    </div>

                    <div class = 'formFieldContainer'>
                        <label v-bind:class = '{invalid: windows[1].formData[1].validated == false}' class = 'formLabel' for="class_">Test Setup</label>

                        <select name = 'setup' class = 'customSelect' v-model= "windows[1].formData[1].content">
                            <option disabled value="">Select: </option>
                            <option value = 'Table-Top'>Table Top</option>
                            <option value = 'Floor Standing'>Floor Standing</option>
                        </select>

                        <p class = 'errorText' v-if = 'windows[1].formData[1].validated == false'>{{windows[1].formData[1].error}}</p>
                    </div>
                    
                    <div class = 'formFieldContainer'>
                        <label v-bind:class = '{invalid: windows[1].formData[2].validated == false}' class = 'formLabel' for="power">Input Power</label>
                        
                        <select name = 'power' class = 'customSelect' v-model= "windows[1].formData[2].content">
                            <option disabled value="">Select: </option>
                            <option value = 'Single Phase'>Single-Phase</option>
                            <option value = 'Three Phase'>Three-Phase</option>
                        </select>

                        <p class = 'errorText' v-if = 'windows[1].formData[2].validated == false'>{{windows[1].formData[2].error}}</p>
                    </div>

                </div>

                <div v-if = 'windows[2].show' class = 'formContentContainer'>
                    <div class = 'formFieldContainer'>
                        <label v-bind:class = '{invalid: windows[2].formData[0].validated == false}' class = 'formLabel' for="class_">Product Class</label>

                        <select name = 'class_' class = 'customSelect' v-model= "windows[2].formData[0].content">
                            <option disabled value="">Select: </option>
                            <option value = 'Class A'>Class A</option>
                            <option value = 'Class B'>Class B</option>
                        </select>

                        <p class = 'errorText' v-if = 'windows[2].formData[0].validated == false'>{{windows[2].formData[0].error}}</p>
                    </div>
                    
                    <div class = 'formFieldContainer'>
                        <label v-bind:class = '{invalid: windows[2].formData[1].validated == false}' class = 'formLabel'>LISN</label>

                        <select name = 'lisn' class = 'customSelect' v-model= "windows[2].formData[1].content">
                            <option disabled value="">Select: </option>
                            <option value = 'GEMC 302'>LISN 302</option>
                            <option value = 'GEMC 303'>LISN 303</option>
                        </select>

                        <p class = 'errorText' v-if = 'windows[2].formData[1].validated == false'>{{windows[2].formData[1].error}}</p>
                    </div>

                    <div class = 'formFieldContainer'>
                        <label v-bind:class = '{invalid: windows[2].formData[2].validated == false}' class = 'formLabel'>Spectrum Analyzer</label>

                        <select name = 'specA' class = 'customSelect' v-model= "windows[2].formData[2].content">
                            <option disabled value="">Select: </option>
                            <option value = 'GEMC 160'>ESL 6</option>
                            <option value = 'GEMC 198'>FSU 3</option>
                        </select>

                        <p class = 'errorText' v-if = 'windows[2].formData[2].validated == false'>{{windows[2].formData[2].error}}</p>
                    </div>
                    
    
                </div>

                <!-- <div v-if = 'windows[3].show' class = 'formContentContainer'>
                    <h2>Submitting this form will delete the session.</h2>
                    <h2>Continue with submission?</h2>
                </div> -->
            </div>

            <!-- Form Navigation -->
            <div class = 'navButtonContainer'>
                <button type = 'button' v-on:click = "nextPrev(-1)" v-if = 'buttonPrevious'>Previous</button>
                <button type = 'button' v-on:click = "nextPrev(1)" v-if = 'buttonNext'>Next</button>
                <button type = 'button' v-if = '!windows[2].validated && buttonSubmit' v-on:click = "validateWindow(windows[2])">Next</button>
                <button v-on:click = 'formSubmit' @click="$router.push({name: 'ReportSuccess'})" v-if = 'windows[2].validated && buttonSubmit'>Submit</button>
            </div>

            <!-- Form Step Bubbles -->
            <div class = 'stepContainer'>
                <span v-bind:class = "{active: windows[0].isActive, finish: windows[0].isFinished}" class="step"></span>
                <span v-bind:class = "{active: windows[1].isActive, finish: windows[1].isFinished}" class="step"></span>
                <span v-bind:class = "{active: windows[2].isActive, finish: windows[2].isFinished}" class="step"></span>
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
            currentWindow: 0,
            counter: 0,
            buttonPrevious: false,
            buttonSubmit: false,
            buttonNext: true,
            submitted: false,
            windows: [
                {
                    id: 0,
                    show: true,
                    isActive: true,
                    isFinished: false,
                    formData: [
                        {
                            name: 'productName',
                            type: 'dataRequired',
                            validated: null,
                            content: '',
                            error: ''
                        },
                        {
                            name: 'companyName',
                            type: 'dataRequired',
                            validated: null,
                            content: '',
                            error: ''
                        },
                        {
                            name: 'dataLocation',
                            type: 'dataRequired',
                            validated: null,
                            content: '',
                            error: ''
                        }
                    ],
                    validated: false,
                },
                {
                    id: 1,
                    show: false,
                    isActive: false,
                    isFinished: false,
                    formData: [
                        {
                            name: 'standard',
                            type: 'dataRequired',
                            validated: null,
                            content: '',
                            error: ''
                        },
                        {
                            name: 'setup',
                            type: 'dataRequired',
                            validated: null,
                            content: '',
                            error: ''
                        },
                        {
                            name: 'power',
                            type: 'dataRequired',
                            validated: null,
                            content: '',
                            error: ''
                        }
                    ],
                    validated: false,
                },
                {
                    id: 2,
                    show:false,
                    isActive: false,
                    isFinished: false,
                    formData: [
                        {
                            name: 'class_',
                            type: 'dataRequired',
                            validated: null,
                            content: '',
                            error: ''
                        },
                        {
                            name: 'lisn',
                            type: 'dataRequired',
                            validated: null,
                            content: '',
                            error: ''
                        },
                        {
                            name: 'specA',
                            type: 'dataRequired',
                            validated: null,
                            content: '',
                            error: ''
                        }
                    ],
                    validated: false,
                },
                // {
                //     id: 3,
                //     show:false,
                //     isActive: false,
                //     isFinished: false,
                //     formData: [
                //         {
                //             name: 'submission',
                //             type: 'noValidation',
                //             validated: null,
                //             content: '',
                //             error: ''
                //         },
                //     ],
                //     validated: false,
                //     subtitle: 'Submit Message'
                // }
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
                        field.error = 'This field is required.'
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
            console.log('form submitted');
            console.log(this.windows[0].formData[0].content);
            axios.post('http://localhost:5000/submit/report', {
                productName: this.windows[0].formData[0].content, 
                companyName: this.windows[0].formData[1].content, 
                dataLocation: this.windows[0].formData[2].content,
                standard: this.windows[1].formData[0].content,
                setup: this.windows[1].formData[1].content,
                power: this.windows[1].formData[2].content,
                class_: this.windows[2].formData[0].content,
                lisn: this.windows[2].formData[1].content,
                specA: this.windows[2].formData[2].content,
                })
        },

        // submitSuccess(){
        //     this.submitted = axios.get('http://localhost:5000/submit/report')
        // },

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
    width: 100%;
}

.customSelect:hover{
    transform: scale(1.01);
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
    margin: auto;
    width: 90%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.formContentContainer{
    display: flex;
    flex-direction: column;
    padding: 20px 0px;
    width: 100%;
    align-self: flex-start;
    align-items: center;
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

.formFieldContainer{
    width: 50%;
}

.navButtonContainer{
    align-self: flex-end;
    margin-right: 75px;
    margin-top: auto;
}

.stepContainer{
    text-align: center;
    margin: 0px 0px 20px 0px;
}

button{
    background-color: #34495e;
    text-decoration: none;
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

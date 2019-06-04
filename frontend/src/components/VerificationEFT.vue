<template>
    <!-- EMC Report Creation Form -->
    <form @submit = 'formSubmit' autocomplete = 'off' class = 'sectionContainer' method = 'POST'>

        <!-- Step 1 - Project Information -->
        <div class = 'colContainer'>

            <!-- Subtitle -->
            <div class = 'subtitle'>
                {{subtitle}}
            </div>
            <hr>

            <!-- Form Layout Tab -->
            <div class = 'formContainer'>

                <!-- Form Content -->
                <div v-if = 'windows[0].show' class = 'formContentContainer'>
                    <ol class = 'list-L'>

                        <li>
                            Setting axis scales:
                            
                            <p>
                                i) Under "Vertical" panel: Set "Scale 1" to 2.5kV maximum value
                            </p>

                            <p>
                                ii) Under "Horizontal" panel: Set "Scale" to 10.0ns
                            </p>
                            
                        </li>

                        <li>
                            Setting trigger:

                            <p>
                                i) Under "Trigger" panel: Set "Level" above noise floor
                            </p>

                            <p>
                                ii) Under "Horizontal" panel: Set "Position" so that the trigger point is located in the first half of the display
                            </p>
                        </li>

                        <li>
                            Start EFT test at a level of +4kV out of the direct output. Set the oscilloscope into "Single" capture mode
                        </li>

                        <li>
                            Using the "Multipurpose" dials with the "Fine" button selected, set the horizontal markers: 

                            <p>
                                i) "Line B" to 0V
                            </p>

                            <p>
                                ii) "Line A" to the peak of the waveform
                            </p>
                        </li>

                        <li>
                            Record the measured peak value below:
                        </li>

                        <div>
                            <input placeholder = 'Peak Value: 1800V - 2200V' v-model = 'formData.peak' class = 'formField' type="text" name = 'peak'>
                        </div>

                    </ol>

                    
                    <div class = 'setupPhoto-R'>
                        <img src="../assets/EFT_PK.png" alt="EFT Peak" height= '326.4' width= '435.2'>
                    </div>
                    
                    

                </div>

                <div v-if = 'windows[1].show' class = 'formContentContainer'>
                    
                </div>

                 <div v-if = 'windows[2].show' class = 'formContentContainer'>
                    
                </div>

                <!-- Form Navigation -->
                <div class = 'navButtonContainer'>
                    <button type = 'button' v-on:click = "nextPrev(-1)" v-if = 'buttonPrevious'>Previous</button>
                    <button type = 'button' v-on:click = "nextPrev(1)" v-if = 'buttonNext'>Next</button>
                    <router-link to = '/verifications/success'><button v-if = 'buttonSubmit'>Submit</button></router-link>
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
    name: 'VerificationForm',
    data() {
        return{
            formData: {
                peak: "",
            },
            subtitle: 'EFT Verification',
            currentWindow: 0,
            buttonPrevious: false,
            buttonSubmit: false,
            buttonNext: true,
            windows: [
                {
                    id: 0,
                    show: true,
                    isActive: true,
                    isFinished: false,
                    subtitle: 'EFT Verification'
                },
                {
                    id: 1,
                    show: false,
                    isActive: false,
                    isFinished: false,
                    subtitle: 'Verification Equipment'
                },
                {
                    id: 2,
                    show:false,
                    isActive: false,
                    isFinished: false,
                    subtitle: 'Verification Setup'
                },
                {
                    id: 3,
                    show:false,
                    isActive: false,
                    isFinished: false,
                    subtitle: 'Verification Setup'
                },
            ]
            
        }
    },
    methods: {
        nextPrev(n){
            this.windows[this.currentWindow].show = false;
            this.windows[this.currentWindow].isFinished = true;
            this.windows[this.currentWindow].isActive = false;
            this.currentWindow += n;
            this.subtitle = this.windows[this.currentWindow].subtitle;
            this.windows[this.currentWindow].show = true;
            this.windows[this.currentWindow].isActive = true;
            console.log(this.currentWindow)
            console.log(this.windows.length)

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
            
        },

        formSubmit(e){
            e.preventDefault();
            axios.post('http://localhost:5000/submit/eftverification')
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
    width: 90%;
    padding: 20px 0px;
    /* flex-grow: 1; */
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}

.formContentContainer{
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-evenly;
    align-items: center;
    /* padding: 20px; 
    background-color: #f1f1f1;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    margin-bottom: 40px; */
}

.setupPhoto-L{
    padding-right: 40px;
    border-right: 2px solid rgba(0, 0, 0, .075);
}

.setupPhoto-R{
    padding-left: 40px;
    border-left: 2px solid rgba(0, 0, 0, .075);
}

.list-R li, .list-L li{
    margin: 10px 0px;
    margin-left: 25px;
}

.list-L{
    padding-left: 0;
    padding-right: 40px;
    flex-basis: 50%;
}

.list-R{
    flex-basis: 50%;
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
    margin-right: 10px;
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

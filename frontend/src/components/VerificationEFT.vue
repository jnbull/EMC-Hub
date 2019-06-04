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
                <div v-if = 'windows[0].show' class = 'formFieldContainer'>
                    <p>
                        <label class = 'formLabel' for="date">Date</label>
                        <input v-model = 'formData.date' class = 'formField' type="text" name = 'date'>
                    </p>
                    
                    <p>
                        <label class = 'formLabel' for="engineer">EMC Engineer</label>
                        
                        <select name = 'engineer' class = 'customSelect' v-model= "formData.engineer">
                            <option disabled value="">Select: </option>
                            <option value = 'Raymond Au'>Raymond Au</option>
                            <option value = 'Jadon Bull'>Jadon Bull</option>
                        </select>
                    </p>

                     <p>
                        <label class = 'formLabel' for="asset">Generator Asset Number</label>
                        
                        <select name = 'asset' class = 'customSelect' v-model= "formData.asset">
                            <option disabled value="">Select: </option>
                            <option value = 'GEMC 4'>GEMC 4</option>
                            <option value = 'GEMC 188'>GEMC 188</option>
                            <option value = 'GEMC 317'>GEMC 317</option>
                        </select>
                    </p>

                     <p>
                        <label class = 'formLabel' for="generate">Create Verification Form?</label>
                        
                        <select name = 'generate' class = 'customSelect' v-model= "formData.generate">
                            <option disabled value="">Select: </option>
                            <option value = 'true'>Yes</option>
                            <option value = 'false'>No</option>
                        </select>
                    </p>
                    
                </div>

                <div v-if = 'windows[1].show' class = 'formContentContainer'>
                    
                </div>

                <div v-if = 'windows[2].show' class = 'formContentContainer'>
                    
                </div>

                <div v-if = 'windows[3].show' class = 'formContentContainer'>
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
                            <input placeholder = 'Peak Value: 1800V - 2200V' v-on:change = 'calculatePeaks' v-model = 'formData.peak' class = 'formField' type="text" name = 'peak'>
                        </div>

                    </ol>

                    
                    <div class = 'setupPhoto-R'>
                        <img src="../assets/EFT_PK.png" alt="EFT Peak" height= '326.4' width= '435.2'>
                    </div>
                </div>

                <div v-if = 'windows[4].show' class = 'formContentContainer'>
                    <div class = 'setupPhoto-L'>
                        <img src="../assets/EFT_RT.png" alt="EFT Rise Time" height= '326.4' width= '435.2'>
                    </div>

                    <ol class = 'list-R'>
                        <li>
                            Using the "Multipurpose" dials with the "Fine" button selected, set the horizontal markers as follows:

                            <p>
                                i) "Line B" to 10% of the previously measured peak value: <strong>{{formData.peak10}}</strong>
                            </p>

                            <p>
                                ii) "Line A" to 90% of the previouly measured peak value: <strong>{{formData.peak90}}</strong>
                            </p>

                        </li>

                        <li>
                            Using the "Select" button to switch axes, set the vertical markers with the "Multipurpose" dials as follows:

                            <p>
                                i) "Line A" to intersect with horizontal "Line B" at 10% of the peak value
                            </p>

                            <p>
                                ii) "Line B" to intersect with horizontal "Line A" at 90% of the peak value
                            </p>
                        </li>

                        <li>
                            Record the delta time value as the rise time below:
                        </li>
                        
                        <div>
                            <input placeholder = 'Rise Time: 3.5ns - 6.5ns' v-model = 'formData.riseTime' class = 'formField' type="text" name = 'riseTime'>
                        </div>
                        
                    </ol>
                </div>

                <div v-if = 'windows[5].show' class = 'formContentContainer'>

                    <ol class = 'list-L'>
                        <li>
                            Using the "Multipurpose" dials with the "Fine" button selected, set the horizontal markers as follows:

                            <p>
                                i) "Line B" to 0V
                            </p>

                            <p>
                                ii) "Line A" to 50% of the previouly measured peak value: <span class = 'bold'>{{formData.peak50}}</span>
                            </p>

                        </li>

                        <li>
                            Using the "Select" button to switch axes, set the vertical markers with the "Multipurpose" dials as follows:

                            <p>
                                i) "Line A" to intersect with horizontal "Line A" at the first instance on the waveform
                            </p>

                            <p>
                                ii) "Line B" to intersect with horizontal "Line A" at the second instance on the waveform.
                            </p>
                        </li>

                        <li>
                            Record the delta time value as the fall time below:
                        </li>

                        <div>
                            <input placeholder = 'Fall Time: 35ns - 65ns' v-model = 'formData.fallTime' class = 'formField' type="text" name = 'fallTime'>
                        </div>
                        

                    </ol>

                    <div class = 'setupPhoto-R'>
                        <img src="../assets/EFT_FT.png" alt="EFT Fall Time" height= '326.4' width= '435.2'>
                    </div>
                </div>

                <div v-if = 'windows[6].show' class = 'formContentContainer'>
                    <div class = 'setupPhoto-L'>
                        <img src="../assets/EFT_BP.png" alt="EFT Burst Period" height= '326.4' width= '435.2'>
                    </div>

                    <ol class = 'list-R'>

                        <li>
                            Under "Horizontal" panel, set "Scale" to 4.00ms
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
                            Using the "Multipurpose" dials with the "Fine" button selected, set the vertical markers as follows:

                            <p>
                                i) "Line A" to the beginning of the burst
                            </p>

                            <p>
                                ii) "Line B" to the end of the burst
                            </p>

                        </li>

                        <li>
                            Record the delta time value as Burst Period below:
                        </li>
                        
                        <div>
                            <input placeholder = 'Burst Period: 12ms - 18ms' v-model = 'formData.burstPeriod' class = 'formField' type="text" name = 'burstPeriod'>
                        </div>
                        
                    </ol>
                </div>

                <div v-if = 'windows[7].show' class = 'formContentContainer'>

                    <ol class = 'list-L'>

                        <li>
                            Under "Horizontal" panel, set "Scale" to 100ms
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
                            Using the "Multipurpose" dials with the "Fine" button selected, set the vertical markers as follows:

                            <p>
                                i) "Line A" to the beginning of the first burst
                            </p>

                            <p>
                                ii) "Line B" to the beginning of the next burst
                            </p>

                        </li>

                        <li>
                            Record the delta time value as Burst Duration below:
                        </li>

                    <div>
                        <input placeholder = 'Burst Duration: 240ms - 360ms' v-model = 'formData.burstDuration' class = 'formField' type="text" name = 'burstDuration'>
                    </div>
                    

                </ol>

                <div class = 'setupPhoto-R'>
                    <img src="../assets/EFT_BD.png" alt="EFT Burst Duration" height= '326.4' width= '435.2'>
                </div>
                </div>
                
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
                <span v-bind:class = "{active: windows[3].isActive, finish: windows[3].isFinished}" class="step"></span>
                <span v-bind:class = "{active: windows[4].isActive, finish: windows[4].isFinished}" class="step"></span>
                <span v-bind:class = "{active: windows[5].isActive, finish: windows[5].isFinished}" class="step"></span>
                <span v-bind:class = "{active: windows[6].isActive, finish: windows[6].isFinished}" class="step"></span>
                <span v-bind:class = "{active: windows[7].isActive, finish: windows[7].isFinished}" class="step"></span>
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
                date: '',
                engineer: '',
                generate: '',
                asset: '',
                peak: "",
                peak10: "",
                peak90: "",
                peak50: "",
                riseTime: '',
                fallTime: '',
                burstPeriod: '',
                burstDuration: ''
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
                    subtitle: 'Peak Value Measurement'
                },
                {
                    id: 4,
                    show:false,
                    isActive: false,
                    isFinished: false,
                    subtitle: 'Rise Time Measurement'
                },
                {
                    id: 5,
                    show:false,
                    isActive: false,
                    isFinished: false,
                    subtitle: 'Fall Time Measurement'
                },
                {
                    id: 6,
                    show:false,
                    isActive: false,
                    isFinished: false,
                    subtitle: 'Burst Period Measurement'
                },
                {
                    id: 7,
                    show:false,
                    isActive: false,
                    isFinished: false,
                    subtitle: 'Burst Duration Measurement'
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
        },

        calculatePeaks(){
            this.formData.peak10 = (this.formData.peak * 0.10) + 'V'; 
            this.formData.peak90 = (this.formData.peak * 0.90) + 'V';
            this.formData.peak50 = (this.formData.peak * 0.50) + 'V';
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
    width: 100%;
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
    margin: auto;
    width: 90%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.formContentContainer{
    margin-top: 20px;
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-evenly;
    align-items: center;
    height: 100%;
    padding: 10px;
}

.formFieldContainer{
    display: flex;
    flex-direction: column;
    padding: 20px 0px;
    width: 100%;
    align-self: flex-start;
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
    margin-right: 75px;
    margin-top: auto;
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
    margin: 0px 0px 20px 0px;
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

p{
    margin-left: 10px;
    margin: 2px 0px;
}

</style>

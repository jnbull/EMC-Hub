<template>
        <!-- EMC Report Creation Form -->
        <form autocomplete = 'off' class = 'sectionContainer' method = 'POST'>
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

                        <!-- Product Name -->
                        <p>
                            <!-- {{ reportForm.productName.label(class_='formLabel') }}
                            {{ reportForm.productName(class_='formField') }} -->
                        </p>

                        <!-- Company Name -->
                        <p>
                            <!-- {{ reportForm.companyName.label(class_='formLabel') }}
                            {{ reportForm.companyName(class_='formField') }} -->
                        </p>

                        <!-- EMC Folder Location -->
                        <p>
                            <!-- {{ reportForm.dataLocation.label(class_='formLabel') }}
                            {{ reportForm.dataLocation(class_='formField') }} -->
                        </p>

                    </div>

                    <div class = 'formContentContainer'>

                        <!-- Product Standard -->
                        <p>
                            <!-- {{ reportForm.standard.label(class_='formLabel') }}
                            {{ reportForm.standard(class_='formField') }} -->
                        </p>

                        <!-- Product Class -->
                        <p>
                            <!-- {{ reportForm.productClass.label(class_='formLabel') }}
                            {{ reportForm.productClass(class_='formField') }} -->
                        </p>

                        <!-- Input Power -->
                        <p>
                            <!-- {{ reportForm.power.label(class_='formLabel') }}
                            {{ reportForm.power(class_='formField') }} -->
                        </p>

                    </div>

                    <div class = 'formContentContainer'>

                        <!-- Test Setup -->
                        <p>
                            <!-- {{ reportForm.setup.label(class_='formLabel') }}
                            {{ reportForm.setup(class_='formField') }} -->
                        </p>

                        <!-- Spectrum Analyzer -->
                        <p>
                            <!-- {{ reportForm.specPLCE.label(class_='formLabel') }}
                            {{ reportForm.specPLCE(class_='formField') }} -->
                        </p>

                        <!-- LISN -->
                        <p>
                            <!-- {{ reportForm.lisnPLCE.label(class_='formLabel') }}
                            {{ reportForm.lisnPLCE(class_='formField') }} -->
                        </p>

                    </div>

                    <!-- Form Navigation -->
                    <div class = 'navButtonContainer'>
                        <button type = 'button' id = 'buttonPrevious' onclick = "nextPrev(-1)">Previous</button>
                        <button type = 'button' id = 'buttonNext' onclick = "nextPrev(1)"></button>
                    </div>

                    <!-- Form Step Bubbles -->
                    <div class = 'stepContainer'>
                        <span class="step"></span>
                        <span class="step"></span>
                        <span class="step"></span>
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
export default {
    name: 'ReportForm',
    delimiters: ['[[',']]']
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
    display: none;
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

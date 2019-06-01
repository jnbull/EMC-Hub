<template>

    <!-- EMC Report Creation Form -->
    <form autocomplete = 'off' id = 'reportForm' class = 'sectionContainer' method = 'POST'>
    {{ reportForm.hidden_tag() }}

        <!-- Step 1 - Project Information -->
        <div class = 'colContainer one'>

            <!-- Subtitle -->
            <div class = 'subtitle'>
                <h3 id = 'formTitle'>Project Information</h3>
            </div>
            <hr>

            <!-- Form Layout Tab -->
            <div class = 'formContainer'>

                <!-- Form Content -->
                <div class = 'formContentContainer'>

                    <!-- Product Name -->
                    <p>
                        {{ reportForm.productName.label(class_='formLabel') }}
                        {{ reportForm.productName(class_='formField') }}
                    </p>

                    <!-- Company Name -->
                    <p>
                        {{ reportForm.companyName.label(class_='formLabel') }}
                        {{ reportForm.companyName(class_='formField') }}
                    </p>

                    <!-- EMC Folder Location -->
                    <p>
                        {{ reportForm.dataLocation.label(class_='formLabel') }}
                        {{ reportForm.dataLocation(class_='formField') }}
                    </p>

                </div>

                <div class = 'formContentContainer'>

                    <!-- Product Standard -->
                    <p>
                        {{ reportForm.standard.label(class_='formLabel') }}
                        {{ reportForm.standard(class_='formField') }}
                    </p>

                    <!-- Product Class -->
                    <p>
                        {{ reportForm.productClass.label(class_='formLabel') }}
                        {{ reportForm.productClass(class_='formField') }}
                    </p>

                    <!-- Input Power -->
                    <p>
                        {{ reportForm.power.label(class_='formLabel') }}
                        {{ reportForm.power(class_='formField') }}
                    </p>

                </div>

                <div class = 'formContentContainer'>

                    <!-- Test Setup -->
                    <p>
                        {{ reportForm.setup.label(class_='formLabel') }}
                        {{ reportForm.setup(class_='formField') }}
                    </p>

                    <!-- Spectrum Analyzer -->
                    <p>
                        {{ reportForm.specPLCE.label(class_='formLabel') }}
                        {{ reportForm.specPLCE(class_='formField') }}
                    </p>

                    <!-- LISN -->
                    <p>
                        {{ reportForm.lisnPLCE.label(class_='formLabel') }}
                        {{ reportForm.lisnPLCE(class_='formField') }}
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
    name: 'ReportForm'
}
</script>

<style scoped>

</style>

<template>
    <!-- Home Page Container -->
    <div id = 'home'>

        <!-- Jumbotron -->
        <div class = 'colContainer one'>

            <!-- App Title -->
            <div class = 'title'>
                <img class = 'bigLogo' src="../assets/biglogo.svg" alt="TUV Logo">
                <h1>EMC Hub</h1>
            </div>
            <hr>

            <!-- Sections Container -->
            <div class = 'homeButtonContainer'>

                <!-- Report Section Button -->
                <div id = 'startReport' class = 'homeButton'>
                    <i class="fas fa-file-alt bigIcon"></i>
                    <div class = 'startContainer'>
                        <h3 class = 'startSubtitle'><strong>Report Creation</strong></h3>
                        <hr>
                        <div class = 'startContent'>
                            <p>
                                Automated Data Processing for:
                            </p>
                            <ul>
                                <li>EMC Reports</li>
                                <li>Findings Letters</li>
                                <li>Prescan Data</li>
                            </ul>
                        </div>
                    </div>
                </div>
                
                <!-- Verifications Section Button -->
                <div id = 'startVerification' class = 'homeButton'>
                    <i class="fas fa-clipboard-check bigIcon"></i>
                    <div class = 'startContainer'>
                        <h3 class = 'startSubtitle'><strong>Equipment Verification</strong></h3>
                        <hr>
                        <div class = 'startContent'>
                            <p>
                                Automated Generation of:
                            </p>
                            <ul>
                                <li>Equipment Verification Forms</li>
                                <li>Test Setup Verification Trends</li>
                                <li>Verification Procedures</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Environmental Conditions Section Button -->
                <div class = 'homeButton'>
                    <i id = 'startEnviro' class="fas fa-thermometer-half bigIcon"></i>
                    <div class = 'startContainer'>
                        <h3 class = 'startSubtitle'><strong>Environmental Conditions</strong></h3>
                        <hr>
                        <div class = 'startContent'>
                            <p>
                                Automated Database for Use in:
                            </p>
                            <ul>
                                <li>EMC Reports</li>
                                <li>Verification Records</li>
                                <li>Laboratory Regulation</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Home'
}
</script>

<style scoped>

</style>


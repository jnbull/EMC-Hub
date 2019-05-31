<template>
    <!-- Home Page Container -->
    <div class = 'sectionContainer'>

        <!-- Jumbotron -->
        <div class = 'colContainer'>

            <!-- App Title -->
            <div class = 'title'>
                <img class = 'bigLogo' src="../assets/biglogo.svg" alt="TUV Logo">
                <h1>EMC Hub</h1>
            </div>
            <hr>

            <!-- Sections Container -->
            <div class = 'homeButtonContainer'>

                <!-- Report Section Button -->
                <router-link to = '/reports' class = 'homeButton'>
                    <font-awesome-icon icon = 'file-alt' class = 'bigIcon'/>
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
                </router-link>
                
                <!-- Verifications Section Button -->
                <router-link to = '/verifications' class = 'homeButton'>
                    <font-awesome-icon icon = 'clipboard-check' class = 'bigIcon'/>
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
                </router-link>

                <!-- Environmental Conditions Section Button -->
                <router-link to = '/environmental' class = 'homeButton'>
                    <font-awesome-icon icon = 'thermometer-half' class = 'bigIcon'/>
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
                </router-link>
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

.startContent{
    margin-top: 10px;
}

.startContent p, .startContent ul li{
    margin-top: 10px;
}

.startSubtitle{
    text-align: center;
    margin-bottom: 10px;
}

 .startContainer{
    color: whitesmoke;
    margin: 20px;
}

.colContainer{
    display: flex;
    flex-direction: column;
    background-color: white;
    border-radius: 5px;
    box-shadow: 0px 5px 2px -2px rgba(0,0,0,.2);
    background-color: #2c3e50;
    grid-column-start: 1;
    grid-column-end: 9;
    grid-row-start: 1;
    grid-row-end: 5;
}

.title{
    margin: auto;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    padding: 20px;
    color: whitesmoke;
    font-family: 'Oswald', sans-serif;
    font-size: 32pt;
}

.bigLogo{
    margin-right: 20px;
}

.homeButtonContainer{
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    height: 100%;
    padding: 20px;
}

.homeButton{
    cursor: pointer;
    border-radius: 5px;
    width: 325px;
    background-color: #34495e;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    box-shadow: 0 2px 2px -1px rgba(0,0,0,.2);
}

.sectionContainer{
  display: grid;
  grid-template-rows: repeat(4, 1fr);
  grid-template-columns: repeat(8, 1fr);
  grid-column-gap: 20px;
  grid-row-gap: 20px;
  padding: 40px;
  position: fixed;
  top: 65px;
  left: 65px;
  right: 0;
  bottom: 0;
}

.homeButton{
    transition: transform .2s;
}

.homeButton:hover{
    transform: scale(1.05);
}

.bigIcon{
    cursor: pointer;
    font-size: 62pt;
    color: whitesmoke;
}

</style>


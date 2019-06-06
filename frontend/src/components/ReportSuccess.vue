<template>
    <!-- Home Page Container -->
    <div class = 'sectionContainer'>

        <!-- Jumbotron -->
        <div class = 'colContainer'>

            <!-- App Title -->
            <div class = 'title'>
                <!-- <img class = 'bigLogo' src="../assets/biglogo.svg" alt="TUV Logo"> -->
                <h1>Report Created</h1>
            </div>
            <hr>

            <!-- Options Container -->
            <div class = 'successButtonContainer'>

                <!-- Success Route Options -->
                <form @submit = 'fileOpen' class = 'homeButton' method="POST">
                    <button>
                        <font-awesome-icon icon = 'folder-open' class = 'bigIcon'/>
                        <div class = 'startContainer'>
                            <h3 class = 'startSubtitle'><strong>Open Output Directory</strong></h3>
                        </div>
                    </button>
                </form>
                
                <!-- Verifications Section Button -->
                <router-link to = '/reports' class = 'homeButton'>
                    <font-awesome-icon icon = 'file-alt' class = 'bigIcon'/>
                    <div class = 'startContainer'>
                        <h3 class = 'startSubtitle'><strong>Create Another Report</strong></h3>
                    </div>
                </router-link>

                <!-- Environmental Conditions Section Button -->
                <router-link to = '/' class = 'homeButton'>
                    <img class = 'bigLogo' src="../assets/successlogo.svg" alt="TUV Logo">
                    <div class = 'startContainer'>
                        <h3 class = 'startSubtitle'><strong>Return to Home</strong></h3>
                    </div>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'ReportSuccess',
    methods: {
        fileOpen(e){
            e.preventDefault()
            axios.post('http://localhost:5000/submit/fileopen')
        }
    }
}
</script>

<style scoped>
button:hover{
    transform: scale(1);
}
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
    color:#0bab64;
    margin: 20px;
}
.colContainer{
    display: flex;
    flex-direction: column;
    border-radius: 5px;
    box-shadow: 0px 5px 2px -2px rgba(0,0,0,.2);
    background-color: #0bab64;
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
.successButtonContainer{
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
    background-color: whitesmoke;
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
    color:#0bab64;
}
</style>

<template>
    <!-- Report Creation Container -->
    <div class = 'sectionContainer'>

        <!-- Create EMC Report -->
        <div class = 'colContainer optionOne'>
            <div class = 'subtitle'>
                Test Setup Verification
            </div>
            <hr>

            <router-link to = '/verifications/create/testsetup' class = 'optionButtonContainer'>
                <button type = 'button'>Create</button>
            </router-link>
        </div>

        <!-- Create Findings Letter -->
        <div class = 'colContainer optionTwo'>
            <div class = 'subtitle'>
                Individual Equipment Verification
            </div>
            <hr>

            <router-link to = '/verifications/create/equipment' class = 'optionButtonContainer'>
                <button type = 'button'>Create</button>
            </router-link>
        </div>

        <!-- Zip Raw Data -->
        <div class = 'colContainer optionThree'>
            <div class = 'subtitle'>
                Equipment Factors
            </div>
            <hr>

            <router-link to = '/verifications/create/factors' class = 'optionButtonContainer'>
                <button type = 'button'>Create</button>
            </router-link>
        </div>

    </div>
</template>

<script>
export default {
    name: 'VerificationCreation',
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
    }

    .subtitle{
    display: flex;
    justify-content: center;
    align-items: center;
    display: relative;
    color: white;
    padding: 15px;
    font-size: 1.17em;
    font-weight: normal;
    font-stretch: normal;
    text-align: center;
    background-color:#34495e;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    border-bottom: solid 2px #2c3e50;
    
}

    .optionButtonContainer{
        margin: auto auto 40px auto;
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

    .optionOne{
        grid-column-start: 1;
        grid-column-end : 2;
        grid-row-start: 1;
        grid-row-end: 4;
    }

    .optionTwo{
        grid-column-start: 2;
        grid-column-end : 3;
        grid-row-start: 1;
        grid-row-end: 4;
    }

    .optionThree{
        grid-column-start: 3;
        grid-column-end : 4;
        grid-row-start: 1;
        grid-row-end: 4; 
    }



</style>

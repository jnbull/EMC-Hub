<template>
    <div class = 'sectionContainer'>

        <router-link to = "/verifications/create/testsetup/eft" class = 'colContainer one'>
            <div class = 'subtitle'>
                <h3>EFT</h3>
            </div>
            <hr>
        </router-link>

        <div class = 'colContainer two'>
        
        </div>

        <div class = 'colContainer three'>
            
        </div>

        <div class = 'colContainer four'>
            
        </div>

        <div class = 'colContainer five'>
            
        </div>

        <div class = 'colContainer six'>
            
        </div>

        <div class = 'colContainer seven'>
            
        </div>

        <div class = 'colContainer eight'>
            
        </div>

    </div>
</template>

<script>
export default {
    name: 'VerificationTests',
    methods:{
        sendPageName(){
            this.$emit('pageName', 'Test Setup Verifications')
        },
    },
    beforeMount(){
      this.sendPageName()
    }
}
</script>

<style scoped>
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
        cursor: pointer;
        transition: transform .2s;
    }

    .colContainer:hover{
        transform: scale(1.05);
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

    .one{
        grid-column-start: 1;
        grid-column-end: 3;
        grid-row-start: 1;
        grid-row-end: 3;
    }

    .two{
        grid-column-start: 3;
        grid-column-end: 5;
        grid-row-start: 1;
        grid-row-end: 3;
    }

    .three{
        grid-column-start: 5;
        grid-column-end: 7;
        grid-row-start: 1;
        grid-row-end: 3;
    }

    .four{
        grid-column-start: 7;
        grid-column-end: 9;
        grid-row-start: 1;
        grid-row-end: 3;
    }

    .five{
        grid-column-start: 1;
        grid-column-end: 3;
        grid-row-start: 3;
        grid-row-end: 5;
    }

    .six{
        grid-column-start: 3;
        grid-column-end: 5;
        grid-row-start: 3;
        grid-row-end: 5;
    }

    .seven{
        grid-column-start: 5;
        grid-column-end: 7;
        grid-row-start: 3;
        grid-row-end: 5;
    }

    .eight{
        grid-column-start: 7;
        grid-column-end: 9;
        grid-row-start: 3;
        grid-row-end: 5;
    }
</style>



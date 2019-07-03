<template>
    <!-- Report Page Container -->
    <div class = 'sectionContainer'>

        <!-- Create Report Button -->
        <router-link to='/reports/create' class = 'colContainer plusIconContainer'>
            <i><font-awesome-icon icon = 'plus' class = 'plusIcon'/></i>
        </router-link>

        <!-- Report Widget 1 -->
        <div class = 'colContainer widgetOne'>
            <div class = 'subtitle'>
                Report Widget 1
            </div>
            <hr>
        </div>

        <!-- Report Widget 2 -->
        <div class = 'colContainer widgetTwo'>
            <div class = 'subtitle'>
                Report Widget 2
            </div>
            <hr>
        </div>

        <!-- Report Widget 3 -->
        <div class = 'colContainer widgetThree'>
            <div class = 'subtitle'>
                Report Widget 3
            </div>
            <hr>
        </div>

    </div>
</template>

<script>
export default {
    name: 'ReportLanding',
    methods:{
        sendPageName(){
            this.$emit('pageName', 'Reports')
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
}

.plusIconContainer{
    display: flex;
    justify-content: center;
    align-items: center;
    grid-column-start: 1;
    grid-column-end: 2;
    grid-row-start: 1;
    grid-row-end: 2;
    cursor: pointer;
    background-color: #3bb78f;
    background-image: linear-gradient(315deg, #3bb78f 0%, #0bab64 74%);
    transition: transform .2s;
}

.plusIcon{
    font-size: 48pt;
    color: whitesmoke;
}

.plusIconContainer:hover{
    transform: scale(1.05);
}

.widgetOne{
    grid-column-start: 4;
    grid-column-end : 9;
    grid-row-start: 1;
    grid-row-end: 5; 
}

.widgetTwo{
    grid-column-start: 2;
    grid-column-end : 4;
    grid-row-start: 1;
    grid-row-end: 2;
}

.widgetThree{
    grid-column-start: 1;
    grid-column-end : 4;
    grid-row-start: 2;
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


</style>




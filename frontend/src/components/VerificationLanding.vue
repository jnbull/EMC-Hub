<template>
    <!-- Report Page Container -->
    <div class = 'sectionContainer'>

        <!-- Create Report Button -->
        <router-link to='/verifications/create' class = 'colContainer plusIconContainer'>
            <i><font-awesome-icon icon = 'plus' class = 'plusIcon'/></i>
        </router-link>

        <!-- Report Widget 1 -->
        <div class = 'colContainer widgetOne'>
            <div class = 'subtitle'>
                <div class = 'barsIconSml'>
                    <font-awesome-icon icon = 'bars'/>
                </div>

                <div>
                    My Verification List
                </div>
                
                <div class = 'plusIconSml'>
                    <font-awesome-icon icon = 'plus'/>
                </div>
            </div>

            <div class = 'todoContainer'>
                <div class = 'todoItem' v-bind:class = "{'completed':todo.completed}" v-bind:key = "todo.id" v-for = "todo in todos">
                    <div class = 'todo checkContainer'>
                        <input class = 'check' type="checkbox">
                    </div>
                    <div class = 'todo'>{{todo.title}}</div>
                    <div class = 'todo'>{{todo.type}}</div>
                    <div class = 'todo'>{{todo.category}}</div>
                </div>
            </div>

            <div class = 'navButtonContainer'>
                <button>Verify Selected</button>
            </div>
        </div>

        <!-- Report Widget 2 -->
        <div class = 'colContainer widgetTwo'>
            <div class = 'subtitle'>
                Next Verification Due
            </div>
            <hr>
        </div>

        <!-- Report Widget 3 -->
        <div class = 'colContainer widgetThree'>
            <div class = 'subtitle'>
                My Requests
            </div>
            <hr>
        </div>

    </div>
</template>

<script>
export default {
    name: 'VerificationLanding',
     data(){
        return {
            todos: [
                {
                id: 1,
                category: 'Individual Equipment',
                type: 'Current Probe',
                title: 'GEMC 125',
                completed: false
                },
                {
                id: 2,
                type: 'Current Probe',
                category: 'Individual Equipment',
                title: 'GEMC 19',
                completed: false
                },
                {
                id: 3,
                type: 'Immunity',
                category: 'Test Setup',
                title: 'EFT',
                completed: false
                }
            ]
        }
  }
}
</script>

<style scoped>

.todo{
    width: 175px;
    display: inline-block;
    padding: 10px;
    border-left: lightgray 2px solid;
}

.checkContainer{
    width: 35px;
    text-align: center;
    border: none;
    padding: 0px;
}

.check{
    zoom: 1.5;
    margin-left: 4px;
}
.todoItem{
    border-bottom: lightgray solid 2px;
}

.todoItem:hover{
    background-color: lightgray;
    cursor: pointer;
}

.completed{
    background-color:#3bb78f;
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
    text-align: right;
    margin-left: auto;
}

.plusIconSml{
    font-size: 14pt;
    color: whitesmoke;
    margin-left: auto;
    cursor: pointer;
    transition: transform .2s;
}

.barsIconSml{
    font-size: 14pt;
    color: whitesmoke;
    margin-right: auto;
    cursor: pointer;
    transition: transform .2s;
}

.plusIconContainer:hover, button:hover{
    transform: scale(1.05);
}

.plusIconSml:hover, .barsIconSml:hover{
    transform: scale(1.15);
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

.navButtonContainer{
    align-self: center;
    margin-top: auto;
    margin-bottom: 25px;
}

button{
    background-color: #34495e;
    text-decoration: none;
    padding: 10px;
    color: whitesmoke;
    border-radius: 5px; 
    width: 150px;
    height: 100%;
    font-size: 12pt;
    text-align: center;
    cursor: pointer;
    transition: transform .2s;
}


</style>




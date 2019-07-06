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
                <div v-on:click = 'addItem = !addItem, singleItem = false, offsite = false, searchItem = false' class = 'barsIconSml'>
                    <font-awesome-icon icon = 'bars'/>
                </div>

                <div>
                    My Verification List
                </div>
                
                <div v-on:click = 'addSingleItem' class = 'plusIconSml'>
                    <font-awesome-icon icon = 'plus'/>
                </div>
            </div>

            <div v-if = 'addItem' class = 'addItemContainer'>
                <div v-on:click = 'addSingleItem' class = 'addItemChoice'>Add Item</div>
                <div v-on:click = 'addSearch' class = 'addItemChoice'>Search Database</div>
                <label class = 'addItemChoice'>
                    Upload Offsite List
                    <input ref = 'file' type='file' v-on:change = 'handleFileUpload' class = 'addItemChoice'>
                </label>
            </div>

            <div v-if= 'offsite' class = 'addContentContainer'>
                <div>Filename: {{file.name}}</div>
                <button class = 'addButton' v-on:click = 'submitFile'>Submit</button>
                <!-- <button class = 'cancelButton' v-on:click = 'cancelOffsite'>Cancel</button> -->
            </div>

            <div v-if= 'singleItem' class = 'addContentContainer'>
                <div>
                    <input type="text" placeholder="Add Item by GEMC ID" v-model = 'addTodo.id' class = 'textField'>
                    <button class= 'addButton' v-on:click = 'addEquipmentTodo(addTodo.id)'>Add</button>
                </div>
            </div>

            <div v-if= 'searchItem' class = 'addContentContainer'>
                <div>
                    ID#: <input type="text" v-model = 'filters.id'>
                    Type: <input type="text" v-model = 'filters.type_'>
                    Manufacturer: <input type="text" v-model = 'filters.manufacturer'>
                    <button class= 'addButton' v-on:click = 'searchEquipment'>Search</button>
                </div>
            </div>

            <div class = 'listContainer'>
                <div class='listTitle'>
                    Search Results
                </div>

                <div class = 'todoContainer'>
                    <div v-on:click = 'todo.completed = !todo.completed' class = 'todoItem' v-bind:class = "{'completed':todo.completed}" v-bind:key = "todo.id" v-for = "todo in todos">
                        <div class = 'todo checkContainer'>
                            <input v-model = 'todo.completed' class = 'check' type="checkbox">
                        </div>
                        <div class = 'todo'></div>
                        <div class = 'todo'>{{todo.type}}</div>
                        <div class = 'todo'>{{todo.category}}</div>
                    </div>
                </div>

                <div class='listTitle'>
                    Verification List
                </div>

                <div class = 'todoContainer'>
                    <div v-on:click = 'todo.completed = !todo.completed' class = 'todoItem' v-bind:class = "{'completed':todo.completed}" v-bind:key = "todo.id" v-for = "todo in todos">
                        <div class = 'todo checkContainer'>
                            <input v-model = 'todo.completed' class = 'check' type="checkbox">
                        </div>
                        <div class = 'todo'>{{todo.title}}</div>
                        <div class = 'todo'>{{todo.type}}</div>
                        <div class = 'todo'>{{todo.category}}</div>
                    </div>
                </div>

            </div>

          

            <!-- <div class = 'navButtonContainer'>
                <button>Verify Selected</button>
            </div> -->
        </div>

        <!-- Report Widget 2 -->
        <div class = 'colContainer widgetTwo'>
            <!-- <div class = 'subtitle'>
                Next Verification Due
            </div>
            <hr> -->
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
import axios from 'axios'

export default {
    name: 'VerificationLanding',
     data(){
        return {
            addItem: false,
            singleItem: false,
            offsite: false,
            searchItem: false,
            // filename: '',
            file: '',
            filters: {
                id: '',
                manufacturer: '',
                type_: ''
            },
            addTodo: {
                id: '',
                category: '',
                type: '',
            },
            searchResult: '',
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
  },
  methods: {
      sendPageName(){
        this.$emit('pageName', 'Verifications')
    },
      handleFileUpload(){
        this.file = this.$refs.file.files[0];
        this.offsite = !this.offsite;
        this.addItem = !this.addItem;
      },
      submitFile(){
        let formData = new FormData();
        formData.append('file', this.file);
        axios.post('http://localhost:5000/submit/offsiteList',formData, {
            headers:{
                'Content-Type': 'multipart/form-data'
            }
        })
          .then(response => {this.addOffsite(response.data)})
      },
    //   addOffsite(assetList){
    //     const unique = [...new Set(assetList)]
    //     for (const item of unique){
    //         const newTodo = {
    //             id: '',
    //             category: 'Dummy',
    //             type: 'Dummy',
    //             title: item,
    //             completed: false
    //         }
    //         this.todos = [...this.todos, newTodo]
    //     }
    //   },
      addSingleItem(){
        //   this.addItem = !this.addItem;
          this.singleItem = !this.singleItem;
      },
      addSearch(){
          this.addItem = !this.addItem;
          this.searchItem = !this.searchItem;
      },
      searchEquipment(){
          axios.post('http://localhost:5000/query/equipment',this.filters)
          .then(response => {this.searchResult = response.data[0]})
          console.log(this.searchResult)
      },
      addEquipmentTodo(id){
          this.filters.id = id
          this.searchEquipment()
          axios.post('http://localhost:5000/add/todo/equipment', this.searchResult)
          .then(response => {console.log('Todo added')})
      }
  },
  beforeMount(){
      this.sendPageName()
  }
}
</script>

<style scoped>

.textField{
    height: 100%;
    width: 500px;
    padding: 5px;
    margin: 0px 15px;
}

.textField::placeholder{
    color: black;
    font-size: 9pt;
}

.listTitle{
    width: 100%;
    font-size: 11pt;
    background-color: lightgrey;
    padding:3px 3px 3px 10px;
}
input[type=file]{
    display: none;
}

.listContainer{
    height: 100%;
    overflow-y: scroll;
}

.addContentContainer{
    display: flex;
    justify-content: center;
    align-items: center;
    border-bottom: darkgray solid 2px;
    padding: 5px;
    color: whitesmoke;
    background-color:#34495e;
    height: 50px;
}

.addItemContainer{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: darkgray solid 2px;
    /* padding: 10px; */
    background-color: lightgrey;
    height: 50px;
}

.addItemChoice:hover{
    background-color: darkgray;
}

.todo{
    width: 175px;
    display: inline-block;
    padding: 10px;
    border-left: darkgrey 2px solid;
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
    border-bottom: darkgrey solid 2px;
}

.todoItem:hover{
    background-color: lightgray;
    cursor: pointer;
    opacity: 0.8;
}

.completed{
    background-color:lightgreen;
    /* opacity: 0.8; */
}

.completed:hover{
    background-color:lightgreen;
    opacity: 0.8;
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
    /* border-bottom: solid 2px #2c3e50; */
    
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

.addButton{
    color: black;
    width: 120px;
    height: 30px;
    padding: 5px;
    background-color: lightgreen;
}

.addItemChoice{
    display: flex;
    justify-content: center;
    align-items: center;   
    /* background-color: #34495e; */
    text-decoration: none;
    /* padding: 10px; */
    color: black;
    /* border-radius: 5px;  */
    height: 100%;
    font-size: 12pt;
    text-align: center;
    cursor: pointer;
    transition: transform .2s;
    width: 33%;
    margin: 0px;
}


</style>




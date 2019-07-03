<template>
  <div id="app">

    <!-- Top Navigation Bar -->
    <div>
      <Topnav :pageName = 'pageName'/>
    </div>

    <!-- Side Navigation Bar -->
    <div>
      <Sidenav/>
    </div>

    <!-- Page View -->
    <div>
      <transition name = 'show'>
        <router-view @pageName = 'setPageName'></router-view>
      </transition>
    </div>
    
  </div>
</template>

<script>

import Topnav from './components/Topnav.vue'
import Sidenav from './components/Sidenav.vue'

export default {
  name: 'App',
  components: {
    Topnav,
    Sidenav
  },
  data(){
    return {
      pageName: ''
    }
  },
  methods: {
    setPageName(pageName){
      this.pageName = pageName
      // console.log(this.pageName)
    }
  },
}
</script>

<style>

@import url('https://fonts.googleapis.com/css?family=Oswald|Roboto&display=swap');
  
*{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Roboto', sans-serif;
}

body{
  overflow: hidden;
  background-color: #ececec;
}

hr{
  width: 100%;
  opacity: 0.2;
}

ul{
  padding-left: 20px;
}

a{
  text-decoration: none;
}

.show-enter-active{
  transition: opacity 0.5s linear; 
}

.show-leave-active{
  transition: opacity 0.01s linear;
}

.show-enter, .show-leave{
  opacity: 0;
}

input:focus,
select:focus,
textarea:focus,
button:focus {
    outline: none;
}

button:hover{
  transform: scale(1.05);
}

button, input[type="submit"], input[type="reset"] {
	background: none;
	color: inherit;
	border: none;
	padding: 0;
	font: inherit;
	cursor: pointer;
	outline: inherit;
}

</style>

<template>
  <div id="app">

    <!-- Top Navigation Bar -->
    <div>
      <Topnav/>
    </div>

    <!-- Side Navigation Bar -->
    <div>
      <Sidenav/>
    </div>

    <!-- Page View -->
    <div class = 'sectionContainer'>
      <router-view></router-view>
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
  }
}
</script>

<style>
  
*{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body{
  font-family: Arial, Helvetica, sans-serif;
  overflow: hidden;
}

.sectionContainer{
  transition: opacity 0.5s linear; 
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

</style>

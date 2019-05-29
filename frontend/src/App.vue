<template>
  <div id="app">

    <!-- Top Navigation Bar -->
    <div class = 'topNav'>
      <Topnav/>
    </div>

    <!-- Side Navigation Bar -->
    <div class = 'sideNav'>
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

.topNav{
  display: flex;
  align-items: center;
  top: 0;
  left: 0;
  z-index: 2;
  width: 100%;
  height: 65px;
  background-color: white;
  box-shadow: 0 2px 2px -1px rgba(0,0,0,.2);
}

.sideNav{
  display: flex;
  flex-direction: column;
  position: fixed;
  z-index: 1;
  top: 65px;
  left: 0;
  width: 65px;
  bottom: 0;
  background-color: #34495e;
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

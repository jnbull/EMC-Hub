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
    <div>
      <transition name = 'show'>
        <router-view></router-view>
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
  }
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

</style>

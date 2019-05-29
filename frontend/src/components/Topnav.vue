<template>

    <nav>
        <!-- TUV Logo - Home Button -->
        <router-link to = '/' class = 'smallLogo'>
            <img src="../assets/logo.svg" alt="TUV Logo">
        </router-link>
    </nav>
    

</template>

<script>
export default {
    name: 'Topnav'
}
</script>

<style scoped>

nav{
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

.smallLogo{
    cursor: pointer;
    position: relative;
    z-index: 2;
    height: 100%;
    width: 65px;
    top:0;
    left:0;
    background-color: #2c3e50;
    box-sizing: border-box;
    padding-left: 5px;
    padding-top: 5px;
}

</style>


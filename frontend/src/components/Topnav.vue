<template>

    <!-- TUV Logo - Home Button -->
    <router-link to = '/' class = 'smallLogo'>
        <img src="../assets/logo.svg" alt="TUV Logo">
    </router-link>

</template>

<script>
export default {
    name: 'Topnav'
}
</script>

<style scoped>

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


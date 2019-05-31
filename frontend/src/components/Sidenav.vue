<template>

    <nav>
        <!-- Report Section Link -->
        <router-link to = '/reports'>
            <div class = 'sideNavButton'>
                <i><font-awesome-icon icon = 'file-alt'/></i>
            </div>
        </router-link>

        <!-- Verifications Section Link -->
        <router-link to = '/verifications'>
            <div class = 'sideNavButton'>
                <i><font-awesome-icon icon = 'clipboard-check'/></i>
            </div>
        </router-link>

        <!-- Environmental Conditions Section Link -->
        <router-link to = '/environmental'>
            <div class = 'sideNavButton'>
                <i><font-awesome-icon icon = 'thermometer-half'/></i>
            </div>
        </router-link>

        <!-- Open Side Nav Button -->
        <div class = 'sideNavButton openSideNav'>
            <i><font-awesome-icon icon = 'angle-right'/></i>
        </div>
    </nav>

</template>

<script>
export default {
    name: 'Sidenav'
}
</script>

<style scoped>

nav{
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

.sideNavButton{
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    border-bottom: solid 2px #2c3e50;
    width: 100%;
    height: 60px;
    color: #ececec;
    font-size: 35px;
}

.openSideNav{
    margin-top: auto;
    border-top: solid 2px #2c3e50;
}

.sideNavButton i{
    transition: transform .2s;
}

.sideNavButton i:hover{
    transform: scale(1.1);
}

</style>


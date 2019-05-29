<template>

    <nav>
        <!-- Report Section Link -->
        <router-link to = '/reports'>
            <div id = 'reportIcon' class = 'sideNavButton'>
                <font-awesome-icon icon = 'file-alt'/>
            </div>
        </router-link>

        <!-- Verifications Section Link -->
        <router-link to = '/verifications'>
            <div id = 'verificationIcon' class = 'sideNavButton'>
                <font-awesome-icon icon = 'clipboard-check'/>
            </div>
        </router-link>

        <!-- Environmental Conditions Section Link -->
        <router-link to = '/environmental'>
            <div class = 'sideNavButton'>
                <font-awesome-icon icon = 'thermometer-half'/>
            </div>
        </router-link>

        <!-- Open Side Nav Button -->
        <div class = 'sideNavButton openSideNav'>
            <font-awesome-icon icon = 'angle-right'/>
        </div>
    </nav>

</template>

<script>
export default {
    name: 'Sidenav'
}
</script>

<style scoped>

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

</style>


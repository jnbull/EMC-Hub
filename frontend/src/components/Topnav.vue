<template>

    <nav>
        <!-- TUV Logo - Home Button -->
        <router-link to = '/' class = 'smallLogo'>
            <img src="../assets/logo.svg" alt="TUV Logo">
        </router-link>
        <div class = 'searchContainer'>
            <div class = 'topNavButton'>
                <i><font-awesome-icon icon = 'search'/></i>
            </div>

            <input class = 'searchField' type="text" placeholder = 'Search...'>
        </div>
        <div class = 'pageTitle'>
            {{pageName}}
        </div>
        <div class = 'userIcon'>
            JB
        </div>
    </nav>
    

</template>

<script>
export default {
    name: 'Topnav',
    props: ['pageName'],
    
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

.searchContainer{
    display: flex;
    justify-content: center;
    align-items: center;
    margin-left: 40px;
}

.topNavButton{
    cursor: pointer;
    display: inline-block;
    color: #999;
    font-size: 20px;
    width: 100%;
    height: 100%;
    padding: 10px;
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

.userIcon{
    display: flex;
    justify-content: center;
    align-items: center;
    /* margin-left: auto; */
    margin-right: 20px;
    margin-left: 20px;
    border-radius: 50%;
    width: 50px;
    height: 50px;
    background-color: #999; 
    /* border: 2px solid whitesmoke; */
    color: whitesmoke;
    font-size: 18pt;
}

.pageTitle{
    display:flex;
    justify-content: center;
    align-items: center;
    margin-left: auto;
    border-right: 2px solid #999;
    height: 60%;
    padding: 20px;
    color: #999;
}

.searchField{
    border: none;
    font-size: 12pt;
    /* margin-left: 40px; */
}

</style>


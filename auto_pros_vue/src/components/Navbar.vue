<template>
    <nav class="navbar is-white">
      <div class="navbar-brand">
          <img src="../assets/media/autopros_logo.png" alt="Logo">
          <div class="navbar-burger burger" data-target="navMenu" :class="{ 'is-active': isHamburgerOpen }" v-on:click="openHamburgerMenu">
            <span></span>
            <span></span>
            <span></span>
          </div>
      </div>
      <div id="navMenu" class="navbar-menu" :class="{ 'is-active': isHamburgerOpen }">
        <div class="navbar-start" id="navbar-links">
          <a class="navbar-item">
            <p>Browse Categories</p>
          </a>
          <a class="navbar-item">
            <p>Blog</p>
          </a>
          <a class="navbar-item">
            <p>Write a Review</p>
          </a>
        </div>
      </div>
    </nav>
</template>

<style>
.navbar {
  width: 100%;
  height: 40px;
}
.navbar-brand {
  width:4%;
  height:100%;
  align-items : center;
}
.navbar-start {
  margin-left: 1rem;
}
.navbar-burger {
  margin-left: 10px;
}
#navbar-links{
  margin-left: 0;
}
img {
    min-width: 40px;
}
</style>
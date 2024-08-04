<template>
  <div id="app">
    <nav class="bg-gray-800 p-4">
      <div class="container mx-auto flex justify-between items-center">
        <router-link to="/" class="text-white font-bold text-xl">Age Fit App</router-link>
        <div>
          <router-link to="/login" class="text-white mr-4" v-if="!isAuthenticated">Login</router-link>
          <router-link to="/register" class="text-white mr-4" v-if="!isAuthenticated">Register</router-link>
          <router-link to="/dashboard" class="text-white mr-4" v-if="isAuthenticated">Dashboard</router-link>
          <button @click="logout" class="text-white" v-if="isAuthenticated">Logout</button>
        </div>
      </div>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      isAuthenticated: false,
    };
  },
  created() {
    this.checkAuthentication();
  },
  methods: {
    checkAuthentication() {
      this.isAuthenticated = !!localStorage.getItem('token');
    },
    logout() {
      localStorage.removeItem('token');
      this.isAuthenticated = false;
      this.$router.push('/login');
    },
  },
  watch: {
    $route() {
      this.checkAuthentication();
    },
  },
};
</script>
<template>
  <div class="max-w-md mx-auto mt-8">
    <h2 class="text-2xl font-bold mb-4">Login</h2>
    <form @submit.prevent="login" class="space-y-4">
      <div>
        <label for="username" class="block mb-1">Username</label>
        <input type="text" id="username" v-model="username" required class="w-full px-3 py-2 border rounded">
      </div>
      <div>
        <label for="password" class="block mb-1">Password</label>
        <input type="password" id="password" v-model="password" required class="w-full px-3 py-2 border rounded">
      </div>
      <button type="submit" class="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://localhost:8000/api/login/', {
          username: this.username,
          password: this.password,
        });
        console.log('Login successful', response.data);
        // Store token in localStorage or Vuex store
        // Redirect to home page or dashboard
      } catch (error) {
        console.error('Login failed', error);
      }
    },
  },
};
</script>

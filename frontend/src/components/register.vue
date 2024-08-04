<template>
  <div class="max-w-md mx-auto mt-8">
    <h2 class="text-2xl font-bold mb-4">Register</h2>
    <form @submit.prevent="register" class="space-y-4">
      <div>
        <label for="username" class="block mb-1">Username</label>
        <input type="text" id="username" v-model="username" required class="w-full px-3 py-2 border rounded">
      </div>
      <div>
        <label for="email" class="block mb-1">Email</label>
        <input type="email" id="email" v-model="email" required class="w-full px-3 py-2 border rounded">
      </div>
      <div>
        <label for="password" class="block mb-1">Password</label>
        <input type="password" id="password" v-model="password" required class="w-full px-3 py-2 border rounded">
      </div>
      <button type="submit" class="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600">Register</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
    };
  },
  methods: {
    async register() {
      try {
        const response = await axios.post('http://localhost:8000/api/register/', {
          username: this.username,
          email: this.email,
          password: this.password,
        });
        console.log('Registration successful', response.data);
        // Redirect to login page or home page
      } catch (error) {
        console.error('Registration failed', error);
      }
    },
  },
};
</script>

<template>
  <div class="container mx-auto mt-8">
    <h1 class="text-3xl font-bold mb-6">Welcome, {{ username }}!</h1>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div class="bg-white p-6 rounded shadow">
        <h2 class="text-xl font-semibold mb-4">Your Programs</h2>
        <ul v-if="programs.length" class="space-y-2">
          <li v-for="program in programs" :key="program.id" class="border-b pb-2">
            {{ program.name }}
          </li>
        </ul>
        <p v-else>You haven't created any programs yet.</p>
        <button @click="createProgram" class="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Create New Program</button>
      </div>
      <div class="bg-white p-6 rounded shadow">
        <h2 class="text-xl font-semibold mb-4">Recent Workouts</h2>
        <ul v-if="recentWorkouts.length" class="space-y-2">
          <li v-for="workout in recentWorkouts" :key="workout.id" class="border-b pb-2">
            {{ workout.date }} - {{ workout.program.name }}
          </li>
        </ul>
        <p v-else>You haven't logged any workouts yet.</p>
        <button @click="logWorkout" class="mt-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">Log New Workout</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      programs: [],
      recentWorkouts: [],
    };
  },
  async mounted() {
    await this.fetchUserData();
    await this.fetchPrograms();
    await this.fetchRecentWorkouts();
  },
  methods: {
    async fetchUserData() {
      try {
        const response = await axios.get('http://localhost:8000/api/users/me/');
        this.username = response.data.username;
      } catch (error) {
        console.error('Failed to fetch user data', error);
      }
    },
    async fetchPrograms() {
      try {
        const response = await axios.get('http://localhost:8000/api/programs/');
        this.programs = response.data;
      } catch (error) {
        console.error('Failed to fetch programs', error);
      }
    },
    async fetchRecentWorkouts() {
      try {
        const response = await axios.get('http://localhost:8000/api/workouts/');
        this.recentWorkouts = response.data.slice(0, 5); // Get the 5 most recent workouts
      } catch (error) {
        console.error('Failed to fetch recent workouts', error);
      }
    },
    createProgram() {
      // Implement program creation logic or navigation to program creation page
    },
    logWorkout() {
      // Implement workout logging logic or navigation to workout logging page
    },
  },
};
</script>

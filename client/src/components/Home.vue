<template>
    <div class="home">
        <h1>Estaciones meteorológicas</h1>
      <table>
        <thead>
          <tr>
            <th>Id</th>
            <th>Nombre</th>
            <th>Ubicación</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="station in stations" :key="station.id">
            <td>{{ station.id }}</td>
            <td>{{ station.name }}</td>
            <td>{{ station.location }}</td>
          </tr>
        </tbody>
      </table>
      <button @click="redirectToCreate">Crear estación meteorológica</button>
    </div>
  </template>


  <script>
  import axios from 'axios'
  import router from '../router/index'
  export default {
    name: 'Main', 
    data() {
      return {
        stations: []
      }
    },
    methods: {
      getStations() {
        const path = 'http://localhost:5000/'
        axios.get(path).then((response) => {
          this.stations = response.data 
        })
        .catch((error) => {
          console.log(error);
        })
      },
      redirectToCreate(){
        router.push('/create');
      }
    }, 
    created() {
      this.getStations()
    }
  }
  </script>
<style src = './Home.css'/>
  

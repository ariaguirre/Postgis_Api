<template>
    <div class="home">
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
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  export default {
    name: 'Main', 
    data() {
      return {
        stations: []  // Array para almacenar las estaciones obtenidas del servidor
      }
    },
    methods: {
      getStations() {
        const path = 'http://localhost:5000/'
        axios.get(path).then((response) => {
          this.stations = response.data // Almacenar los datos en la variable stations
        })
        .catch((error) => {
          console.log(error);
        })
      }
    }, 
    created() {
      this.getStations()
    }
  }
  </script>
  
  <style>
  .home {
    text-align: center;
    margin-top: 20px;
  }
  </style>
  
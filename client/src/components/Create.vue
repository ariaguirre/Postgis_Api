<template>
    <div>

        <div class="form-container">
            <h2>Crear nueva estación meteorológica</h2>
            <form @submit.prevent="submitForm">
                <div class="form-group">
                    <label for="name">Nombre:</label>
                    <input type="text" id="name" v-model="station.name" required>
                </div>
                
                <div class="form-group">
                    <label for="latitude">Latitud:</label>
                    <input type="text" id="latitude" v-model="station.latitude" required>
                </div>
                
                <div class="form-group">
                    <label for="longitude">Longitud:</label>
                    <input type="text" id="longitude" v-model="station.longitude" required>
                </div>
                
                <button type="submit">Crear estación</button>
            </form>
        </div>
        <button @click="redirect">Volver al inicio</button>
    </div>
    </template>
  
  <script>
  import axios from 'axios';
  import Swal from 'sweetalert2'
  import router from '../router';
  
  export default {
    data() {
      return {
        station: {
          name: '',
          latitude: '',
          longitude: ''
        }
      };
    },
    methods: {
      submitForm() {
        const path = 'http://localhost:5000/add'; 
        axios
          .post(path, this.station)
          .then(response => {
            console.log(response.data);
            Swal.fire({
                title: 'Created!',
                text: 'Station created succesfully!',
                icon: 'success',
                confirmButtonText: 'Cool'
                })
          })
          .catch(error => {
            console.error(error.response.data.message);
            Swal.fire({
                title: 'Error!',
                text: 'There was an error creating the new station, try again!',
                icon: 'error',
                confirmButtonText: 'Cool'
                })
          });
      },
      redirect(){
              router.push('/home');
          },
    }, 
  };
  </script>


<!-- 
<button @click="redirect">Volver a inicio</button>

  <script>
  import router from '../router/index'

  export default {
    methods:{
        redirect(){
            router.push('/home');
        },
    },
  };
  </script> -->
  <style src="./Create.css" />
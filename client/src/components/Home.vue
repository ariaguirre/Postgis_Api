<template>
    <div class="home">
      <p>{{ message }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  export default {
    name: 'Main', 
    data () {
        return{
            message: 'New message from VueJS.'
        }
    },
    methods: {
        getMessage() {
            const path = 'http://localhost:5000/message'
            axios.get(path).then((response) => {
                this.message = response.data
            })
            .catch((error) => {
                console.log(error);
            })
        }
    }, 
    created(){
        this.getMessage()
    }
  }
  </script>
  
  <style>
  .home {
    text-align: center;
    margin-top: 20px;
  }
  </style>
  
<template>
  <div id="app">
    <h2>
      <Header @toggle-zip-code="toggleZipCode" title = "Bond" :showZipCode="showZipCode" />
    </h2>
  </div>
  <InsertZip @add-zip="addZip"/>

  <Slider />
  <AddgoogleMap/>
</template>

<script>
import AddGoogleMap from './components/AddGoogleMap'
import Header from './components/Header'
import Slider from './components/Slider'
import InsertZip from './components/InsertZip'

export default {
  name: 'App',
  components: {
    Header,
    Slider,
    AddGoogleMap,
    InsertZip,
  },
  methods: {
    toggleZipCode() {
      this.showZipCode=!this.showZipCode
    },
    async addZip() {
      const res = await fetch('',{
        method: 'POST',
        headers: {
          'Content-type': 'application/json',
        },
      }).then()
    }
  }
}
</script>

<style>
@import url('https://fonts.goggleapis.com/css2?family=Poppins:wght@300;400&display=swap');

*{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  text-align: center;
}

h2 {
  text-align: right;
  justify-content: space-between;
  color: rgb(11, 50, 94);
}
Header {
  background-color: rgb(129, 187, 253);
  text-align: right;
  align-items: center;
  justify-content: space-between;
  
}
Slider {
  align-items: center;
}
body {
  font-family: 'Poppins', sans-serif;
  background-color: rgb(221, 243, 255);
  text-align: center; 
  justify-content: space-between;
}

.container {
  max-width: 500px;
  margin: 30px auto;
  overflow: auto;
  min-height: 300px;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
}

.btn {
  display: inline-block;
  background: #000;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}

.btn:focus {
  outline: none;
}

.btn:active {
  transform: scale(0.98);
}

.btn-block {
  display: block;
  width: 100%
}
</style>

<template>
<div>
    <transition-group name='fade' tag='div'>
      <div v-for="i in [currentIndex]" :key='i'>
        <img :src="currentImg" />
      </div>
    </transition-group>
    <a class="prev" @click="prev" href='#'>&#10094;</a>
  <a class="next" @click="next" href='#'>&#10095;</a>
  </div>
</template>

<script>
export default {
  name: 'Slider',
  data() {
    return {
      images: [
        'https://www.mrshappyhomemaker.com/wp-content/uploads/blogger/-mK0a1k7U-b4/UA3s8vrmoMI/AAAAAAAAFJg/i0SqQJqIuLQ/s1600/meadowlarkdairy.jpg',
        'https://img.restaurantguru.com/r8ef-exterior-Gay-90s.jpg',
        'https://visittrivalley.com/wp-content/uploads/2017/09/Striz-Pleasanton-store-med.jpg',
        'https://www.eastbaytimes.com/wp-content/uploads/2017/06/sjm-l-dining-0615-01.jpg?w=620',
        'https://patch.com/img/cdn/users/2833480/2012/12/raw/e22dff5ad909cc07ea3d453e6e9e0ed8.jpg'
        ],
      timer: null,
      currentIndex: 0,
    }
  },
  
    mounted: function() {
      this.startSlide();
    },
  
    methods: {
      startSlide: function() {
        this.timer = setInterval(this.next, 5000);
      },
  
  
      next: function() {
        this.currentIndex += 1
      },
      prev: function() {
        this.currentIndex -= 1
      }
    },
  
    computed: {
      currentImg: function() {
        return this.images[Math.abs(this.currentIndex) % this.images.length];
      }
    }
  
}
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: all 0.9s ease;
  overflow: hidden;
  visibility: visible;
  position: absolute;
  width:100%;
  opacity: 1;
}
.fade-enter,
.fade-leave-to {
  visibility: hidden;
  width:100%;
  opacity: 0;
}
img {
height:400px;
width:66%;
margin-top: 30px;
  }
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 40%;
  width: auto;
  padding: 16px;
  color: rgb(0, 0, 0);
  font-weight: bold;
  font-size: 18px;
  transition: 0.7s ease;
  border-radius: 0 4px 4px 0;
  text-decoration: none;
  user-select: none;
  margin-top: 160px;
}
/* Position the "next button" to the right */
.next {
  right: 0;
}
.prev {
  left: 0;
}
/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(213, 213, 213, 0.9);
}
</style>
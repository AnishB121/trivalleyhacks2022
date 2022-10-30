<template>
    <header>
        <h2>{{ title }}</h2>
        <Personal :text= 'Personalize' :color= 'B29EED'/>
    </header>
</template>

<script>
import Personal from './Personal'
    export default {
        name: 'Header',
        props: {
            title: String,
        },
        components: {
            Personal
        }
    }
</script>

<style scoped>
    header {
        display: flex;
        justify-content: space-between;
        align-items: right;
        margin-bottom: 10px;
        text-align: right;
    }
    h1 {
        text-align: right;
        justify-content: space-between;
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
    .btn:active {
        transform: scale(0.9);
    }
    .btn-block {
        display: block;
        width: 100%
    }
    button hover {
        transform: scale(0.98);
    }
</style>
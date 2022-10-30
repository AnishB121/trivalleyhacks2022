<template>
    <header>
        <h2>{{ title }}</h2>
        <Button @btn-click="$emit('toggle-zip-code')"
         :text="showZipCode? 'Close' : 'Location'"
         :color="showZipCode? '#cc0000' : 'B29EED'"/>
    </header>
</template>

<script>
import Button from './Button'
    export default {
        name: 'Header',
        props: {
            title: String,
            showZipCode: Boolean,
        },
        components: {
            Button
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
        background: rgb(69, 40, 101);
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
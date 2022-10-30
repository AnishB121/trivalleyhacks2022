<template>
    <button @click="onClick()" :style="{background: color}" class="btn">{{text}}</button>
</template>

<script>
export default {
    name: 'Button',
    props: {
        text: String,
        color: String,
    },
    methods: {
        onClick() {
            console.log("test")
            this.$emit('btn-click')
        }
    }
}
</script>

<style scoped>

</style>

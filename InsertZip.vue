<template>
    <form @submit="onSubmit" class="add-form">
        <div class="form-control">
            <input type="text" v-model="text" name="text" placeholder="Insert Zip Code" />
        </div>
        <div class="text-center">
            <input type="submit" value="Save zip code" class="btn btn-block" />
        </div>
    </form>
</template>

<script>
export default{
    name: 'InsertZip',
    data() {
        return {
            text: '',
        }
    },
    methods: {
        onSubmit(e) {
            e.preventDefault()
            if(!this.text) {
                alert('Please add your zip code!')
                return
            }
        }
    }
}
</script>

<style scoped>
.add-form {
    margin-bottom: 40px;
}

.form-control {
    margin: 20px 0;
}

.form-control label {
    display: block;
}

.form-control input {
    width: 20%;
    height: 40px;
    margin: 5px;
    padding: 3px 7px;
    font-size: 17px;
}

.form-control-check {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.form-control-check label {
    flex: 1;
}

.form-control-check input {
    flex: 2;
    height: 20px;
}
.btn {
    width: 190px;
    align-items: center;
    background-color: rgb(63, 35, 107);
    margin-left: 540px;
}
</style>
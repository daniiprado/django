<template>
    <div class="row mt-5">
        <div class="col-md-4 mb-3" v-for="product in products">
            <div class="card">
                <img class="card-img-top" height="180" :src="`/storage/${product.fields.image}`" alt="Card image cap" />
                <div class="card-body">
                <h5 class="card-title" v-text="product.fields.name"></h5>
                    <small class="text-muted" v-text="product.fields.category"></small>
                    <p class="card-text" v-text="product.fields.description"></p>
                <a href="javascript:;" class="btn btn-primary">$ {{ product.fields.price }}</a>
                <a :href="`/products/${product.pk}`" class="btn btn-primary"> Ver </a>
              </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Products",
        data: () => {
          return {
              products: []
          }
        },
        mounted: function () {
            this.getProducts();
        },
        methods: {
            getProducts() {
                axios.get('/products/json')
                    .then((response) => {
                        this.products = response.data
                    })
                    .catch((error) => {
                        console.log(error)
                    })
            },
        }
    }
</script>

<style scoped>

</style>
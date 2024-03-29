
/**
 * First we will load all of this project's JavaScript dependencies which
 * includes Vue and other libraries. It is a great starting point when
 * building robust, powerful web applications using Vue and Laravel.
 */

require('./bootstrap');

import Vue from "vue"
import { library } from '@fortawesome/fontawesome-svg-core'
import { faCoffee } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import VueDummy from "vue-dummy"
library.add(faCoffee)
Vue.use(VueDummy)
/**
 * Next, we will create a fresh Vue application instance and attach it to
 * the page. Then, you may begin adding components to this application
 * or customize the JavaScript scaffolding to fit your unique needs.
 */
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.component('example-component', require('./components/ExampleComponent.vue').default);
Vue.component('vue-nav-bar', require('./components/NavBar.vue').default);
Vue.component('vue-footer', require('./components/Footer.vue').default);
Vue.component('products', require('./components/Products.vue').default);

const app = new Vue({
    el: '#app'
});
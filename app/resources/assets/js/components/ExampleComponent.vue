<template>
    <main role="main" class="container">
        <h1 class="mt-lg-5">Sticky footer with fixed navbar</h1>
        <p class="lead">Pin a fixed-height footer to the bottom of the viewport in desktop browsers with this custom HTML and CSS. A fixed navbar has been added with <code>padding-top: 60px;</code> on the <code>body &gt; .container</code>.</p>
        <p>Back to <a href="../sticky-footer">the default sticky footer</a> minus the navbar.</p>
        <div class="row justify-content-center mt-xl-5">
            <div class="col-md-8">
                <div class="card card-default">
                    <div class="card-header">Example Component</div>
                    <div class="card-body">
                        <font-awesome-icon icon="coffee" />
                        I'm an example component.
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
    export default {
        mounted() {
            console.log('Component mounted.')
        }
    }
</script>

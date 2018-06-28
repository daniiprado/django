/*********************************
 * Environment and imports
 *********************************/
const env = process.env.NODE_ENV || 'development';
const autoprefixer = require('autoprefixer');
const webpack = require('webpack');
const path = require('path');
const { VueLoaderPlugin } = require('vue-loader');
const UglifyJsPlugin = require("uglifyjs-webpack-plugin");
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const ExtractTextPlugin = require("extract-text-webpack-plugin");

console.log(process.env.NODE_ENV);
console.log(env);

/***************
 * Entry
 ***************/

const entry = [
    "./resources/assets/sass/app.scss",
    "./resources/assets/js/app.js",
    "./resources/assets/css/styles.css"
];

/***************
 * Output
 ***************/

const output = {
    filename: "[name].bundle.js",
    chunkFilename: '[name].bundle.js',
    publicPath: '/js/',
    path: path.resolve(__dirname, './public/js/'),
    pathinfo: false
};

if (env === "production") {
    output.filename = "[name].bundle.min.js";
    output.chunkFilename = "[name].bundle.min.js";
    output.pathinfo = false;
}

/***************
 * Modules
 ***************/

const _module = {
    rules: [
        {
            test: /\.bundle\.js$/,
            use: 'bundle-loader'
        },
        {
            test: /\.vue$/,
            loader: 'vue-loader'
        },
        {
            test: /\.js$/,
            loader: 'babel-loader',
            exclude: /node_modules/
        },
        {
            test: /\.(sa|sc|c)ss$/,
            use: ExtractTextPlugin.extract({
                fallback: "style-loader",
                use: [
                    "css-loader",
                    "postcss-loader",
                    "sass-loader"
                ]
            })
        },
        {
            test: /\.(woff|woff2|eot|ttf|otf)$/,
            loader: [
                'file-loader'
            ]
        },
        {
            test: /\.(png|jpg|gif|svg)$/,
            loader: 'file-loader',
            options: {
                name: '[name].[ext]?[hash]'
            }
        }
    ]
};

/***************
 * Optimization
 ***************/

const optimization = {
    splitChunks: {
        cacheGroups: {
            styles: {
                name: 'styles',
                test: /\.css$/,
                chunks: 'all',
                enforce: true
            },
            common: {
                test: /[\\/]node_modules[\\/]/,
                name: "vendors",
                chunks: 'all',
                enforce: true
            }
        }
    },
    minimizer: [
        new UglifyJsPlugin({
            cache: true,
            parallel: true,
            sourceMap: true // set to true if you want JS source maps
        }),
        new OptimizeCSSAssetsPlugin({})
    ]
};


/***************
 * Plugins
 ***************/

const plugins = [
    new VueLoaderPlugin(),
    new ExtractTextPlugin({
        filename: env === "production" ? "../css/[name].bundle.min.css" : "../css/[name].bundle.css",
        disable: false,
        allChunks: true
    }),
    new webpack.LoaderOptionsPlugin({
        options: {
            postcss: [
                autoprefixer()
            ]
        },
        minimize: env === "production",
    }),
    new webpack.DefinePlugin({
        'process.env': {
            NODE_ENV: JSON.stringify(process.env.NODE_ENV)
        }
    })
];
/***************
 * Resolve
 ***************/

const resolve = {
    extensions: [".ts", ".js"],
    modules: [
        "node_modules"
    ],
    alias: {
        vue: 'vue/dist/vue.js'
    }
};

/***************
 * Exports
 ***************/

module.exports = {
    entry: entry,
    output: output,
    resolve: resolve,
    mode: env,
    module: _module,
    optimization: optimization,
    plugins: plugins
};
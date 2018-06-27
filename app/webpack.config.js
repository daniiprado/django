let path = require('path')
let webpack = require('webpack')
const { VueLoaderPlugin } = require('vue-loader')
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const devMode = process.env.NODE_ENV !== 'production'

module.exports = {
  mode: 'production',
  // entry: './static/js/app.js',
  entry: {
    'app': [
      './resources/assets/js/app.js',
      './resources/assets/sass/app.scss',
    ]
  },
  output: {
    path: path.resolve(__dirname, './public'),
    publicPath: '/public/',
    filename: 'scripts.bundle.js'
  },
  module: {
    rules: [
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
        use: [
           {
            loader: MiniCssExtractPlugin.loader,
            options: {
                // you can specify a publicPath here
                // by default it use publicPath in webpackOptions.output
                publicPath: '/public/'
              },
           },
          'css-loader',
          'sass-loader',
        ]
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
  },
  resolve: {
    modules: [
      "node_modules"
    ],
    alias: {
      vue: 'vue/dist/vue.js'
    }
  },
  plugins: [
    // make sure to include the plugin for the magic
    new VueLoaderPlugin(),
    new MiniCssExtractPlugin({
      // Options similar to the same options in webpackOptions.output
      // both options are optional
      filename: "styles.bundle.css",
      chunkFilename: "[id].css"
    })
  ],
  performance: {
    hints: false
  },

  devtool: '#eval-source-map'
}

if (process.env.NODE_ENV === 'production')
{
  module.exports.devtool = '#source-map'

  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      sourceMap: true,
      compress: {
        warnings: false
      }
    }),
    new webpack.LoaderOptionsPlugin({
      minimize: true
    })
  ])
}

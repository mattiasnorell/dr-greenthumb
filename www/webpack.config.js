var path = require("path");
const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const htmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: "./src/main.ts",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "bundle.js",
    publicPath: ""
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        loader: 'ts-loader',
				include: [ path.join(__dirname, 'src') ]
      },
      {
        test: /\.(html)$/,
        use: {
          loader: 'html-loader',
          options: {
            attrs: [ ':data-src' ]
          }
        }
      },
      {
        test: /\.scss$/,
        use: ExtractTextPlugin.extract(
          {
            fallback: "style-loader",
            use: [
              {
                loader: "css-loader"
              },
              {
                loader: "sass-loader"
              }    
            ]
          }
        ),
        include: [ path.join(__dirname, 'src/style') ]
      }
    ]
  },
  resolve: {
      extensions: [".tsx", ".ts", ".js"],
      modules: [ path.resolve(__dirname, 'src'), 'node_modules' ],
  },
  plugins: [ 
    new ExtractTextPlugin({filename: 'style.css'}),
    new htmlWebpackPlugin({
      template: './index.html',
      inject: true,
      filename: 'index.html',
      title: 'Dr Greenthumb',
      chunksSortMode: 'none'
    }),
  ]
};
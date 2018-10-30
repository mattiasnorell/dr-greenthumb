/* === dont forget to import scss to main.js file === */
/* ===> import './main.scss'; <=== */

var path = require("path");
const ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
  entry: "./src/main.ts",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "bundle.js",
    publicPath: "/dist"
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        loader: 'ts-loader',
        exclude: /node_modules/,
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
        )
      }
    ]
  },
  resolve: {
      extensions: [".tsx", ".ts", ".js"]
  },plugins: [ 
    new ExtractTextPlugin({filename: 'style.css'})
  ]
};
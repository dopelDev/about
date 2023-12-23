const { VueLoaderPlugin } = require('vue-loader');
const path = require('path');

module.exports = {
  entry: './about/static/js/app', // Punto de entrada de tu aplicación
  output: {
    path: path.resolve(__dirname, './about/static/js/'), // Directorio de salida
    filename: 'bundle.js' // Nombre del archivo empaquetado
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      // Aquí puedes añadir más reglas para otros tipos de archivos
    ]
  },
  plugins: [
    // Asegúrate de incluir el plugin de Vue Loader
    new VueLoaderPlugin()
  ]
};


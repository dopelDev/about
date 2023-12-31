const { VueLoaderPlugin } = require('vue-loader');
const path = require('path');

module.exports = {
  entry: './about/static/js/app.js', // Punto de entrada de tu aplicación
  output: {
    path: path.resolve(__dirname, './about/static/'), // Directorio de salida
    filename: './js/app.bundle.js' // Nombre del archivo empaquetado
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
  ],
	resolve: {
		extensions: ['.js', '.vue', '.json'],
		alias: {
			'vue$': './node_modules/vue/dist/vue.esm.js',
};


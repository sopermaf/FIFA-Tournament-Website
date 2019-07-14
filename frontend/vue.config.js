const BundleTracker = require("webpack-bundle-tracker");

const pages = {
    'fifa_app': {
        entry: './src/main.js',
        chunks: ['chunk-vendors']
    },
    'data_app': {
        entry: './src/dataEntry.js',
        chunks: ['chunk-vendors']
    },
    'fixtures_app': {
        entry: './src/fixtures.js',
        chunks: ['chunk-vendors']
    }
}

module.exports = {
    baseUrl: "http://127.0.0.1:8080/",
    outputDir: './dist/',
    pages: pages,

    chainWebpack: config => {
        
        config.optimization
            .splitChunks({
                cacheGroups: {
                    vendor: {
                        test: /[\\/]node_modules[\\/]/,
                        name: "chunk-vendors",
                        chunks: "all",
                        priority: 1
                    },
                },
            });
        
        // avoid creating unused pages as Django backend
        Object.keys(pages).forEach(page => {
            config.plugins.delete(`html-${page}`);
            config.plugins.delete(`preload-${page}`);
            config.plugins.delete(`prefetch-${page}`);
        })

        config
            .plugin('BundleTracker')
            .use(BundleTracker, [{filename: '../frontend/webpack-stats.json'}])

        config.resolve.alias
            .set('__STATIC__', 'static')

        config.devServer
            .public('http://0.0.0.0:8080')
            .host('0.0.0.0')
            .port(8080)
            .hotOnly(true)
            .watchOptions({poll: 1000})
            .https(false)
            .headers({"Access-Control-Allow-Origin": ["\*"]})
            }
        };
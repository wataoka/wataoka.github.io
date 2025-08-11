module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
    fontFamiliy: {
        body: [
            'ヒラギノ角ゴ StdN',
            'Hiragino Kaku Gothic StdN',
            'ヒラギノ角ゴシック',
            'Hiragino Sans',
            'ＭＳ ゴシック',
            'sans-serif'
        ]
    },
    listStyleType: {
      none: 'none',
      square: 'square',
      roman: 'upper-roman',
    }
  },
  plugins: [],
}
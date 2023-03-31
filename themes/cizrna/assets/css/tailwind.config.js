module.exports = {
  darkMode: 'class',
  content: [
    "./themes/**/layouts/**/*.html",
    "./content/**/layouts/**/*.html",
    "./layouts/**/*.html",
    "./content/**/*.html"
  ],
  theme: {
    extend: {
	  backgroundImage: {
        'main': "url('/falafel-logo-screen-2v.png')"
      },
	  backgroundSize: {
        'auto': 'auto',
        'cover': 'cover',
      },
	  fontFamily: {
		  'sans': ['ui-sans-serif', 'system-ui'],
		  'serif': ['Merriweather', 'ui-serif'],
		  'castoro': ['Castoro', 'ui-serif']
	  }
	},
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
    require('@tailwindcss/line-clamp'),
  ]
}

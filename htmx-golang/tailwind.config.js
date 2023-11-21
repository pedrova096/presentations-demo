/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.tmpl',
    './templates/*.tmpl',
  ],
  theme: {
    extend: {},
  },
  plugins: [
  ],
  safelist: [
    "bg-rose-500", "bg-yellow-500", "bg-cyan-500", "bg-indigo-500", "bg-violet-500", "bg-teal-500"
  ]
}


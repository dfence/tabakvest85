/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.html",
    "./pages/**/*.html"
  ],
  theme: {
    extend: {
      colors: {
        primary: '#8B6F47',
        secondary: '#D4A574',
        accent: '#2C3E50',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      }
    },
  },
  plugins: [],
}

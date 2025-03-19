/** @type {import('tailwindcss').Config} */
const { colors: defaultColors } = require('tailwindcss/defaultTheme');

module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        gray: {
          700: '#4B5563', // Main background color
          800: '#1F2937', // Navbar and other components background color
          900: '#111827', // Deep shadows background color
        },
        custom: {
          main: '#9CA3AF', // Main test color
          red: {
            400: '#F87171', // Button color for red
          },
          green: {
            400: '#34D399', // Button color for green
          },
          blue: {
            400: '#60A5FA', // Button color for blue
          },
          yellow: {
            400: '#FBBF24', // Button color for yellow
          },
          pink: {
            400: '#F472B6', // Button color for pink
          },
          orange: {
            500: '#FB923C', // Logo color
          },
        },
      },
    },
  },
  plugins: [],
};



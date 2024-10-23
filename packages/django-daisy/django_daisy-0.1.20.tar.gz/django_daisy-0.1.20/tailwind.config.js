/** @type {import('tailwindcss').Config} */

module.exports = {
    content: [],
    theme: {
        extend: {
            fontFamily: {
                vazir: ['Vazir', 'sans-serif'],   // Define the Vazir font
                roboto: ['Cantarell', 'sans-serif'], // Define the Roboto font
            },
            animation: {
                'bounce-once': 'bounce 1s ease-in-out 1',
            },
        },
    },

    daisyui: {
        themes: [
            "light",
            "dark",
            "dracula",
            "dim",
            "autumn",
            "lemonade",
        ],  // Include themes from DaisyUI
        darkTheme: "dark", // name of one of the included themes for dark mode
        base: true, // applies background color and foreground color for root element by default
        styled: true, // include daisyUI colors and design decisions for all components
        utils: true, // adds responsive and modifier utility classes
    },
    safelist: [
        "flex",
        // List all potential classes that you expect to be dynamically generated
    ],

    plugins: [
        require('daisyui'),  // DaisyUI for additional UI components
    ],
}

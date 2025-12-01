// eslint.config.js
import js from "@eslint/js";
import reactHooks from "eslint-plugin-react-hooks";
import reactRefresh from "eslint-plugin-react-refresh";
import importPlugin from "eslint-plugin-import";
import globals from "globals";
import { defineConfig } from "eslint/config";

export default defineConfig([
  // --- 1) Ignore files globally ---
  {
    ignores: ["vite.config.js"],
  },

  // --- 2) Main JS/JSX config ---
  {
    files: ["**/*.{js,jsx}"],

    settings: {
      "import/resolver": {
        node: {
          extensions: [".js", ".jsx"],
        },
        alias: {
          map: [["@", "./src"]],
          extensions: [".js", ".jsx"],
        },
      },
    },

    plugins: {
      import: importPlugin,
    },

    extends: [
      js.configs.recommended,
      reactHooks.configs.flat.recommended,
      reactRefresh.configs.vite,
    ],

    languageOptions: {
      ecmaVersion: "latest",
      globals: globals.browser,
      parserOptions: {
        ecmaFeatures: { jsx: true },
        sourceType: "module",
      },
    },

    rules: {
      "import/no-unresolved": "error",
      "import/named": "error",
      "import/default": "error",

      "import/namespace": "off",

      "no-unused-vars": "warn",
    },
  },
]);

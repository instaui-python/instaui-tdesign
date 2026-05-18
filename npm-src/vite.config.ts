import vue from "@vitejs/plugin-vue";
import * as path from "path";
import { defineConfig } from "vite";

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],

  define: {
    "process.env": {},
  },

  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src"),
    },
  },

  base: "./",

  build: {
    sourcemap: false,
    lib: {
      entry: path.resolve(__dirname, "src/main.ts"),
      fileName: "instaui-tdesign",
    },
    rollupOptions: {
      external: [
        "vue",
        "instaui",
        "tdesign-vue-next",
        "tdesign-vue-next/es/config-provider/hooks/useConfig",
      ],
      output: [
        {
          format: "es",
        },
      ],
    },
    outDir: "dist/instaui-dist",
  },
});

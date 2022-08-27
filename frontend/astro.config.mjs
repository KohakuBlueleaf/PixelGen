import { defineConfig } from 'astro/config';
import compress from "astro-compress";
import { viteCommonjs } from '@originjs/vite-plugin-commonjs';

import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'

import vue from "@astrojs/vue";

// https://astro.build/config
export default defineConfig({
  vite: {
    plugins: [
      viteCommonjs(),
      AutoImport({
        resolvers: [ElementPlusResolver()],
      }),
      Components({
        resolvers: [ElementPlusResolver()],
      }),
    ],
    build: {
      commonjsOptions: {
        transformMixedEsModules: true
      }
    },
    ssr: {
      noExternal: ['element-plus']
    }
  },
  integrations: [
    compress(), 
    vue()
  ],
});
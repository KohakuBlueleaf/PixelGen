import { defineConfig } from 'astro/config';

import { viteCommonjs } from '@originjs/vite-plugin-commonjs';
import viteCompression from 'vite-plugin-compression';

import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'

import vue from "@astrojs/vue";
import compress from "astro-compress";
import sitemap from '@astrojs/sitemap';
import robotsTxt from 'astro-robots-txt';


// https://astro.build/config
export default defineConfig({
  vite: {
    plugins: [
      viteCommonjs(),
      viteCompression(),
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
  site: 'https://pixelgen.kblueleaf.net',
  integrations: [
    vue(),
    compress(),
    sitemap(),
    robotsTxt()
  ],
});
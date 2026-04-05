// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from "@tailwindcss/vite";
import icon from 'astro-icon';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import remarkDirective from 'remark-directive';
import rehypeComponents from "rehype-components";

import { AdmonitionComponent } from "./src/plugins/rehype-component-admonition.mjs";
import { parseDirectiveNode } from "./src/plugins/remark-directive-rehype.js";
import { MusicCardComponent } from "./src/plugins/rehype-component-music-card.mjs";
import { GithubCardComponent } from './src/plugins/rehype-component-github-card.mjs';
import { QuoteComponent } from "./src/plugins/rehype-component-quote.mjs"
import { customFigurePlugin } from "./src/plugins/rehype-figure-plugin.mjs";
import { remarkCombined } from './src/plugins/remark-combined.mjs';
import { remarkTypst } from './src/plugins/remark-typst.mjs';
import { remarkReadingTime } from './src/plugins/remark-reading-time.mjs';

import svelte from "@astrojs/svelte";

/**
 * Wrap admonition renderer with explicit JS doc types to satisfy @ts-check.
 * @param {any} x
 * @param {any} y
 * @param {"note" | "tip" | "important" | "caution" | "warning"} kind
 */
const renderAdmonition = (x, y, kind) => AdmonitionComponent(x, y, kind);

/** @type {(x: any, y: any) => any} */
const noteAdmonition = (x, y) => renderAdmonition(x, y, "note");
/** @type {(x: any, y: any) => any} */
const tipAdmonition = (x, y) => renderAdmonition(x, y, "tip");
/** @type {(x: any, y: any) => any} */
const importantAdmonition = (x, y) => renderAdmonition(x, y, "important");
/** @type {(x: any, y: any) => any} */
const cautionAdmonition = (x, y) => renderAdmonition(x, y, "caution");
/** @type {(x: any, y: any) => any} */
const warningAdmonition = (x, y) => renderAdmonition(x, y, "warning");


// https://astro.build/config
export default defineConfig({
  site: 'https://tooru283.github.io', // GitHub Pages 域名
  base: '/asakura-blog', // GitHub 仓库名
  i18n: {
    locales: ['zh-cn', 'en'],
    defaultLocale: 'zh-cn',
    routing: {
      prefixDefaultLocale: false,
      redirectToDefaultLocale: false
    }
  },
  integrations: [icon({
    include: {
      "fa6-brands": ["*"],
      "fa6-solid": ["*"],
      "simple-icons": ["*"],
      "vscode-icons": ["*"],
      "material-symbols": ["*"]
    }
  }), svelte()],
  markdown: {
    shikiConfig: {
      theme: 'one-dark-pro', // code theme
      // theme: 'github-dark',
      wrap: false
    },
    remarkPlugins: [
      remarkMath,
      remarkReadingTime,
      remarkDirective,
      remarkTypst,
      parseDirectiveNode,
      remarkCombined
    ],
    rehypePlugins: [
      rehypeKatex,
      customFigurePlugin,
      [
        rehypeComponents,
        {
          components: {
            github: GithubCardComponent,
            music: MusicCardComponent,
            quote: QuoteComponent,
            note: noteAdmonition,
            tip: tipAdmonition,
            important: importantAdmonition,
            caution: cautionAdmonition,
            warning: warningAdmonition,
          },
        },
      ],
    ]
  },
  vite: {
    // @ts-expect-error Astro currently types Vite 6 while @tailwindcss/vite ships Vite 7 types.
    plugins: [tailwindcss()]
  }
});
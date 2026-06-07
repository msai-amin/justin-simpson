// @ts-check
import { defineConfig } from 'astro/config';

// Deployed to GitHub Pages as a project site:
//   https://msai-amin.github.io/justin-simpson/
// If you later point a custom domain at the site (served from the root),
// change `base` to '/' and update `site` accordingly, then redeploy.
// https://astro.build/config
export default defineConfig({
  site: 'https://msai-amin.github.io',
  base: '/justin-simpson',
});

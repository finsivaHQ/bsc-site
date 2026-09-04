import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://brasizechecker.com',
  trailingSlash: 'never',
  integrations: [
    sitemap({
      filter: (page) => 
        !page.includes('/404') && 
        !page.includes('/500') &&
        !page.includes('/rss.xml')
    })
  ],
  redirects: {
    '/blog/accurate-bra-size-calculator-inches': { status: 301, destination: '/how-to-measure' },
    '/blog/international-bra-size-conversion-chart': { status: 301, destination: '/bra-size-converter' },
    '/blog/how-to-measure-bra-size-at-home': { status: 301, destination: '/how-to-measure' },
    '/blog/what-cup-size-am-i-calculator': { status: 301, destination: '/bra-size-chart' },
    '/blog/victoria-secret-bra-size-calculator-comparison': { status: 301, destination: '/guides/why-bra-sizes-vary-between-brands' },
    '/blog/marks-and-spencer-bra-size-calculator-differences': { status: 301, destination: '/uk-bra-size-guide' },
    '/blog/what-size-bra-should-i-wear-calculator': { status: 301, destination: '/how-to-measure' },
    '/blog/indian-bra-size-calculator-zivame-clovia': { status: 301, destination: '/blog/indian-bra-size-chart-conversions-us-uk-eu-au' },
    '/blog/how-to-know-if-your-bra-size-calculator-is-accurate': { status: 301, destination: '/blog/are-bra-size-calculators-accurate' },
    '/blog/teens-first-bra-size-calculator': { status: 301, destination: '/how-to-measure' },
    '/blog/bra-size-calculator-without-measurements': { status: 301, destination: '/blog/are-bra-size-calculators-accurate' },
    '/blog/uk-nhs-bra-size-calculator-standards': { status: 301, destination: '/uk-bra-size-guide' },
    '/blog/bust-size-to-bra-size-calculator': { status: 301, destination: '/methodology' },
    '/blog/bra-size-calculator-canada-australia-new-zealand': { status: 301, destination: '/blog/canada-bra-size-calculator-guide' },
    '/blog/skims-savage-x-fenty-bra-size-calculator': { status: 301, destination: '/guides/why-bra-sizes-vary-between-brands' },
    '/blog/bra-size-calculator-for-small-busts': { status: 301, destination: '/how-to-measure' },
    '/blog/bra-size-chart-xl-xxl-sml': { status: 301, destination: '/bra-size-chart' },
    '/blog/canada-bra-size-chart-conversion-guide': { status: 301, destination: '/blog/canada-bra-size-calculator-guide' },
    '/blog/canada-bra-size-profiles-band-cup-guide': { status: 301, destination: '/blog/canada-bra-size-calculator-guide' },
    '/blog/canadian-bra-brands-sizing-guide': { status: 301, destination: '/blog/canada-bra-size-calculator-guide' },
    '/blog/bras-for-large-busts-canada-guide': { status: 301, destination: '/blog/canada-bra-size-calculator-guide' },
    '/blog/plus-size-bras-canada-fit-guide': { status: 301, destination: '/blog/canada-bra-size-calculator-guide' },
    '/blog/small-bust-petite-bras-canada-guide': { status: 301, destination: '/blog/canada-bra-size-calculator-guide' },
    '/blog/how-to-measure-bra-size-india-inches-cm': { status: 301, destination: '/blog/indian-bra-size-chart-conversions-us-uk-eu-au' },
    '/blog/jockey-zivame-enamor-clovia-bra-size-guide-india': { status: 301, destination: '/blog/indian-bra-size-chart-conversions-us-uk-eu-au' },
    '/blog/maternity-sports-first-bra-size-guide-india': { status: 301, destination: '/blog/indian-bra-size-chart-conversions-us-uk-eu-au' },
    '/blog/fuller-bust-small-ribcage-bra-calculator-australia': { status: 301, destination: '/blog/best-bra-size-calculator-australia-accuracy-guide' },
    '/blog/kmart-bra-size-calculator-australia-brand-guide': { status: 301, destination: '/blog/best-bra-size-calculator-australia-accuracy-guide' },
    '/blog/how-to-measure-bra-size-at-home-guide': { status: 301, destination: '/how-to-measure' },
    '/blog/how-to-measure-bra-size-determine-calculate-find-your-fit': { status: 301, destination: '/how-to-measure' },
    '/blog/ultimate-bra-size-calculator-measurement-guide': { status: 301, destination: '/how-to-measure' },
    '/blog/how-to-estimate-bra-cup-size-from-photo-visual-guide': { status: 301, destination: '/blog/are-bra-size-calculators-accurate' },
    '/blog/international-bra-size-differences-conversion-guide': { status: 301, destination: '/bra-size-converter' },
    '/blog/how-to-read-bra-size-charts-conversions': { status: 301, destination: '/bra-size-chart' },
    '/blog/popular-bra-sizes-explained-34b-32b-34c-36c-double-d': { status: 301, destination: '/bra-size-chart' },
    '/blog/what-is-the-biggest-and-smallest-bra-size-world-records-guide': { status: 301, destination: '/bra-size-chart' },
    '/blog/bra-sizes-compared-small-medium-big-celebrities': { status: 301, destination: '/bra-size-chart' },
    '/blog/sydney-sweeney-bra-size-celebrity-fitting-guide': { status: 301, destination: '/fit-guide' },
    '/blog/can-breast-size-change-naturally-guide': { status: 301, destination: '/guides/how-often-to-measure-bra-size' },
    '/blog/understanding-cup-sizes-breast-measurement': { status: 301, destination: '/guides/how-cup-sizes-work' },
    '/blog/how-bra-sizes-work-numbers-letters-explained': { status: 301, destination: '/guides/how-bra-sizes-work' },
    '/blog/bra-size-calculator-reddit-a-bra-that-fits': { status: 301, destination: '/blog/are-bra-size-calculators-accurate' },
  },
  prefetch: { prefetchAll: true },
  vite: {
    plugins: [tailwindcss()],
    build: {
      cssMinify: true,
    },
  },
});

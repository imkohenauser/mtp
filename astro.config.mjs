import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightThemeFlexoki from 'starlight-theme-flexoki';
import starlightGitHubAlerts from 'starlight-github-alerts';
import starlightLlmsTxt from 'starlight-llms-txt';
import starlightLinksValidator from 'starlight-links-validator';
import starlightScrollToTop from 'starlight-scroll-to-top';

export default defineConfig({
  site: 'https://mappingtheprompt.com',
  integrations: [
    starlight({
      plugins: [
        starlightThemeFlexoki({ accentColor: 'blue' }),
        starlightGitHubAlerts(),
        starlightLlmsTxt({
          projectName: 'MTP (Mapping the Prompt)',
          description:
            'A framework for steering LLM output through sliders, grid coordinates, and presets. Documentation is authored in English (default); Japanese pages live under `/ja/` on the site.',
          details: `## How to use this site as context

- **Start here for concepts**: read the *MTP core documentation* set, then optional deep dives if needed.
- **Benchmarks**: the *Comparisons (landing pages + baselines)* set explains tasks and structure without every per-coordinate model output.
- **Full evidence**: \`llms-full.txt\` includes all benchmark pages (every slider/grid cell and preset run). Prefer it when you need verbatim model outputs or citations.

## Locales

- Default locale for generated \`llms*.txt\` exports is **English** (\`/\` URLs). Japanese mirrors the same slugs under \`/ja/\` in the web docs.`,
          optionalLinks: [
            {
              label: 'Documentation site (human UI)',
              url: 'https://mappingtheprompt.com/',
              description: 'Browse the same content with navigation, search, and both EN/JA locales.',
            },
            {
              label: 'MTP source repository',
              url: 'https://github.com/imkohenauser/mtp',
              description: 'Project source and issue tracker.',
            },
          ],
          customSets: [
            {
              label: 'MTP core documentation',
              description:
                'Foundational concepts, optional background, and the MTP Skill — the minimum to apply MTP in practice.',
              paths: ['index*', 'foundational/**', 'optional/**', 'skills/**'],
            },
            {
              label: 'Comparisons (landing pages + baselines)',
              description:
                'Benchmark section introductions, task landing pages, model-pair indexes, and baseline runs — excludes dense per-coordinate outputs (see complete documentation for those).',
              paths: ['comparisons/**/index', 'comparisons/**/baseline'],
            },
          ],
          promote: [
            'index*',
            'foundational/overview*',
            'foundational/node-reference*',
            'foundational/grid-and-coordinate-system*',
            'foundational/**',
            'skills/**',
            'optional/**',
          ],
          demote: ['comparisons/**'],
          exclude: [
            'comparisons/**/slider/**',
            'comparisons/**/grid/**',
            'comparisons/**/preset/**',
          ],
          pageSeparator: '\n\n---\n\n',
        }),
        starlightLinksValidator(),
        starlightScrollToTop({
          position: 'right',
          tooltipText: {
            'en': 'Scroll to top',
            'ja': 'ページの先頭へ',
          },
          showTooltip: true,
          showOnHomepage: true,
          smoothScroll: true,
          showProgressRing: true,
          borderRadius: '50',
          progressRingColor: 'var(--color-base-400)',
       }),
      ],
      customCss: [
        '@fontsource/source-serif-4/400.css',
        '@fontsource/source-serif-4/600.css',
        '@fontsource/inter/400.css',
        '@fontsource/inter/700.css',
        './src/styles/global.css',
      ],
      title: 'MTP Docs',
      logo: {
        src: './public/images/common/logo.svg',
        alt: 'MTP (Mapping the Prompt)',
      },
      head: [
        {
          tag: 'script',
          attrs: {
            async: true,
            src: 'https://www.googletagmanager.com/gtag/js?id=G-5LVZE8CEYC',
          },
        },
        {
          tag: 'script',
          content: `
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-5LVZE8CEYC');
          `,
        },
        {
          tag: 'link',
          attrs: {
            rel: 'icon',
            href: '/favicon.ico',
            sizes: 'any',
          },
        },
        {
          tag: 'link',
          attrs: {
            rel: 'icon',
            type: 'image/svg+xml',
            href: '/favicon.svg',
          },
        },
        {
          tag: 'link',
          attrs: {
            rel: 'apple-touch-icon',
            href: '/apple-touch-icon.png',
          },
        },
      ],
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: 'https://github.com/imkohenauser/mtp',
        },
      ],
      locales: {
        root: {
          label: 'English',
          lang: 'en',
        },
        ja: {
          label: '日本語',
          lang: 'ja',
        },
      },
      sidebar: [
        {
          label: 'Foundational',
          translations: { ja: '基本' },
          items: [
            {
              label: 'Overview',
              slug: 'foundational/overview',
              translations: { ja: '概要' },
            },
            {
              label: 'Node Reference',
              slug: 'foundational/node-reference',
              translations: { ja: 'ノードリファレンス' },
            },
            {
              label: 'Grid and Coordinate System',
              slug: 'foundational/grid-and-coordinate-system',
              translations: { ja: 'グリッドと座標系' },
            },
          ],
        },
        {
          label: 'Optional',
          translations: { ja: '補足' },
          items: [
            {
              label: 'Design Background',
              slug: 'optional/design-background',
              translations: { ja: '設計上の背景' },
            },
            {
              label: 'Color Grid Visualization',
              slug: 'optional/color-grid-visualization',
              translations: { ja: '色グリッド可視化' },
            },
            {
              label: 'Mapping and Sequence',
              slug: 'optional/mapping-and-sequence',
              translations: { ja: '分類と順序' },
            },
          ],
        },
        {
          label: 'Skills',
          translations: { ja: 'スキル' },
          items: [
            {
              label: 'MTP Skill (beta)',
              slug: 'skills/mtp',
              translations: { ja: 'MTP Skill (beta)' },
            },
          ],
        },
        {
          label: 'Comparisons',
          translations: { ja: '比較' },
          items: [
            {
              label: 'Overview',
              slug: 'comparisons',
              translations: { ja: '概要' },
            },
            {
              label: 'Text Generation',
              translations: { ja: 'テキスト生成' },
              collapsed: false,
              items: [
                {
                  label: 'Overview',
                  slug: 'comparisons/text-generation',
                  translations: { ja: '概要' },
                },
                {
                  label: '1. Explanatory Task',
                  slug: 'comparisons/text-generation/01_origins-of-language',
                  translations: { ja: '1. 説明課題' },
                },
                {
                  label: '2. Comparison Task',
                  slug: 'comparisons/text-generation/02_model-self-compare',
                  translations: { ja: '2. 比較課題' },
                },
                {
                  label: '3. Design Task',
                  slug: 'comparisons/text-generation/03_kyoto-one-day-itinerary',
                  translations: { ja: '3. 設計課題' },
                },
              ],
            },
            {
              label: 'Image Generation',
              translations: { ja: '画像生成' },
              collapsed: false,
              items: [
                {
                  label: 'Overview',
                  slug: 'comparisons/image-generation',
                  translations: { ja: '概要' },
                },
                {
                  label: '1. Mona Lisa Portrait',
                  slug: 'comparisons/image-generation/01_mona-lisa-portrait',
                  translations: { ja: '1. モナ・リザのポートレート' },
                },
                {
                  label: '2. Editorial Fashion Photography',
                  slug: 'comparisons/image-generation/02_editorial-fashion-photography',
                  translations: { ja: '2. ファッション雑誌の写真' },
                },
                {
                  label: '3. Geometric Billiards Painting',
                  slug: 'comparisons/image-generation/03_geometric-billiards-painting',
                  translations: { ja: '3. 幾何学的なビリヤードの絵画' },
                },
              ],
            },
          ],
        },
      ],
    }),
  ],
});

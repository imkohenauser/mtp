import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { defineConfig } from 'astro/config';

import starlight from '@astrojs/starlight';
import starlightThemeFlexoki from 'starlight-theme-flexoki';
import starlightGitHubAlerts from 'starlight-github-alerts';
import starlightLinksValidator from 'starlight-links-validator';
import starlightScrollToTop from 'starlight-scroll-to-top';
import starlightImageZoom from 'starlight-image-zoom';
import starlightPageActions from 'starlight-page-actions';

/** Production origin; used by Astro `site`, copied Markdown links, and generated llms.txt files. */
const site = 'https://mappingtheprompt.com';
const projectRoot = path.dirname(fileURLToPath(import.meta.url));
const docsSourceRoot = path.join(projectRoot, 'src/content/docs');

const llmsTxtProjectName = 'MTP (Mapping the Prompt)';
const llmsTxtDescription = 'A framework for steering LLM output through sliders, grid coordinates, and presets.';
const llmsTxtDetails =
  'Raw Markdown copies are published for AI assistants and chat tools when rendered documentation pages cannot be fetched or processed directly.';

const llmsTxtSourceDirectories = [
  'src/content/docs/foundational',
  'src/content/docs/optional',
  'src/content/docs/skills',
];

const llmsTxtOptionalSourcePages = [
  'src/content/docs/optional/design-background/index.md',
  'src/content/docs/optional/mapping-and-sequence/index.md',
  'src/content/docs/optional/color-grid-visualization/index.md',
];

const llmsTxtComparisonSourcePages = [
  'src/content/docs/comparisons/index.md',
  'src/content/docs/comparisons/text-generation/index.md',
  'src/content/docs/comparisons/text-generation/01_origins-of-language/index.md',
  'src/content/docs/comparisons/text-generation/02_model-self-compare/index.md',
  'src/content/docs/comparisons/text-generation/03_kyoto-one-day-itinerary/index.md',
  'src/content/docs/comparisons/image-generation/index.md',
  'src/content/docs/comparisons/image-generation/01_mona-lisa-portrait/index.md',
  'src/content/docs/comparisons/image-generation/02_editorial-fashion-photography/index.md',
  'src/content/docs/comparisons/image-generation/03_geometric-billiards-painting/index.md',
];

function toUrlPath(filePath) {
  return filePath.split(path.sep).join('/');
}

function toSiteUrl(filePath) {
  return `${site}/${toUrlPath(filePath)}`;
}

function collectSourceMarkdownFiles(relativeDir) {
  const absoluteDir = path.join(projectRoot, relativeDir);

  if (!fs.existsSync(absoluteDir)) return [];

  return fs
    .readdirSync(absoluteDir, { withFileTypes: true })
    .flatMap((entry) => {
      const entryRelativePath = path.join(relativeDir, entry.name);

      if (entry.isDirectory()) return collectSourceMarkdownFiles(entryRelativePath);
      if (!entry.isFile() || !entry.name.endsWith('.md')) return [];

      return [toUrlPath(entryRelativePath)];
    })
    .sort((a, b) => a.localeCompare(b));
}

function unique(values) {
  return [...new Set(values)];
}

function getLlmsTxtSourcePages() {
  return unique([
    'src/content/docs/index.md',
    ...llmsTxtSourceDirectories.flatMap((dir) =>
      dir === 'src/content/docs/optional' ? llmsTxtOptionalSourcePages : collectSourceMarkdownFiles(dir),
    ),
    ...llmsTxtComparisonSourcePages,
  ]);
}

function sourcePageToMarkdownFile(sourcePage) {
  const sourcePath = path.join(projectRoot, sourcePage);
  const docsRelativePath = toUrlPath(path.relative(docsSourceRoot, sourcePath));
  const docsPathWithoutExtension = docsRelativePath.replace(/\.md$/, '');

  if (docsPathWithoutExtension === 'index') return 'index.md';
  if (docsPathWithoutExtension.endsWith('/index')) {
    return `${docsPathWithoutExtension.slice(0, -'/index'.length)}.md`;
  }

  return `${docsPathWithoutExtension}.md`;
}

function buildLlmsTxt(distPath) {
  const sections = getLlmsTxtSourcePages().map((sourcePage) => {
    const markdownFile = sourcePageToMarkdownFile(sourcePage);
    const markdownPath = path.join(distPath, markdownFile);

    if (!fs.existsSync(markdownPath)) {
      throw new Error(`Missing generated Markdown file for ${sourcePage}: ${markdownFile}`);
    }

    const content = fs.readFileSync(markdownPath, 'utf-8').trim();

    return `---\n\nSource file: ${sourcePage}\nURL: ${toSiteUrl(markdownFile)}\n\n${content}`;
  });

  return `# ${llmsTxtProjectName}
> ${llmsTxtDescription}

${llmsTxtDetails}

${sections.join('\n\n')}
`;
}

/** Writes the project llms.txt after starlight-page-actions has copied per-page Markdown. */
function writeLlmsTxt() {
  return {
    name: 'write-llms-txt',
    hooks: {
      'astro:build:done': ({ dir }) => {
        const distPath = fileURLToPath(dir);

        fs.rmSync(path.join(distPath, 'llms-small.txt'), { force: true });
        fs.rmSync(path.join(distPath, 'llms-full.txt'), { force: true });
        fs.writeFileSync(path.join(distPath, 'llms.txt'), buildLlmsTxt(distPath), 'utf-8');
      },
    },
  };
}

export default defineConfig({
  site,
  integrations: [
    starlight({
      plugins: [
        starlightThemeFlexoki({ accentColor: 'blue' }),
        starlightGitHubAlerts(),
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
        starlightImageZoom(),
        starlightPageActions({
          baseUrl: site,
          actions: {
            chatgpt: false,
            claude: false,
            markdown: false,
          },
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
        src: './public/logo.svg',
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
              label: 'Mapping and Sequence',
              slug: 'optional/mapping-and-sequence',
              translations: { ja: '分類と順序' },
            },
            {
              label: 'Color Grid Visualization',
              slug: 'optional/color-grid-visualization',
              translations: { ja: '色グリッド可視化' },
            },
          ],
        },
        {
          label: 'Skills',
          translations: { ja: 'スキル' },
          items: [
            {
              label: 'Installation',
              slug: 'skills',
              translations: { ja: 'インストール' },
            },
            {
              label: 'MTP Skill',
              translations: { ja: 'MTP Skill' },
              items: [
                {
                  label: 'MTP Skill',
                  slug: 'skills/mtp',
                  translations: { ja: 'MTP Skill' },
                },
                {
                  label: 'Customization',
                  slug: 'skills/mtp/customize',
                  translations: { ja: 'カスタマイズ' },
                },
              ],
            },
            {
              label: 'MTP Playlist Skill',
              translations: { ja: 'MTP Playlist Skill' },
              items: [
                {
                  label: 'MTP Playlist',
                  slug: 'skills/mtp-playlist',
                  translations: { ja: 'MTP Playlist' },
                },
              ],
            },
          ],
        },
        {
          label: 'Comparisons',
          translations: { ja: '比較' },
          items: [
            {
              label: 'Comparisons',
              slug: 'comparisons',
              translations: { ja: '比較' },
            },
            {
              label: 'Text Generation',
              translations: { ja: 'テキスト生成' },
              collapsed: false,
              items: [
                {
                  label: 'Text Generation',
                  slug: 'comparisons/text-generation',
                  translations: { ja: 'テキスト生成' },
                },
                {
                  label: '4. Literary Task',
                  slug: 'comparisons/text-generation/04_alice-in-wonderland',
                  translations: { ja: '4. 文学課題' },
                },
                {
                  label: '3. Design Task',
                  slug: 'comparisons/text-generation/03_kyoto-one-day-itinerary',
                  translations: { ja: '3. 設計課題' },
                },
                {
                  label: '2. Comparison Task',
                  slug: 'comparisons/text-generation/02_model-self-compare',
                  translations: { ja: '2. 比較課題' },
                },
                {
                  label: '1. Explanatory Task',
                  slug: 'comparisons/text-generation/01_origins-of-language',
                  translations: { ja: '1. 説明課題' },
                },
              ],
            },
            {
              label: 'Image Generation',
              translations: { ja: '画像生成' },
              collapsed: false,
              items: [
                {
                  label: 'Image Generation',
                  slug: 'comparisons/image-generation',
                  translations: { ja: '画像生成' },
                },
                {
                  label: '3. Geometric Billiards Painting',
                  slug: 'comparisons/image-generation/03_geometric-billiards-painting',
                  translations: { ja: '3. 幾何学的なビリヤードの絵画' },
                },
                {
                  label: '2. Editorial Fashion Photography',
                  slug: 'comparisons/image-generation/02_editorial-fashion-photography',
                  translations: { ja: '2. ファッション雑誌の写真' },
                },
                {
                  label: '1. Mona Lisa Portrait',
                  slug: 'comparisons/image-generation/01_mona-lisa-portrait',
                  translations: { ja: '1. モナ・リザのポートレート' },
                },
              ],
            },
          ],
        },
      ],
    }),
    writeLlmsTxt(),
  ],
});

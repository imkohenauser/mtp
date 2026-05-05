/**
 * One-off / repeat: resolves ./ and ../ internal links in Starlight docs (.md)
 * to root-absolute paths for starlight-links-validator (errorOnRelativeLinks).
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(__dirname, '..');
const docsRoot = path.join(root, 'src/content/docs');

/** @param {string} dir */
function walkMd(dir, out = []) {
  for (const name of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, name.name);
    if (name.isDirectory()) walkMd(full, out);
    else if (name.name.endsWith('.md')) out.push(full);
  }
  return out;
}

/**
 * @param {string} fromDir posix, relative to docs root (no leading slash), '' for root index
 * @param {string} link e.g. ./foo, ../bar, optional #hash
 */
function toAbsolute(fromDir, link) {
  const hashIdx = link.indexOf('#');
  const pathPart = hashIdx >= 0 ? link.slice(0, hashIdx) : link;
  const hash = hashIdx >= 0 ? link.slice(hashIdx) : '';

  let rel = pathPart;
  if (fromDir === 'ja' || fromDir.startsWith('ja/')) {
    if (rel.startsWith('./ja/')) rel = `./${rel.slice('./ja/'.length)}`;
  }

  if (!rel.startsWith('./') && !rel.startsWith('../')) return null;

  const base = fromDir === '.' || fromDir === '' ? '.' : fromDir;
  const joined = path.posix.normalize(path.posix.join(base, rel));
  let url = '/' + joined.replace(/^\/+/, '').replace(/\/+$/, '');
  if (!url.endsWith('/')) url += '/';
  return url + hash;
}

/**
 * @param {string} fileAbs
 */
function processFile(fileAbs) {
  const relFromDocs = path.relative(docsRoot, fileAbs).split(path.sep).join('/');
  const fromDir = path.posix.dirname(relFromDocs);
  let s = fs.readFileSync(fileAbs, 'utf8');

  s = s.replace(/\]\((\.\.?\/[^")\s]+)(\s+"[^"]*")?\)/g, (full, urlOnly, titlePart) => {
    const abs = toAbsolute(fromDir, urlOnly);
    if (!abs) return full;
    const title = titlePart ?? '';
    return `](${abs}${title})`;
  });

  s = s.replace(/^(\s*link:\s*)(\.\.?\/[^\s#]+\/?)/gm, (_, prefix, url) => {
    const abs = toAbsolute(fromDir, url.trim());
    return abs ? `${prefix}${abs}` : `${prefix}${url}`;
  });

  fs.writeFileSync(fileAbs, s, 'utf8');
}

const files = walkMd(docsRoot);
for (const f of files) processFile(f);

console.log(`Updated ${files.length} markdown files under src/content/docs`);

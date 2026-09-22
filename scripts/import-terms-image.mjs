import { createRequire } from 'node:module';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { articles } from './insurance-terms-data.mjs';

const [source, slug, type, moduleRoot] = process.argv.slice(2);
if (!articles.some(a => a.slug === slug) || !['thumb', 'body1', 'body2'].includes(type)) throw new Error('Unknown article image');
const require = createRequire(import.meta.url);
const sharp = moduleRoot ? require(join(resolve(moduleRoot), 'sharp')) : require('sharp');
const root = dirname(dirname(fileURLToPath(import.meta.url)));
const destination = join(root, 'assets', 'images', `terms-${slug}-${type}.webp`);
// Format optimization only: preserve the generated composition and dimensions.
const result = await sharp(source).webp({ quality: 86, effort: 5 }).toFile(destination);
console.log(JSON.stringify({ destination, width: result.width, height: result.height, bytes: result.size }));

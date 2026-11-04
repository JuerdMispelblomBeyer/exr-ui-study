import { readFileSync, writeFileSync } from 'node:fs';
const f = process.argv[2];
let s = readFileSync(f, 'utf8');
s = s.replace(/<script src="\.\/support\.js"><\/script>/, '');
s = s.replace(/<script data-dc-script[\s\S]*?<\/script>/, '');
s = s.replace(/<x-dc>|<\/x-dc>/g, '');
s = s.replace(/<helmet>|<\/helmet>/g, '');
writeFileSync(f.replace('.dc.html', '.preview.html'), s);
console.log('wrote', f.replace('.dc.html', '.preview.html'));

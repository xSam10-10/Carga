// Rasteriza os ícones SVG gerados por tools/logo.py em PNG.
const {chromium}=require('playwright'),fs=require('fs'),path=require('path');
const R=path.join(__dirname,'..');
const jobs=[['icon.svg','icon-192.png',192],['icon.svg','icon-512.png',512],['icon-maskable.svg','icon-maskable-512.png',512],['tools/icon-apple.svg','icon-180.png',180]];
(async()=>{const b=await chromium.launch();const p=await b.newPage();
 for(const [src,out,n] of jobs){await p.setViewportSize({width:n,height:n});
  await p.setContent(`<style>*{margin:0}svg{display:block;width:${n}px;height:${n}px}</style>`+fs.readFileSync(path.join(R,src),'utf8'));
  await p.screenshot({path:path.join(R,out),omitBackground:true});console.log(out)}
 await b.close()})();

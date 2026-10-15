const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');

const EDGE_PATH = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const HTML_FILE = path.join(__dirname, 'previa_template.html');
const OUTPUT_PDF = path.join(__dirname, 'previa_layout.pdf');

async function generatePDF() {
    console.log('Iniciando Puppeteer com Microsoft Edge...');
    const browser = await puppeteer.launch({
        executablePath: EDGE_PATH,
        headless: 'new',
        args: [
            '--no-sandbox',
            '--disable-gpu',
            '--disable-dev-shm-usage',
            '--font-render-hinting=medium'
        ]
    });

    const page = await browser.newPage();
    
    // Viewport A4
    await page.setViewport({ width: 1200, height: 1600, deviceScaleFactor: 2 });

    console.log('Carregando previa_template.html...');
    const htmlContent = fs.readFileSync(HTML_FILE, 'utf-8');
    await page.setContent(htmlContent, { waitUntil: 'domcontentloaded' });

    console.log('Aguardando renderização de KaTeX e Mermaid...');
    await page.waitForFunction(() => {
        return window.katexDone === true && window.mermaidDone === true;
    }, { timeout: 30000 });

    // Pequena pausa para consolidação de layout dos SVGs
    await new Promise(r => setTimeout(r, 1200));

    console.log('Renderizando PDF com margens estritas ABNT (Sup: 3cm, Esq: 3cm, Inf: 2cm, Dir: 2cm)...');
    await page.pdf({
        path: OUTPUT_PDF,
        format: 'A4',
        printBackground: true,
        margin: {
            top: '3cm',
            left: '3cm',
            bottom: '2cm',
            right: '2cm'
        },
        displayHeaderFooter: true,
        headerTemplate: '<div style="height: 0;"></div>',
        footerTemplate: `
            <div style="font-family: Arial, sans-serif; font-size: 10pt; color: #475569; width: 100%; text-align: right; padding-right: 2cm; padding-bottom: 0.8cm;">
                <span class="pageNumber"></span>
            </div>
        `
    });

    await browser.close();
    console.log('Sucesso! previa_layout.pdf gerado em:', OUTPUT_PDF);
}

generatePDF().catch(err => {
    console.error('Falha na geração do PDF:', err);
    process.exit(1);
});

const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');

const EDGE_PATH = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';

async function renderPDF(htmlPath, pdfPath) {
    const absHtml = path.resolve(htmlPath);
    const absPdf = path.resolve(pdfPath);

    console.log(`[Puppeteer] Abrindo Edge Headless para: ${path.basename(absHtml)}`);
    const browser = await puppeteer.launch({
        executablePath: EDGE_PATH,
        headless: 'new',
        args: [
            '--no-sandbox',
            '--disable-gpu',
            '--disable-dev-shm-usage',
            '--font-render-hinting=medium',
            '--allow-file-access-from-files'
        ]
    });

    try {
        const page = await browser.newPage();
        await page.setViewport({ width: 1200, height: 1600, deviceScaleFactor: 2 });

        const fileUrl = 'file:///' + absHtml.replace(/\\/g, '/');
        console.log(`[Puppeteer] Navegando para ${fileUrl}...`);
        await page.goto(fileUrl, { waitUntil: 'domcontentloaded' });

        console.log('[Puppeteer] Aguardando compilação de fórmulas (KaTeX) e diagramas (Mermaid)...');
        await page.waitForFunction(() => {
            return window.katexDone === true && window.mermaidDone === true;
        }, { timeout: 180000 });

        // Pequena pausa para consolidação de layout dos SVGs
        await new Promise(r => setTimeout(r, 1500));

        console.log(`[Puppeteer] Gerando PDF vetorial com margens ABNT em ${path.basename(absPdf)}...`);
        await page.pdf({
            path: absPdf,
            preferCSSPageSize: true,
            printBackground: true,
            timeout: 300000
        });

        console.log(`[Puppeteer] Sucesso! PDF gerado: ${absPdf}`);
    } finally {
        await browser.close();
    }
}

const args = process.argv.slice(2);
if (args.length < 2) {
    console.error('Uso: node render_html_to_pdf.js <input.html> <output.pdf>');
    process.exit(1);
}

renderPDF(args[0], args[1]).catch(err => {
    console.error('[Puppeteer] Erro fatal durante a renderização:', err);
    process.exit(1);
});

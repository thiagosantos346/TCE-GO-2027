const puppeteer = require('puppeteer-core');

const EDGE_PATH = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';

async function test() {
    const browser = await puppeteer.launch({
        executablePath: EDGE_PATH,
        headless: false,
        ignoreDefaultArgs: ['--enable-automation'],
        args: [
            '--disable-blink-features=AutomationControlled',
            '--start-maximized'
        ]
    });

    const page = await browser.newPage();
    
    page.on('response', async (response) => {
        const url = response.url();
        if (url.includes('/provas/link')) {
            try {
                const json = await response.json();
                console.log('>>> RESPOSTA /provas/link RECEBIDA COM SUCESSO:');
                console.log(JSON.stringify(json, null, 2));
            } catch (e) {
                console.log('Erro ao ler json de /provas/link:', e.message);
            }
        }
    });

    console.log('Navegando...');
    await page.goto('https://www.pciconcursos.com.br/provas/download/analista-judiciario-area-administrativa-tecnologia-da-informacao-trt-16-fgv-2022', {
        waitUntil: 'domcontentloaded'
    });

    console.log('Aguardando 8 segundos para Turnstile resolver...');
    await new Promise(r => setTimeout(r, 8000));

    await browser.close();
}

test().catch(console.error);

const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');
const https = require('https');

const EDGE_PATH = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const DEST_DIR = path.join(__dirname, 'provas_pci');
const LINKS_FILE = path.join(DEST_DIR, 'links_diretos.txt');

if (!fs.existsSync(DEST_DIR)) {
    fs.mkdirSync(DEST_DIR, { recursive: true });
}

const URLS = [
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-area-administrativa-tecnologia-da-informacao-trt-16-fgv-2022",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-governanca-e-gestao-de-tecnologia-da-informacao-trf-6-cebraspe-2025",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-suporte-em-tecnologia-da-informacao-stj-cebraspe-2024",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-trf-6-cebraspe-2025",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-trt-3-fumarc-2022",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-trt-8-cespe-2016",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-trt-14-fcc-2016",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-trt-23-fcc-2016",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-trt-9-fcc-2015",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-banco-de-dados-tj-ap-fgv-2023",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-desenvolvimento-de-sistemas-tj-ap-fgv-2023",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-seguranca-da-informacao-tj-ap-fgv-2023",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-telecomunicacoes-tj-ap-fgv-2023",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-apoio-especializado-tecnologia-da-informacao-trt-6-fcc-2012",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-area-apoio-especializado-especialidade-tecnologia-da-informacao-trt-7-cespe-2017",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-area-apoio-especializado-especialidade-suporte-em-tecnologia-da-informacao-trf-1-fgv-2024",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-area-apoio-especializado-especialidade-tecnologia-da-informacao-trf-1-fgv-2024",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-area-apoio-especializado-tecnologia-da-informacao-trt-da-24-regiao-fgv-2025",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-area-apoio-especializado-tecnologia-da-informacao-trt-da-8-regiao-cebraspe-2022",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-area-de-apoio-especializado-governanca-e-gestao-de-tecnologia-da-informacao-trf-da-5-regiao-ibfc-2024",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-classe-c-analista-de-tecnologia-da-informacao-tj-mg-ibfc-2022",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-especialidade-analista-de-tecnologia-da-informacao-tjm-mg-instituto-consulplan-2021",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-gestao-e-governanca-de-tecnologia-da-informacao-tj-rr-fgv-2024",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-grupo-tecnologia-da-informacao-analista-de-gestao-de-tic-tj-rj-cebraspe-2021",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-grupo-tecnologia-da-informacao-analista-de-infraestrutura-de-tic-tj-rj-cebraspe-2021",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-grupo-tecnologia-da-informacao-analista-de-negocios-tj-rj-cebraspe-2021",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-grupo-tecnologia-da-informacao-analista-de-projetos-tj-rj-cebraspe-2021",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-grupo-tecnologia-da-informacao-analista-de-seguranca-da-informacao-tj-rj-cebraspe-2021",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-grupo-tecnologia-da-informacao-analista-de-sistemas-tj-rj-cebraspe-2021",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-infraestrutura-de-tecnologia-da-informacao-tj-rr-fgv-2024",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-infraestrutura-de-tecnologia-da-informacao-tj-pb-faperp-2012",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-suporte-em-tecnologia-da-informacao-tj-dft-fgv-2022",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-suporte-em-tecnologia-da-informacao-tj-dft-cespe-2015",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-suporte-em-tecnologia-da-informacao-stj-cespe-2015",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-suporte-em-tecnologia-da-informacao-stf-cespe-2013",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-suporte-em-tecnologia-da-informacao-stf-cespe-2008",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-tj-mt-fgv-2024",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-da-13-regiao-fgv-2022",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-13-fgv-2022",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-24-fcc-2017",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-11-fcc-2017",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-tj-ba-fgv-2015",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-15-fcc-2015",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-3-fcc-2015",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-4-fcc-2015",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-13-fcc-2014",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-16-fcc-2014",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-1-fcc-2014",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-2-fcc-2014",
    "https://www.pciconcursos.com.br/provas/download/analista-judiciario-tecnologia-da-informacao-trt-10-cespe-2013"
];

function downloadFile(url, destPath) {
    return new Promise((resolve, reject) => {
        const file = fs.createWriteStream(destPath);
        https.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                'Referer': 'https://www.pciconcursos.com.br/'
            }
        }, (response) => {
            if (response.statusCode >= 300 && response.statusCode < 400 && response.headers.location) {
                file.close();
                return downloadFile(response.headers.location, destPath).then(resolve).catch(reject);
            }
            response.pipe(file);
            file.on('finish', () => {
                file.close(resolve);
            });
        }).on('error', (err) => {
            fs.unlink(destPath, () => {});
            reject(err);
        });
    });
}

async function main() {
    console.log(`Iniciando automação com Microsoft Edge...`);
    console.log(`Total de concursos a processar: ${URLS.length}\n`);

    const browser = await puppeteer.launch({
        executablePath: EDGE_PATH,
        headless: false,
        ignoreDefaultArgs: ['--enable-automation'],
        args: [
            '--disable-blink-features=AutomationControlled',
            '--window-size=1000,700'
        ]
    });

    const page = await browser.newPage();
    const linksStream = fs.createWriteStream(LINKS_FILE, { flags: 'a', encoding: 'utf-8' });

    for (let i = 0; i < URLS.length; i++) {
        const url = URLS[i];
        const slug = url.split('/').pop();
        console.log(`[${i + 1}/${URLS.length}] Processando: ${slug}...`);

        let arquivosRecebidos = null;

        const responseHandler = async (response) => {
            if (response.url().includes('/provas/link')) {
                try {
                    const json = await response.json();
                    if (json && json.ok && json.arquivos) {
                        arquivosRecebidos = json.arquivos;
                    }
                } catch (e) {}
            }
        };

        page.on('response', responseHandler);

        try {
            await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });

            // Aguarda até 10 segundos pela liberação automática dos links pelo Turnstile
            const inicio = Date.now();
            while (!arquivosRecebidos && (Date.now() - inicio) < 10000) {
                await new Promise(r => setTimeout(r, 500));
            }

            if (arquivosRecebidos && arquivosRecebidos.length > 0) {
                for (const item of arquivosRecebidos) {
                    const pdfUrl = item.ver || item.baixar;
                    const nomeArquivo = `${slug}___${item.arquivo}`;
                    const caminhoDestino = path.join(DEST_DIR, nomeArquivo);

                    linksStream.write(`${pdfUrl}\n`);

                    if (fs.existsSync(caminhoDestino) && fs.statSync(caminhoDestino).size > 1000) {
                        console.log(`   -> [Já existe] ${nomeArquivo}`);
                    } else {
                        console.log(`   -> [Baixando] ${nomeArquivo}`);
                        try {
                            await downloadFile(pdfUrl, caminhoDestino);
                        } catch (err) {
                            console.log(`      Erro no download: ${err.message}`);
                        }
                    }
                }
            } else {
                console.log(`   -> [Aviso] Captcha pendente ou links não liberados a tempo.`);
            }
        } catch (err) {
            console.log(`   -> Erro ao acessar: ${err.message}`);
        } finally {
            page.off('response', responseHandler);
        }

        await new Promise(r => setTimeout(r, 600));
    }

    linksStream.end();
    await browser.close();

    console.log(`\nProcesso concluído!`);
    console.log(`Arquivos salvos em: ${DEST_DIR}`);
    console.log(`Lista de links diretos salva em: ${LINKS_FILE}`);
}

main().catch(console.error);


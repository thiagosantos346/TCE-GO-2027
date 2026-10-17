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

// Carregar URLs selecionadas ou usar a lista de alta relevância para as lacunas do edital
let URLS = [];
const URLS_JSON_PATH = path.join('C:\\Users\\thiag\\.gemini\\antigravity\\brain\\dbf7b4de-f50d-4fb0-b4cd-f0e5c20a827d\\scratch\\selected_provas_urls.json');

if (fs.existsSync(URLS_JSON_PATH)) {
    try {
        URLS = JSON.parse(fs.readFileSync(URLS_JSON_PATH, 'utf-8'));
    } catch (e) {
        console.warn(`Erro ao ler ${URLS_JSON_PATH}:`, e.message);
    }
}

if (!URLS || URLS.length === 0) {
    URLS = [
        "https://www.pciconcursos.com.br/provas/download/analista-de-controle-externo-ciencias-contabeis-tce-go-fgv-2024",
        "https://www.pciconcursos.com.br/provas/download/auditor-fiscal-de-controle-externo-ciencias-contabeis-tce-sc-fgv-2026",
        "https://www.pciconcursos.com.br/provas/download/auditor-fiscal-de-controle-externo-economia-tce-sc-fgv-2026",
        "https://www.pciconcursos.com.br/provas/download/auditor-fiscal-de-controle-externo-ciencias-atuariais-tce-sc-fgv-2026",
        "https://www.pciconcursos.com.br/provas/download/auditor-de-controle-externo-fiscalizacao-contabilidade-tce-pa-fgv-2024",
        "https://www.pciconcursos.com.br/provas/download/analista-de-controle-externo-controle-externo-tce-go-fgv-2024",
        "https://www.pciconcursos.com.br/provas/download/analista-de-controle-externo-tecnologia-da-informacao-tce-go-fgv-2024",
        "https://www.pciconcursos.com.br/provas/download/auditor-de-controle-externo-administrativa-contabilidade-tce-pa-fgv-2024",
        "https://www.pciconcursos.com.br/provas/download/analista-de-controle-externo-juridica-tce-go-fgv-2024",
        "https://www.pciconcursos.com.br/provas/download/auditor-de-controle-externo-administrativa-administracao-tce-pa-fgv-2024",
        "https://www.pciconcursos.com.br/provas/download/auditor-de-controle-externo-administrativa-direito-tce-pa-fgv-2024",
        "https://www.pciconcursos.com.br/provas/download/auditor-de-controle-externo-administrativa-gestao-governamental-tce-pa-fgv-2024",
        "https://www.pciconcursos.com.br/provas/download/auditor-de-controle-externo-administrativa-ciencia-de-dados-tce-pa-fgv-2024",
        "https://www.pciconcursos.com.br/provas/download/analista-judiciario-area-administrativa-sem-especialidade-trt-da-24-regiao-fgv-2025",
        "https://www.pciconcursos.com.br/provas/download/tecnico-judiciario-area-administrativa-sem-especialidade-trt-da-24-regiao-fgv-2025",
        "https://www.pciconcursos.com.br/provas/download/analista-judiciario-area-administrativa-contabilidade-trt-da-24-regiao-fgv-2025",
        "https://www.pciconcursos.com.br/provas/download/auditor-fiscal-de-controle-externo-ciencias-da-computacao-sistemas-de-informacao-tce-sc-fgv-2026",
        "https://www.pciconcursos.com.br/provas/download/auditor-fiscal-de-controle-externo-administracao-tce-sc-fgv-2026",
        "https://www.pciconcursos.com.br/provas/download/auditor-fiscal-de-controle-externo-direito-tce-sc-fgv-2026",
        "https://www.pciconcursos.com.br/provas/download/analista-administrativo-tj-sc-fgv-2026",
        "https://www.pciconcursos.com.br/provas/download/analista-judiciario-area-administrativa-trt-1-fgv-2024",
        "https://www.pciconcursos.com.br/provas/download/auditor-de-controle-externo-controle-externo-especifica-de-area-comum-tce-pi-fgv-2025"
    ];
}

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
            if (response.statusCode !== 200) {
                file.close();
                fs.unlink(destPath, () => {});
                return reject(new Error(`HTTP Status ${response.statusCode}`));
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
    console.log(`================================================================`);
    console.log(`BUSCA E DOWNLOAD DE PROVAS PCI CONCURSOS - FOCO EM LACUNAS`);
    console.log(`Navegador: Microsoft Edge (${EDGE_PATH})`);
    console.log(`Diretório de destino: ${DEST_DIR}`);
    console.log(`Total de concursos prioritários mapeados: ${URLS.length}`);
    console.log(`================================================================\n`);

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

    let sucessos = 0;
    let pulados = 0;
    let falhas = 0;

    for (let i = 0; i < URLS.length; i++) {
        const url = URLS[i];
        const slug = url.split('/').pop();
        console.log(`[${i + 1}/${URLS.length}] Acessando: ${slug}...`);

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
                await new Promise(r => setTimeout(r, 400));
            }

            if (arquivosRecebidos && arquivosRecebidos.length > 0) {
                console.log(`   ✓ ${arquivosRecebidos.length} arquivos detectados`);
                for (const item of arquivosRecebidos) {
                    const pdfUrl = item.ver || item.baixar;
                    const nomeArquivo = `${slug}___${item.arquivo}`;
                    const caminhoDestino = path.join(DEST_DIR, nomeArquivo);

                    linksStream.write(`${pdfUrl}\n`);

                    if (fs.existsSync(caminhoDestino) && fs.statSync(caminhoDestino).size > 1000) {
                        console.log(`      [Já existe] ${nomeArquivo}`);
                        pulados++;
                    } else {
                        console.log(`      [Baixando] ${nomeArquivo} ...`);
                        try {
                            await downloadFile(pdfUrl, caminhoDestino);
                            console.log(`         -> Concluído (${(fs.statSync(caminhoDestino).size / 1024).toFixed(1)} KB)`);
                            sucessos++;
                        } catch (err) {
                            console.log(`         -> Erro no download: ${err.message}`);
                            falhas++;
                        }
                    }
                }
            } else {
                console.log(`   ⚠ [Aviso] Captcha pendente ou links não liberados a tempo.`);
                falhas++;
            }
        } catch (err) {
            console.log(`   ✖ Erro ao acessar a página: ${err.message}`);
            falhas++;
        } finally {
            page.off('response', responseHandler);
        }

        await new Promise(r => setTimeout(r, 600));
    }

    linksStream.end();
    await browser.close();

    console.log(`\n================================================================`);
    console.log(`DOWNLOAD CONCLUÍDO COM SUCESSO!`);
    console.log(`Total baixados agora: ${sucessos}`);
    console.log(`Total já existentes: ${pulados}`);
    console.log(`Total falhas/não liberados: ${falhas}`);
    console.log(`Pasta: ${DEST_DIR}`);
    console.log(`================================================================`);
}

main().catch(console.error);


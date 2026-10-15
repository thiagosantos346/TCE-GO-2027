# Script PowerShell para download automatizado de Provas e Gabaritos do PCI Concursos

$pastaDestino = Join-Path $PWD "provas_pci"
if (!(Test-Path $pastaDestino)) {
    New-Item -ItemType Directory -Path $pastaDestino | Out-Null
}

$arquivoLinks = Join-Path $pastaDestino "links_diretos.txt"
if (Test-Path $arquivoLinks) {
    Remove-Item $arquivoLinks
}

$headers = @{
    "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    "Referer"    = "https://www.pciconcursos.com.br/"
}

$paginas = @(
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
)

$total = $paginas.Count
$i = 1

Write-Host "Iniciando raspagem e download de $total itens..." -ForegroundColor Cyan

foreach ($url in $paginas) {
    $slug = $url.Split('/')[-1]
    Write-Host "[$i/$total] Obtendo links de: $slug" -ForegroundColor Yellow

    try {
        $html = (Invoke-WebRequest -Uri $url -Headers $headers -UseBasicParsing -TimeoutSec 15).Content
        $pdfLinks = [regex]::Matches($html, 'href=["'']([^"'']*\.pdf)["'']') | ForEach-Object { $_.Groups[1].Value } | Select-Object -Unique

        foreach ($link in $pdfLinks) {
            $pdfUrl = if ($link -match '^https?://') { $link } else { "https://www.pciconcursos.com.br$link" }
            "$pdfUrl" | Out-File -FilePath $arquivoLinks -Append -Encoding utf8
            
            $nomeOriginal = [System.IO.Path]::GetFileName($pdfUrl)
            $nomeFinal = "${slug}___${nomeOriginal}"
            $destino = Join-Path $pastaDestino $nomeFinal

            if (Test-Path $destino) {
                Write-Host "   -> [Ja baixado] $nomeFinal" -ForegroundColor DarkGray
            } else {
                Write-Host "   -> [Baixando] $nomeFinal" -ForegroundColor Green
                Invoke-WebRequest -Uri $pdfUrl -Headers $headers -OutFile $destino -UseBasicParsing -TimeoutSec 30
            }
        }
    } catch {
        Write-Host "   -> [Falha ao acessar]: $_" -ForegroundColor Red
    }

    $i++
    Start-Sleep -Milliseconds 400
}

Write-Host "`nFinalizado! Arquivos salvos em: $pastaDestino" -ForegroundColor Cyan
Write-Host "Links registrados em: $arquivoLinks" -ForegroundColor Cyan


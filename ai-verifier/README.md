# ai-verifier — Servizio di verifica visiva

Servizio Python (FastAPI) che confronta le foto scattate dal compratore con le foto
di riferimento registrate all'emissione del certificato e restituisce un verdetto
firmato: conforme, non conforme o incerto (SRS §3.1.5).

Gira su CPU, senza GPU (RNF-VIN-03).

## Struttura
- `app/` — API e configurazione
- `app/pipeline/` — stadi della pipeline (qualità, segmentazione, DINOv2, OCR, matching, mappa delle differenze, verdetto)
- `eval/` — script di valutazione sul dataset
- `tests/` — test automatici

## Requisiti
Python 3.11

Le istruzioni di installazione e avvio saranno completate con lo sviluppo del servizio.

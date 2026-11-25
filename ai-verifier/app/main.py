"""Applicazione FastAPI del servizio di verifica visiva."""

from fastapi import FastAPI

from app.config import get_settings

app = FastAPI(
    title="SafeResale ai-verifier",
    description="Servizio di verifica visiva delle sneaker (SRS §3.1.5).",
    version=get_settings().pipeline_version,
)


@app.get("/health")
def health() -> dict[str, str]:
    """Indica che il servizio è acceso e quale versione della pipeline sta usando.

    Non decide se fare la verifica: la scelta è del compratore (RS-4.6).
    Serve all'app per avvisare il compratore se il servizio non risponde (RNF-AFF-02)
    e a Docker per controllare che il container sia partito.

    Returns:
        Un dizionario con `status` ("ok") e `pipelineVersion`.
    """
    return {"status": "ok", "pipelineVersion": get_settings().pipeline_version}

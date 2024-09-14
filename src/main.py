from fastapi import FastAPI


from src.notes.router import router as router_notes

app = FastAPI(
    title="Заметки"
)


app.include_router(router_notes)

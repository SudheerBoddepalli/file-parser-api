import asyncio, os, json
import pytest
from httpx import AsyncClient
from app.main import app
from app.db import init_db, engine, SessionLocal
import sqlalchemy

@pytest.fixture(autouse=True)
def prepare_db(tmp_path, monkeypatch):
    # use a temp sqlite file for tests
    db_file = tmp_path / "test.db"
    monkeypatch.setenv("DB_URL", f"sqlite:///{db_file}")
    # reload modules that depend on DB_URL
    import importlib
    importlib.reload(__import__("app.db", fromlist=["init_db"]))
    from app.db import init_db as init_db2
    init_db2()
    yield
    # cleanup handled by tmp_path

@pytest.mark.asyncio
async def test_signup_login_and_upload_and_flow(tmp_path):
    async with AsyncClient(app=app, base_url="http://test") as client:
        # signup
        r = await client.post("/auth/signup", params={"email":"test@example.com","password":"secret"})
        assert r.status_code == 201
        # login
        r = await client.post("/auth/login", params={"email":"test@example.com","password":"secret"})
        assert r.status_code == 200
        token = r.json().get("access_token")
        assert token
        headers = {"Authorization": f"Bearer {token}"}
        # upload sample.csv
        sample = os.path.join(os.getcwd(), "sample.csv")
        files = {"file": ("sample.csv", open(sample, "rb"), "text/csv")}
        r = await client.post("/files", files=files, headers=headers)
        assert r.status_code == 201
        fid = r.json().get("file_id")
        assert fid
        # poll progress until ready (timeout)
        for _ in range(30):
            r = await client.get(f"/files/{fid}/progress")
            assert r.status_code == 200
            data = r.json()
            if data.get("status") == "ready":
                break
            await asyncio.sleep(0.1)
        assert data.get("status") == "ready"
        # fetch parsed content
        r = await client.get(f"/files/{fid}")
        assert r.status_code in (200,202)
        if r.status_code == 200:
            body = r.json()
            assert body.get("total_rows") >= 1
        # delete file
        r = await client.delete(f"/files/{fid}", headers=headers)
        assert r.status_code == 204

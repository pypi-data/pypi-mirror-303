def test_custom_encoding(api, session):
    data = "hi alex!"

    @api.route("/", methods=["POST"])
    async def route(req, resp):
        req.encoding = "ascii"
        resp.text = await req.text

    r = session.post(api.url_for(route), content=data)
    assert r.text == data


def test_bytes_encoding(api, session):
    data = b"hi lenny!"

    @api.route("/", methods=["POST"])
    async def route(req, resp):
        resp.text = (await req.content).decode("utf-8")

    r = session.post(api.url_for(route), content=data)
    assert r.content == data

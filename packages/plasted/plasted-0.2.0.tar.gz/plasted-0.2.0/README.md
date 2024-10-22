# Plasted

Fix the problem to run an WSGI app configured with plaster using uwsgi.

uwsgi as many loader, but it does not support plaster, only the old paste.ini
format.

Plasted

```bash
export PLASTER_URI=file+yaml://test.yaml
uwsgi -M --workers 1 --http 127.0.0.1:8000  --module pasted:app
```

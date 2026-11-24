"""Sobe o markdown-live-editor em http://localhost e abre o navegador.

Existe porque o YouTube recusa embed quando a pagina vem de file:// (a origem
vira "null" e o player devolve erro 153). Servido por http, o video toca dentro
do proprio app.
"""
import functools, http.server, os, sys, threading, webbrowser

PASTA = os.path.dirname(os.path.abspath(__file__))
PORTAS = range(8123, 8143)


class Servidor(http.server.ThreadingHTTPServer):
    # no Windows o SO_REUSEADDR deixa dois processos na mesma porta; desligado,
    # a varredura abaixo encontra de fato uma porta livre
    allow_reuse_address = False
    daemon_threads = True


def abrir_servidor(handler):
    for porta in PORTAS:
        try:
            return Servidor(("127.0.0.1", porta), handler), porta
        except OSError:
            continue
    return None, None


def main():
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=PASTA)
    srv, porta = abrir_servidor(handler)
    if srv is None:
        print(f"Nenhuma porta livre entre {PORTAS[0]} e {PORTAS[-1]}.")
        return 1

    url = f"http://localhost:{porta}/index.html"
    print("", flush=True)
    print(f"  markdown-live-editor  ->  {url}", flush=True)
    print("  Deixe esta janela aberta. Ctrl+C (ou fechar a janela) para o servidor.", flush=True)
    print("", flush=True)
    if "--sem-navegador" not in sys.argv:
        threading.Timer(0.8, webbrowser.open, args=(url,)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
    finally:
        srv.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

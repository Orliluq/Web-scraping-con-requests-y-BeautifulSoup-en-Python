import requests
from bs4 import BeautifulSoup

def get_main_news():
    url = 'https://www.cmmedia.es/noticias/castilla-la-mancha/'
    respuesta = launch_request(url)
    contenido_web = BeautifulSoup(respuesta.text, 'lxml')
    noticias = contenido_web.find('ul', attrs={'class':'news-list'})
    if noticias is not None:
        articulos = noticias.findChildren('div', attrs={'class':'media-body'})
        for articulo in articulos:
            noticias.append({
                'url': articulo.find('h3').a.get('href'),
                'titulo': articulo.find('h3').get_text()
            })
    return noticias if noticias is not None else []

def launch_request(url):
    try:
        respuesta = requests.get(
            url,
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
            }
        )
        respuesta.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    return respuesta

if __name__ == '__main__':
    response = launch_request('https://www.cmmedia.es/noticias/castilla-la-mancha')
    print(response.status_code) # Correctly accessing status_code from the response object
    print(response.text) # Correctly accessing text from the response object
    print(response.headers) # Correctly accessing headers from the response object
    print(response.request.headers) # Correctly accessing request headers from the response object
    print(response.request.method) # Correctly accessing request method from the response object

    noticias = get_main_news()
    for noticia in noticias:
        noticia = get_all_info_by_news(noticia)
        print('=================================')
        print(noticia)
        print('=================================')
        print('=================================')

       
       
    # Si queremos ver la respuesta que ha dado el servidor al hacer la petición lo podremos hacer con status_code, también lo podemos usar para parar la ejecución sino recibimos un estado válido como por ejemplo el 404 o 500.
# print(requests.status_code)

    # Para ver el contenido utilizaremos text, aquí se guarda todo el html de la página.
# print(requests.text)

    # Con header veremos las cabeceras que nos devuelve la página, esta puede contener cookies, información sobre que tipo de servidor están usando, el tipo de contenido (json, html, texto), etc.
# print(requests.headers)

    # Aquí podemos ver la cabecera de la petición, es decir, la que enviamos nosotros.
# print(requests.request.headers)

    # Para ver el método que hemos usado lo haremos con method, en nuestro caso get que también se ve en la llamada de la función.
# print(requests.request.method)

# contenido_web = BeautifulSoup(requests.text, 'lxml')
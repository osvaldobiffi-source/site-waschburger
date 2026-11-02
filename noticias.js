// Mostra as notícias de noticias.json (atualizado uma vez por dia pelo GitHub Actions).
(function () {
  var POR_AREA = 3;

  function quando(iso) {
    var d = new Date(iso);
    var horas = Math.floor((Date.now() - d.getTime()) / 36e5);
    if (horas < 1) return 'agora há pouco';
    if (horas < 24) return 'há ' + horas + (horas === 1 ? ' hora' : ' horas');
    var dias = Math.floor(horas / 24);
    if (dias === 1) return 'ontem';
    if (dias < 7) return 'há ' + dias + ' dias';
    return d.toLocaleDateString('pt-BR', { day: 'numeric', month: 'short' });
  }

  function preencher(id, itens) {
    var lista = document.getElementById(id);
    lista.textContent = '';
    if (!itens || !itens.length) {
      var vazio = document.createElement('li');
      vazio.className = 'vazio';
      vazio.textContent = 'Nenhuma notícia nova nos últimos dias.';
      lista.appendChild(vazio);
      return;
    }
    itens.slice(0, POR_AREA).forEach(function (n) {
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.href = n.link;
      a.target = '_blank';
      a.rel = 'noopener';
      var titulo = document.createElement('strong');
      titulo.textContent = n.titulo;
      var meta = document.createElement('span');
      meta.textContent = n.fonte + ' · ' + quando(n.data);
      a.appendChild(titulo);
      a.appendChild(meta);
      li.appendChild(a);
      lista.appendChild(li);
    });
  }

  fetch('noticias.json', { cache: 'no-cache' })
    .then(function (r) { return r.json(); })
    .then(function (d) {
      preencher('noticias-tributario', d.tributario);
      preencher('noticias-previdenciario', d.previdenciario);
      if (d.atualizado) {
        document.getElementById('atualizado').textContent =
          'Atualizadas automaticamente a partir de fontes oficiais · ' +
          new Date(d.atualizado).toLocaleDateString('pt-BR', { day: 'numeric', month: 'long' });
      }
    })
    .catch(function () {
      preencher('noticias-tributario', []);
      preencher('noticias-previdenciario', []);
    });
})();

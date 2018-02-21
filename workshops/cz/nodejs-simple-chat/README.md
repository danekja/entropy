# Jednoducha chatovaci aplikace

Vysledkem teto ukazky je jednoducha chatovaci aplikace napsana v Node.js.

Ukazeme si realizaci nasledujicich funkci:
* posilani zprav
* zadani jmena
* prirazeni vlastni barvy kazdemu uzivateli
* odeslani historie zprav nove prihlasenemu uzivateli

## Upozorneni

Tato ukazka je zamyslena jako jednoducha demonstrace pro nespecializovane stredni
skoly. Vysledna aplikace nesplnuje zakladni pozadavky na bezpecnost
ci schopnost reagovat na chybove stavy. Podklad zaroven nevysvetluje 
zakladni principy na kterych aplikace funguje. Neni vhodna jako zakladni
studijni material.

## Podekovani

Kod pro tento workshop je prejaty z [blogu](https://medium.com/@martin.sikora/node-js-websocket-simple-chat-tutorial-2def3a841b61) Martina Sikory.

## Workshop

Tato sekce obsahuje popis kroku potrebnych pro realizaci jednoduche chatovaci aplikace.

### Zakladni struktura

Na zacatku mate k dispozici 3 soubory ve 2 slozkach. Slozka **server** 
obsahuje soubor *server.js* s kodem serverove casti. Ta ma na starost 
prijimani zprav od uzivatelu a preposilani je ostatnim. Bude take 
drzet historii zprav, seznam prihlasenych uzivatelu a prirazovat
jim barvy.

Slozka **client** obsahuje dva soubory. *index.html* je stranka s 
uzivatelskym rozhranim aplikace. Je uz hotova a nebudeme v ni delat zadne 
zmeny. *frontend.js* obsahuje javascriptovy kod potrebny pro pripojeni k 
serverove casti - posilani a prijimani zprav na/z server/u.

### Posilani zprav

Na zacatku musime naucit klienta a server jak spolu komunikovat. 
Soubor *server/serverj.js* obsahuje kod, ktery vytvori a spusti
server schopny prijimat a posilat zpravy. Nicmene se zpravami nic
nedela.

Jako prvni musime uzivateli umoznit se prihlasit. K tomu musi byt
server schopny udrzet si seznam pripojenych klientu. Do sekce
**Global Variables** v souboru *server/server.js* vytvorte promennou
**clients**:

```
// list of currently connected clients (users)
var clients = [ ];
```




Vlozte nasledujici na konec souboru *server/server.js*:

```
// This callback function is called every time someone
// tries to connect to the WebSocket server
wsServer.on('request', function(request) {
  // accept connection - you should check 'request.origin' to
  // make sure that client is connecting from your website
  // (http://en.wikipedia.org/wiki/Same_origin_policy)
  var connection = request.accept(null, request.origin); 

  // we need to know client index to remove them on 'close' event
  var index = clients.push(connection) - 1;
  var userName = false;

  console.log((new Date()) + ' Connection accepted.');


  
  });

```

1. Nyni zkuste server pustit. V terminalu prejdete do slozky server
a zavolejte **node server.js**. Server by mel vypsat 
`Server is listening on port 1337`. 
1. Otevrete soubor *client/index.html* ve Firefoxu.
1. Server by mel do konzole vypsat `Connection accepted.`

Ted server sice umi prijmout spojeni, ale stale nevi, co ma delat s 
prichazejicimi zpravami. Pro zacatek je proste preposleme vsem
prihlasenym klientum.

Do funkce zpracovavajici request vlozte nasledujici:

```
// user sent some message
connection.on('message', function(message) {
    if (message.type === 'utf8') { // accept only text

        var obj = {
            time: (new Date()).getTime(),
            text: htmlEntities(message.utf8Data),
        };

        // broadcast message to all connected clients
        var json = JSON.stringify({ type:'message', data: obj });
        for (var i=0; i < clients.length; i++) {
            clients[i].sendUTF(json);
        }
    }

});
```

Pokud bychom ted restartovali server a zkusili se pripojit, nas klient
by na zpravy nijak nereagoval. Musime ho to naucit.

Do souboru **client/frontend.js** vlozte nasledujici:

```
 // most important part - incoming messages
connection.onmessage = function (message) {
    // try to parse JSON message. Because we know that the server
    // always returns JSON this should work without any problem but
    // we should make sure that the massage is not chunked or
    // otherwise damaged.
    try {
        var json = JSON.parse(message.data);
    } catch (e) {
        console.log('Invalid JSON: ', message.data);
        return;
    }
    
    if (json.type === 'message') { // it's a single message
        // let the user write another message
        input.removeAttr('disabled'); 
        addMessage(json.data.author, json.data.text,
                     new Date(json.data.time));
    } else {
        console.log('Hmm..., I\'ve never seen JSON like this:', json);
    }
    };
```

Restartujte server a znovu nactete klienta v prohlizeci. Po odeslani 
zpravy by se vam mela zobrazit v okne.

### Vlastni jmeno pro uzivatele

Nyni zajistime, aby se u zprav zobrazovalo jmeno autora. Pro jednoduchost
se dohodneme, ze prvni zprava poslana z klienta na server bude jmeno.
Jinymi slovy, jako jmeno uzivatele se pouzije to, co jako prvni 
napise do zadavaciho pole.

Do souboru *server/server.js*, do funkce zpracovavajici zpravy od 
uzivatele, vlozte nasledujici na jeji zacatek (hned za radek `if (message.type === ...`:

```
if (userName === false) {
    // remember user name
    userName = htmlEntities(message.utf8Data);

    console.log((new Date()) + ' User is known as: ' + userName);
    
    return; //no need to send user's name back
}
```

A v teze funkci pridejte do objektu **obj** pole autor:
```
var obj = {
    time: (new Date()).getTime(),
    text: htmlEntities(message.utf8Data),
    author: userName,
};
```

1. Restartujte server a znovu nactete stranku v prohlizeci.
1. Napiste sve jmeno a odeslete. Na strance by nemelo byt nic videt,
ale v konzoli serveru uvidite `User is known as: ... `.
1. Napiste dalsi zpravu. V okne zprav by se mela zobrazit s vasim jmenem.

### Vypis historie pro noveho uzivatele

Nyni si zajistime, aby nove prihlaseni uzivatele dostali vypis posledni 
zprav.

Do souboru *server/server.js* vlozte do sekce **Global Variables**
promennou pro ukladani historie:

```
// latest 100 messages
var history = [ ];
```

Nasledne vlozte do funkce zpracovavajici prijate zpravy, pote co je 
vytvorena promenna **obj**:

```
history.push(obj);
history = history.slice(-100);

```

Nyni sice server historii uklada, ale jeste ji neposila. Chceme, aby se 
posilala pouze pro nove uzivatele, proto nasledujici kod vlozime
do funkce zpracovavaji pozadavky `wsServer.on('request', function(request) { ...`, nikoliv do funkce zpracovavajici zpravy od uzivatelu:

```
  // send back chat history
  if (history.length > 0) {
    connection.sendUTF(
        JSON.stringify({ type: 'history', data: history} ));
  }
```

Ted sice uz server historii posila, ale otevreme-li si klienta ve dvou 
zalozkach prohlizece, stale zadnou neuvidime. Je treba pridat
podporu pro historii i do nej. Do souboru *client/frontend.js* vlozte
nasledujici do funkce pro zpracovani zprav ze serveru (za konec
bloku `if`:

```
else if (json.type === 'history') { // entire message history
    // insert every single message to the chat window
    for (var i=0; i < json.data.length; i++) {
        addMessage(json.data[i].author, json.data[i].text,
        new Date(json.data[i].time));
    }
}
```


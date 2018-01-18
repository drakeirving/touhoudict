// populate jp->en

for(genre of Object.keys(touhoudict.en_jp)){
  for(k of Object.keys(touhoudict.en_jp[genre])){
    touhoudict.jp_en[genre][touhoudict.en_jp[genre][k]] = k;
  }
}

// the stuff that does the work

var translate_all = function(dict, q){
  if(!touhoudict.hasOwnProperty(dict)){
    console.error("touhoudict: Not a valid dictionary (" + Object.keys(touhoudict).join(", ") + ")");
    return false;
  }
  var c = 0;
  var elems = document.querySelectorAll(q);
  for(var i = 0; i < elems.length; i++){
    var e = elems[i];
    var x = e.textContent;
    for(genre of Object.keys(touhoudict.jp_en)){
      if(touhoudict[dict][genre].hasOwnProperty(x)){
        e.textContent = touhoudict[dict][genre][x];
        c++;
      }
    }
  }
  console.info("touhoudict: Translated " + c + " instances.");
  return (c > 0);
};

var jp2en_all = translate_all.bind(this, "jp_en");
var en2jp_all = translate_all.bind(this, "en_jp");

// actually run now

jp2en_all("option, article li, .result td[style]");

// ==UserScript==
// @name         touhoudict
// @namespace    https://drakeirving.github.io/touhoudict/
// @version      2.1.1
// @description  https://drakeirving.github.io/touhoudict/
// @author       drakeirving
// @match        https://toho-vote.info/*
// @grant        none
// @require      thdict_data.js
// ==/UserScript==

(function() {
  'use strict';

  let treeWalker = document.createTreeWalker(
    document.body,
    NodeFilter.SHOW_ELEMENT,
    (function(){
      let stuff = new Set(["a","h2","h3","dt","dd","em","input","p","optgroup","option","button","li","span","time", "i"]);
      return {
        acceptNode: function(node) {
          return (stuff.has(node.localName)) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP;
        }
      };
    })()
  );

  function process(node){
    if(node.localName === "optgroup"){
      // replace label text
      let s = translate(node.baseURI, node.label);
      if(s !== undefined){
        node.label = s;
      }
    }
    else if(node.childNodes.length > 0){
      // replace element's text nodes' content
      [... node.childNodes]
      .filter(a => a.nodeType === Node.TEXT_NODE && !/^\s*$/.test(a.textContent))
      .forEach(t => {
        let s = translate(t.baseURI, t.textContent);
        if(s !== undefined){
          t.textContent = s;
        }
      });
    }
    else if(node.localName === "input" && node.placeholder !== undefined){
      // replace placeholder text
      let s = translate(node.baseURI, node.placeholder);
      if(s !== undefined){
        node.placeholder = s;
      }
    }
  }

  function translate(uri, s){
    let res = dict["common"][s];
    if(res !== undefined) return res;

    uri = uri.split("//")[1];
    if(uri in dict) res = dict[uri][s];
    if(res !== undefined) return res;

    return undefined;
  }

  while(treeWalker.nextNode()){
    process(treeWalker.currentNode);
  }

})();

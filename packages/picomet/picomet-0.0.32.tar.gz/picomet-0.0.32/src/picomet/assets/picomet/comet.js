var __async = (__this, __arguments, generator) => {
  return new Promise((resolve, reject) => {
    var fulfilled = (value) => {
      try {
        step(generator.next(value));
      } catch (e) {
        reject(e);
      }
    };
    var rejected = (value) => {
      try {
        step(generator.throw(value));
      } catch (e) {
        reject(e);
      }
    };
    var step = (x) => x.done ? resolve(x.value) : Promise.resolve(x.value).then(fulfilled, rejected);
    step((generator = generator.apply(__this, __arguments)).next());
  });
};
import Alpine from "alpinejs";
export function getCookie(cookieName) {
  const name = cookieName + "=";
  const ca = document.cookie.split(";");
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == " ") {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
export function getFullXPath(element) {
  if (!(element instanceof Element))
    return;
  const path = [];
  let currentNode = element;
  while (currentNode !== document.documentElement) {
    let count = 0;
    for (const siblingNode of Array.from(currentNode.parentNode.children)) {
      if (siblingNode.nodeType === Node.ELEMENT_NODE && siblingNode.tagName === currentNode.tagName) {
        count++;
      }
      if (siblingNode === currentNode) {
        break;
      }
    }
    const tagName = currentNode.tagName.toLowerCase();
    path.unshift(`${tagName}[${count}]`);
    const parentNode = currentNode.parentNode;
    if (parentNode instanceof Element) {
      currentNode = parentNode;
    }
  }
  path.unshift("html[1]");
  return `/${path.join("/")}`;
}
function getParamTargets(urlPrevious, urlNew) {
  const targets = [];
  const paramsPrevious = new URL(urlPrevious).searchParams;
  const paramsNew = new URL(urlNew).searchParams;
  paramsNew.forEach((value, key) => {
    if (value != paramsPrevious.get(key)) {
      targets.push(`?${key}`);
    }
  });
  return targets;
}
function handleClick(event) {
  event.preventDefault();
  const currentTarget = event.currentTarget;
  const { href } = currentTarget;
  if (location.href != new URL(href).href) {
    update(
      location.pathname != new URL(href).pathname ? ["&page"] : getParamTargets(location.href, href) || ["&x"],
      href,
      location.pathname != new URL(href).pathname
    ).then((data) => {
      if (!("redirect" in data)) {
        history.pushState({}, "", href);
      }
    }).catch(() => {
    });
  }
}
function getMetaKeyValues(el) {
  return [
    ["name", el.getAttribute("name")],
    ["property", el.getAttribute("property")],
    ["http-equiv", el.getAttribute("http-equiv")]
  ];
}
function appendToHead(el) {
  const copiedEl = el.cloneNode(true);
  if (copiedEl instanceof Element) {
    copiedEl.removeAttribute("x-head");
    document.head.appendChild(copiedEl);
  }
}
document.addEventListener("alpine:init", () => {
  Alpine.directive("head", (el, _, { cleanup: cleanup2 }) => {
    const tag = el.tagName.toLowerCase();
    if (tag == "title") {
      document.title = el.textContent;
    } else if (tag == "meta") {
      const keyValues = getMetaKeyValues(el);
      for (const keyValue of keyValues) {
        if (keyValue[1]) {
          const meta = document.head.querySelector(
            `meta[${keyValue[0]}="${keyValue[1]}"]`
          );
          if (meta instanceof Element) {
            meta.setAttribute("content", el.getAttribute("content"));
          } else {
            appendToHead(el);
          }
        }
      }
    }
    cleanup2(() => {
      if (tag == "title") {
        document.title = "";
      } else if (tag == "meta") {
        const keyValues = getMetaKeyValues(el);
        for (const keyValue of keyValues) {
          if (keyValue[1]) {
            document.head.querySelector(`meta[${keyValue[0]}="${keyValue[1]}"]`).remove();
          }
        }
      }
    });
  });
  Alpine.directive(
    "form",
    (el, _, { cleanup: cleanup2 }) => {
      function handleSubmit(event) {
        event.preventDefault();
        const body = new FormData(el);
        const url = new URL(window.location.toString());
        const method = el.getAttribute("method");
        if (method && method.toLowerCase() == "post") {
          fetch(url, {
            method,
            body,
            headers: {
              Targets: JSON.stringify([getFullXPath(el)])
            }
          }).then((response) => {
            handleResponse(response).catch(() => {
            });
          }).catch(() => {
          });
        } else if (!method || method.toLowerCase() == "get") {
          const actionUrl = new URL(el.action);
          const formData = new FormData(el);
          formData.forEach((value, key) => {
            if (typeof value == "string") {
              actionUrl.searchParams.append(key, value);
            }
          });
          update([getFullXPath(el)], actionUrl.toString()).then((data) => {
            if (!("redirect" in data)) {
              history.pushState({}, "", actionUrl);
            }
          }).catch(() => {
          });
        }
      }
      el.addEventListener("submit", handleSubmit);
      cleanup2(() => {
        el.removeEventListener("click", handleSubmit);
      });
    }
  );
  Alpine.directive(
    "link",
    (el, _, { cleanup: cleanup2 }) => {
      el.addEventListener("click", handleClick);
      cleanup2(() => {
        el.removeEventListener("click", handleClick);
      });
    }
  );
  Alpine.directive("prop", (el, { value, expression }) => {
    Alpine.addScopeToNode(el, {
      [value]: JSON.parse(expression.replace(/&quot;/g, '"'))
    });
  }).before("data");
});
window.Alpine = Alpine;
Alpine.start();
export function update(targets, url, scrollToTop) {
  return __async(this, null, function* () {
    const response = yield fetch(new URL(url || window.location.toString()), {
      headers: {
        Targets: JSON.stringify(targets)
      }
    });
    return yield handleResponse(response, scrollToTop);
  });
}
export function go(path, scrollToTop) {
  const url = new URL(path, window.location.origin);
  scrollToTop = scrollToTop == null ? true : scrollToTop;
  update(["&page"], url.toString(), scrollToTop).then((data) => {
    if (!("redirect" in data)) {
      history.pushState({}, "", url.toString());
    }
  }).catch(() => {
  });
}
function handleNavigate() {
  Alpine.store("previousUrl", location.href);
}
navigation.addEventListener("navigate", handleNavigate);
function handlePopState() {
  const previousUrl = Alpine.store("previousUrl");
  if (typeof previousUrl == "string") {
    const newUrl = location.toString();
    update(
      new URL(previousUrl).pathname != new URL(newUrl).pathname ? ["&page"] : getParamTargets(previousUrl, newUrl) || ["&x"]
    ).catch(() => {
    });
  }
}
window.addEventListener("popstate", handlePopState);
export function cleanup() {
  navigation.removeEventListener("navigate", handleNavigate);
  window.removeEventListener("popstate", handlePopState);
}
export function call(action, payload, keys) {
  return __async(this, null, function* () {
    const url = new URL(window.location.toString());
    let formData;
    if (payload instanceof FormData) {
      formData = payload;
    } else {
      formData = new FormData();
      for (const key in payload) {
        const value = payload[key];
        if (typeof value == "string" || value instanceof Blob) {
          formData.append(key, value);
        } else if (typeof value == "number" || typeof value == "boolean") {
          formData.append(key, JSON.stringify(value));
        }
      }
    }
    const response = yield fetch(url, {
      method: "post",
      body: formData,
      headers: {
        Action: action,
        Keys: JSON.stringify(keys || []),
        "X-CSRFToken": getCookie("csrftoken")
      }
    });
    yield handleResponse(response);
  });
}
function handleResponse(response, scrollToTop) {
  return __async(this, null, function* () {
    const data = yield response.json();
    if ("redirect" in data) {
      history.pushState({}, "", data.redirect);
      if (data.update) {
        const targets = ["&page"];
        for (const target of JSON.parse(
          response.headers.get("Targets") || "[]"
        )) {
          if (typeof target == "string" && targets.indexOf(target) !== -1) {
            targets.push(target);
          }
        }
        update(targets, null, location.pathname != data.redirect).catch(() => {
        });
      }
    } else {
      if (scrollToTop) {
        window.scrollTo(0, 0);
      }
      for (const target in data) {
        const partial = data[target];
        const el = document.evaluate(
          target,
          document,
          null,
          XPathResult.FIRST_ORDERED_NODE_TYPE,
          null
        ).singleNodeValue;
        if (el instanceof Element) {
          for (const id in partial.css) {
            if (!document.querySelector(`[data-style-id="${id}"]`)) {
              const linkElement = document.createElement("link");
              linkElement.rel = "stylesheet";
              linkElement.href = partial.css[id];
              linkElement.setAttribute("data-style-id", id);
              document.head.appendChild(linkElement);
            }
          }
          for (const id in partial.js) {
            if (!document.querySelector(`[data-script-id="${id}"]`)) {
              import(partial.js[id]).then((module) => {
                Object.keys(module).forEach((key) => {
                  if (key == "cleanup") {
                    window[`${id}_cleanup`] = module[key];
                  } else {
                    window[key] = module[key];
                  }
                });
              }).catch(() => {
              });
            }
          }
          el.outerHTML = partial.html;
        }
      }
    }
    return data;
  });
}

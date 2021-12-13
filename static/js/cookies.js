function getCookie(cname) {
    let cookies = document.cookie;
    let cookieKVSs = cookies.split("; ");       // KVSs: key-value strings (e.g. ["key1=val1", "key2=val2", ...])
    for (let i in cookieKVSs) {
        let cookieKVS = cookieKVSs[i];
        let cookieKVP = cookieKVS.split("=");   // KVP: key-value pair (e.g. ["key1", "val1"])
        if (cookieKVP[0] == String(cname)) { return cookieKVP[1]; }
    }
    return "";
}

function checkCookieExists(cname) {
    cookieRequested = getCookie(cname);
    if (cookieRequested != "") { return true; }
    return false;
}

function checkCookieMatchesVal(cname, val) {
    if (checkCookieExists(cname)) { if (getCookie(cname) == val) { return true; } }
    return false;
}

function setCookie(cname, val) {
    let cookieNew = String(cname) + "=" + String(val) + "; expires=Thu, 31 Dec 2099 23:59:59 UTC; path=/;";
    document.cookie = cookieNew;
}

function delCookie(cname) {
    let cookieSelected = String(cname) + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    document.cookie = cookieSelected;
}

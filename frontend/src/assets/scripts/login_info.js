function parseJwt(token) {
    if (!token || !token.includes('.')) {
        throw new Error('Invalid token format');
    }

    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(
        atob(base64)
            .split('')
            .map(function (c) {
                return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
            })
            .join('')
    );

    return JSON.parse(jsonPayload);
}

function isTokenExpired(token) {
    const currentTime = Math.floor(Date.now() / 1000); // Convert to seconds
    return token.exp < currentTime;
}



function getCookie(name) {
    const cookieName = name + '=';
    const decodedCookie = decodeURIComponent(document.cookie);
    const cookieArray = decodedCookie.split(';');

    for (let i = 0; i < cookieArray.length; i++) {
        let cookie = cookieArray[i];
        while (cookie.charAt(0) === ' ') {
            cookie = cookie.substring(1);
        }
        if (cookie.indexOf(cookieName) === 0) {
            return cookie.substring(cookieName.length, cookie.length);
        }
    }
    return '';
}

// function to check if jwt token is there and if it is valid
export function checkCookie() {
    const token = getCookie('access_token');
    console.log(token);
    if (token !== '') {
        return token;
    } else {
        return false;
    }
}

export function checkValidToken() {
    const token = checkCookie();
    if (!token) {
        return false; // 'invalid';
    }
    
    console.log("processing token");
    const parsedToken = parseJwt(token); // Fixed variable name
    console.log(parsedToken)
    if (isTokenExpired(parsedToken)) {
        return false; //'invalid'; // Token is expired
    }
    return true; //'valid';
}



export function setCookie(name, value, minutes) {
    const date = new Date();
    date.setTime(date.getTime() + minutes * 60 * 1000); // Set expiration time in milliseconds

    const expires = 'expires=' + date.toUTCString();
    document.cookie = name + '=' + value + ';' + expires + ';path=/';
}






import { saved_just_now } from "./store";

let timeout;
const broadcast_saved = () => {
    saved_just_now.set(true);
    if (timeout) clearTimeout(timeout);
    timeout = setTimeout(() => {
        saved_just_now.set(false);
    }, 1000);
}

export const query = async (url, method='GET', data=null, parse='JSON') => {
    method = method.toUpperCase()
    parse = parse.toUpperCase()
    let params = {
        method,
        headers: {}
    }
    // Determine URL.
    if (['GET', 'DELETE'].includes(method) && data !== null) {
        const params = new URLSearchParams(data);
        url = `/api${url}?${params.toString()}`;
    } else {
        url = `/api${url}`;
    }
    // Encode data.
    if (['POST', 'PUT'].includes(method) && data !== null) {
        if (parse === 'JSON') {
            params.body = JSON.stringify(data)
            params.headers['Content-Type'] = 'application/json';
        } else if (parse === 'FILE') {
            const formData = new FormData();
            formData.append('file', data);
            formData.append('mime_type', data.type);
            params.body = formData;
        }
    }
    // Send request.
    try {
        const response = await fetch(url, params);
        const result = await response.json();
        if (response.ok) {
            if(['POST', 'PUT', 'DELETE'].includes(method)) broadcast_saved();
            return result
        } else {
            result.detail.forEach(item => console.error(item));
            throw new Error('Network response was not ok ' + response.statusText);
        }
    }
    catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}
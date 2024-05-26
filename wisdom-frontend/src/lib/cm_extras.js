// Gets the line number and line text between two lines.
const getLines = (editor, start, end) => {
    const lines = [];
    for (let i = start; i <= end; i++) {
        const text = editor.getLine(i);
        if (typeof text !== 'undefined') lines.push({line: i, text});
    }
    return lines;
}

// Gets the line number and line text for the whole document.
const scanDocument = editor => {
    const lines = [];
    editor.eachLine((lineHandle) => {
        const line = lineHandle.lineNo();
        const text = lineHandle.text;
        lines.push({line, text});
    });
    return lines;
}

// Returns an image DOM element.
const createResponsiveImage = srcUrl => {
    const img = document.createElement('img');
    img.src = srcUrl;
    return img;
}

// Finds markdown image URL.
const getImgUrl = text => {
    const match = text.match(/!\[([^\]]*)\]\(([^)]*)\)/);
    if (match) {
        return match[2];
    } else {
        return null;
    }
}
// Adds widgets and keeps a trace to remove them later.
class manageWidgets {
    constructor(editor) {
        this.editor = editor;
        this.line_widgets = [];
    }
    add(line, element) {
        this.line_widgets[line] = this.editor.addLineWidget(line, element);
    }
    update(lines) {
        lines.forEach(i => {
            const img = getImgUrl(i.text);
            const line = this.line_widgets[i.line];
            if (typeof line === 'object') line.clear();
            if (img !== null) this.add(i.line, createResponsiveImage(img));
        });
    }
}

// Send save 
let timeout;
const save = (editor, dispatch) => {
    if (timeout) clearTimeout(timeout);
    timeout = setTimeout(() => {
        dispatch('change', editor.getValue());
    }, 1500);
}

// Wrapper.
export const extras = (editor, dispatch) => {
    const mw = new manageWidgets(editor);
    mw.update(scanDocument(editor));
    editor.on('change', (instance, changeObj) => {
        mw.update(getLines(editor, changeObj.from.line, changeObj.to.line));
        save(editor, dispatch);
    });
}
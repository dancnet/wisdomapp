import { writable, get } from 'svelte/store';
import { query } from '$lib/api'

const writable2 = (fun) => { 
    const { subscribe, set, update } = writable([]);
    const reload = () => { fun(set)};
    return { subscribe, set, update, reload};
}

export const mindmaps_data = writable2(set => {
    query('/mindmaps/').then(result => { set(result)});
});
export const selected_mindmap = writable(1);
export const nodes_data = writable2(set => {
    set([]);
    query(`/mindmaps/${get(selected_mindmap)}/nodes/`).then(result => { set(result) });
});
export const node_selected = writable(null);
export const show_modal = writable(null);
export const saved_just_now = writable(false);
import { get } from 'svelte/store';
import { nodes_data, node_selected } from '$lib/store';
import { query } from '$lib/api';

const loop = (data, element, result = []) => {
    if (Number.isInteger(element)) element = data.find(i => i.id === element);
    if (!element) return null;
    result.push(element);
    if (element.expanded === 1) {
        data.forEach(i => {
            if (i.parentid === element.id) loop(data, i, result);
        });
    }
    return result;
}
export const eligible_nodes = () => loop(get(nodes_data), get(node_selected));

export class Random {
    constructor(data) {
        this.data = data;
        this.position = 1;
        this.length = this.data.length;
        this.shuffle();
    }
    static async init_random_node() {
        const eligibleNodes = eligible_nodes();
        const all_nodes = await Promise.all(eligibleNodes.map(node => query(`/nodes/${node.id}`)));
        const filtered_nodes = all_nodes.filter(node => node.markdown !== '');
        return new Random(filtered_nodes);
    }
    static async init_quiz() {
        const eligibleNodes = eligible_nodes();
        const all_questions = await Promise.all(eligibleNodes.map(node => query(`/nodes/${node.id}/questions/`)));
        const all_questions_flat = all_questions.flat();
        return new Random(all_questions_flat);
    }
    shuffle() {
        for (let i = this.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [this.data[i], this.data[j]] = [this.data[j], this.data[i]];
        }
    }
    next() {
        if (this.length === 0) return null;
        const data = this.data[this.position - 1];
        if (this.position == this.length) {
            this.position = 1;
            this.shuffle();
        } else {
            this.position++;
        }
        return data;
    }
}
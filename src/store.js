// store.js
import { writable } from 'svelte/store';

export const playersStore = writable([]);
export const userStore = writable("");  // add this
export const spotifyAccessToken = writable("");  // add this

/* global window */
window.jQuery = window.$ = require('jquery');

const $ = window.$;

require('bootstrap');

$(() => {
    $('#id_participants').chosen();
});

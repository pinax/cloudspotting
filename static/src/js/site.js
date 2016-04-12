/* global window document */
window.jQuery = window.$ = require('jquery');

const $ = window.$;

require('bootstrap');

const React = require('react');
const ReactDOM = require('react-dom');
const ImagePanel = require('pinax-images-panel');

$(() => {
    const imagePanelElement = document.getElementById('image-panel');
    if (imagePanelElement) {
      const imagesUrl = imagePanelElement.getAttribute('data-images-url');
      const imageSetId = parseInt(imagePanelElement.getAttribute('data-image-set-id'), 10);
      const uploadUrl = imagePanelElement.getAttribute('data-upload-url');
      ReactDOM.render(<ImagePanel imagesUrl={imagesUrl} initialUploadUrl={uploadUrl} initialImageSetId={imageSetId}/>, imagePanelElement);
    }
});

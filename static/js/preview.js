var ClosingPage = angular.module('ClosingPage', ['ui.bootstrap']);

ClosingPage
.component('fileUpload', FileUpload)
.component('pdfDisplay', PDFDisplay)
.component('pptDisplay', PPTDisplay)
.component('gifDisplay', GIFDisplay)
.controller('Preview', Preview);
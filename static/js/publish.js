var ClosingPage = angular.module('ClosingPage', ['ui.bootstrap']);

ClosingPage
.component('fileUpload', FileUpload)
.component('pdfDisplay', PDFDisplay)
.component('pptDisplay', PPTDisplay)
.component('gifDisplay', GIFDisplay)
.directive('backImg', function() {
    return function (scope, element, attrs) {
        attrs.$observe('backImg', function (value) {
            element.css({
                'background-image': 'url(' + value + ')',
                'background-size': 'cover'
            });
        });
    }
}).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{(').endSymbol(')}');
})
.controller('Publish', Publish);
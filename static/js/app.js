var ClosingPage = angular.module('ClosingPage', ['ui.router','ui.bootstrap']);

ClosingPage.controller('TemplatePickerCtrl', TemplatePickerCtrl)
.component('fileUpload', FileUpload)
.component('pdfDisplay', PDFDisplay)
.component('pptDisplay', PPTDisplay)
.component('gifDisplay', GIFDisplay)
.controller('TemplateOneCtrl', TemplateOneCtrl)
.directive('backImg', function() {
    return function (scope, element, attrs) {
        attrs.$observe('backImg', function (value) {
            element.css({
                'background-image': 'url(' + value + ')',
                'background-size': 'cover'
            });
        });
    }
})
.service('Template', TemplateService)
.config(function($stateProvider, $urlRouterProvider, $interpolateProvider) {

    $interpolateProvider.startSymbol('{(').endSymbol(')}');

    $urlRouterProvider.otherwise('/choose-template/preview-one');

    $stateProvider

        .state('choose-template', {
            url: '/choose-template',
            templateUrl: '/partials/choose-template/choose-template.pug',
            controller: 'TemplatePickerCtrl'
        })

        .state('choose-template.preview-one', {
            url: '/preview-one',
            templateUrl: '/partials/choose-template/view-one.pug'
        })

        .state('choose-template.preview-two', {
            url: '/preview-two',
            templateUrl: '/partials/choose-template/view-two.pug'
        })

        .state('template-one', {
            url: '/template-one',
            templateUrl: '/partials/template-one.pug',
            controller: 'TemplateOneCtrl'
        })

        .state('template-two', {
            url: '/template-two',
            templateUrl: 'partials/template-two.pug'
        })
});
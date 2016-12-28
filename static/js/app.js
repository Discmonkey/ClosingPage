var ClosingPage = angular.module('ClosingPage', ['ui.router']);

ClosingPage.controller('TemplatePickerCtrl', TemplatePickerCtrl)
.component('fileUpload', FileUpload)
.controller('TemplateOneCtrl', TemplateOneCtrl)
.controller('TemplateTwoCtrl', TemplateTwoCtrl)
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
            templateUrl: 'partials/template-two.pug',
            controller: 'TemplateTwoCtrl'
        });
});